import asyncio
import os
import uuid
from abc import abstractmethod
from typing import List
import logging
from urllib.parse import urljoin

import httpx
from playwright.async_api import (
    async_playwright,
    PlaywrightContextManager,
    Playwright,
    Browser,
    Page,
)
from playwright_stealth import stealth_async

from config import log_config
from config.log_config import ContextLoggerAdapter

log_config.setup_logging()  # TODO: Potentially move somewhere else


class BaseCrawler:
    MIN_YEAR = 2021

    def __init__(
        self,
        url: str,
        commission: str,
        municipality: str,
        state: str,
        document_type: str,
        file_extension: str,
    ):
        self.url: str = url
        self.commission: str = commission
        self.municipality: str = municipality
        self.state: str = state
        self.document_type: str = document_type
        self.file_extension: str = file_extension
        self.playwright_context: PlaywrightContextManager | None = None
        self.playwright: Playwright | None = None
        self._browser: Browser | None = None
        self._page: Page | None = None
        self.logger = self.setup_logger()
        self.download_dir = "./downloaded_files"

    @abstractmethod
    async def perform_interactions(self) -> None:
        pass

    @abstractmethod
    async def get_file_urls(self, existing_links: List[str]) -> List[str]:
        pass

    async def download_file(self, url: str) -> None:
        filename = self.get_filename()
        save_path = os.path.join(self.download_dir, filename)
        if not os.path.exists(self.download_dir):
            os.makedirs(self.download_dir)

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

        backoff_time = 1  # initial backoff time in seconds

        while True:
            try:
                async with httpx.AsyncClient(verify=False) as client:
                    response = await client.get(url, headers=headers)
                    if response.status_code == 200:
                        with open(save_path, "wb") as f:
                            f.write(response.content)
                        return
                    elif response.status_code == 429:
                        self.logger.warning(
                            f"Rate limited. Retrying after {backoff_time} seconds. URL: {url}"
                        )
                        await asyncio.sleep(backoff_time)
                        backoff_time = min(
                            backoff_time * 2, 60
                        )  # exponential backoff, max 60 seconds
                    else:
                        self.logger.warning(
                            f"Failed to download PDF from {url}, status code: {response.status_code}"
                        )
                        return
            except Exception as e:
                self.logger.exception(
                    f"Failed to download PDF from {url}. Error: {str(e)}"
                )
                return

    def get_filename(self) -> str:
        doc_id = uuid.uuid4()  # TODO: Implement generate_doc_id
        filename = f"doc_{doc_id}.{self.file_extension}"
        return filename

    async def crawl(self, debug: bool = False, stealth: bool = False) -> None:
        self.logger.debug(
            f"Starting {self.municipality} - {self.state} crawler at {self.url}"
        )
        await self.setup_browser(debug, stealth)
        existing_links: List[str] = []  # TODO: Implement fetch_existing_links
        self.logger.debug(f"Found {len(existing_links)} existing links")
        await self.get_page().goto(self.url)
        await self.perform_interactions()
        file_urls: List[str] = await self.get_file_urls(existing_links)
        self.logger.info(f"Found {len(file_urls)} new file urls")
        # remove existing links from file_urls and log which ones are duplicates
        for existing_link in existing_links:
            if existing_link in file_urls:
                file_urls.remove(existing_link)
                self.logger.info(f"Skipping already crawled url: {existing_link}")
        for file_url in file_urls:
            await self.download_file(file_url)
            # await self.store_document() TODO: Implement store_document, checks for file hash match
        await self.teardown_browser()

    async def get_redirect(self, url):
        async with httpx.AsyncClient(follow_redirects=False) as client:
            response = await client.head(url)
            if response.status_code in (301, 302):
                redirect_url = response.headers["Location"]
                if not redirect_url.startswith("http"):
                    redirect_url = urljoin(url, redirect_url)
                return redirect_url
        return None

    def setup_logger(self) -> ContextLoggerAdapter:
        context_str = f"{self.municipality}-{self.state}"
        return ContextLoggerAdapter(
            logging.getLogger(__name__), {"context": context_str}
        )

    async def setup_browser(self, debug: bool, stealth: bool) -> None:
        self.logger.debug("Setting up browser")
        self.playwright_context = async_playwright()
        self.playwright = await self.playwright_context.__aenter__()
        if debug:
            self._browser = await self.playwright.chromium.launch(headless=False)
        else:
            self._browser = await self.playwright.chromium.launch(headless=True)
        self._page = await self._browser.new_page()

        if stealth:
            self.logger.debug("Applying stealth settings")
            await stealth_async(self.get_page())

    async def teardown_browser(self) -> None:
        if self._browser:
            await self._browser.close()
        if self.playwright_context:
            await self.playwright_context.__aexit__(None, None, None)
        self.logger.debug("Browser teardown complete")

    def get_page(self) -> Page:
        if self._page is None:
            raise RuntimeError("Page is not initialized.")
        return self._page

    def get_browser(self) -> Browser:
        if self._browser is None:
            raise RuntimeError("Browser is not initialized.")
        return self._browser
