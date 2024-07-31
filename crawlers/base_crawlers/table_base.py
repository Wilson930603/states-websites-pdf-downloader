from abc import ABC, abstractmethod
from typing import List
from urllib.parse import urljoin
from crawlers.base_crawlers.base import BaseCrawler
import time

class TableCrawler(BaseCrawler, ABC):
    DOCUMENT_TYPE = "Minutes"
    FILE_EXTENSION = "pdf"
    MIN_YEAR = 2021

    def __init__(
        self,
        url: str,
        municipality: str,
        commission: str,
        state: str,
        row_selector: str,
        url_href: str,
        document_type: str = DOCUMENT_TYPE,
        file_extension: str = FILE_EXTENSION,
        has_redirect: bool = False,
        base_url: str | None = None,
    ):
        super().__init__(
            url=url,
            municipality=municipality,
            commission=commission,
            state=state,
            document_type=document_type,
            file_extension=file_extension,
        )
        self.row_selector = row_selector
        self.url_href = url_href
        self.has_redirect = has_redirect
        self.base_url = base_url

    @abstractmethod
    async def should_crawl_row(self, row) -> bool:
        raise NotImplementedError(
            "should_crawl_row method must be implemented in the subclass."
        )
 
    async def get_file_urls(self, existing_links: List[str]) -> List[str]:
        file_urls = []
        time.sleep(5)
        rows = await self.get_page().query_selector_all(self.row_selector)
        print(len(rows))
        for row in rows:
            if not await self.should_crawl_row(row):
                continue
            download_link = await row.query_selector(self.url_href)
            if download_link:
                pdf_url = await download_link.get_attribute("href")
                if pdf_url:
                    full_pdf_url = urljoin(self.url, pdf_url)
                    if self.has_redirect:
                        full_pdf_url = await self.get_redirect(full_pdf_url)
                    if self.base_url:
                        full_pdf_url = urljoin(self.base_url, pdf_url)
                    if full_pdf_url not in existing_links:
                        file_urls.append(full_pdf_url)
                        self.logger.debug(f"Found PDF: {full_pdf_url}")

        return file_urls
