from abc import ABC
from typing import List
from urllib.parse import urljoin

from crawlers.base_crawlers.base import BaseCrawler


class CivicEngageCrawler(BaseCrawler, ABC):
    DOCUMENT_TYPE = "Minutes"
    FILE_EXTENSION = "pdf"
    MIN_YEAR = 2021
    DEFAULT_HREF = 'a[href*="View.ashx?M=M"]'
    BUTTON_VIEW_MORE_LOCATOR = 'a[id^="btnViewMore"]'

    def __init__(
        self,
        url: str,
        municipality: str,
        commission: str,
        state: str,
        document_type: str = DOCUMENT_TYPE,
        file_extension: str = FILE_EXTENSION,
        url_href: str = DEFAULT_HREF,
    ):
        super().__init__(
            url=url,
            municipality=municipality,
            commission=commission,
            state=state,
            document_type=document_type,
            file_extension=file_extension,
        )
        self.url_href = url_href

    async def perform_interactions(self) -> None:
        # Wait for the initial content to be available
        await self.get_page().wait_for_selector("ul.years", timeout=60000)

    async def get_file_urls(self, existing_links: list) -> List[str]:
        file_urls = []

        year_links = await self.get_year_links()
        self.logger.debug(f"Found {len(year_links)} year links")

        for year_link in year_links:
            year = await self.get_year_from_link(year_link)
            if year < self.MIN_YEAR:
                continue

            await self.handle_year_click(year_link)
            file_urls.extend(await self.extract_file_urls_for_year(existing_links))
        # Filter any possible repeated link
        file_urls = list(set(file_urls))
        return file_urls

    async def get_year_links(self) -> List:
        # Get all visible year links and additional year links from "View More"
        visible_year_links = await self.get_page().query_selector_all(
            'ul.years > li > a[id^="a"]'
        )
        view_more_year_links = await self.get_view_more_year_links()
        return (
            view_more_year_links + visible_year_links
        )  # Put view_more_year first, as if we click on the others first, the view_more_link will disappear

    async def get_view_more_year_links(self) -> List:
        view_more_year_links = []
        view_more_link = await self.get_page().query_selector(
            self.BUTTON_VIEW_MORE_LOCATOR
        )
        if view_more_link:
            await view_more_link.hover()
            await self.get_page().click(self.BUTTON_VIEW_MORE_LOCATOR)
            await self.get_page().wait_for_timeout(1000)
            view_more_year_links = await self.get_page().query_selector_all(
                'div[id^="yearDD"] a[id^="anchYearDD"]'
            )
        return view_more_year_links

    async def get_year_from_link(self, year_link) -> int:
        year_text = await year_link.inner_text()
        try:
            return int(year_text)
        except ValueError:
            self.logger.warning(f"Invalid year format: {year_text}")
            return 0

    async def handle_year_click(self, year_link) -> None:

        year_id = await year_link.get_attribute("id")
        is_view_more_year_link = "anchYearDD" in year_id
        if is_view_more_year_link:
            # Click on every "View More" button until the year link is visible
            button_view_mores = await self.get_page().query_selector_all(
                self.BUTTON_VIEW_MORE_LOCATOR
            )
            for button_view_more in button_view_mores:
                await button_view_more.click()
                if await year_link.is_visible():
                    break

        await self.get_page().click(f"#{year_id}")
        await self.get_page().wait_for_load_state("networkidle", timeout=60000)
        await self.get_page().wait_for_timeout(1000)

    async def extract_file_urls_for_year(self, existing_links: list) -> List[str]:
        file_urls = []
        download_links = await self.get_page().query_selector_all(self.url_href)
        self.logger.debug(f"Found {len(download_links)} download links")

        for download_link in download_links:
            file_url = await download_link.get_attribute("href")
            if file_url:
                full_file_url = urljoin(self.url, file_url)
                if full_file_url not in existing_links:
                    file_urls.append(full_file_url)
                    self.logger.debug(f"Found PDF: {full_file_url}")

        return file_urls
