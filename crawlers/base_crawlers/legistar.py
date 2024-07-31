from abc import abstractmethod, ABC
from datetime import datetime
from typing import List
from urllib.parse import urljoin

from crawlers.base_crawlers.base import BaseCrawler


class LegistarCrawler(BaseCrawler, ABC):
    DOCUMENT_TYPE = "Minutes"
    FILE_EXTENSION = "pdf"
    ROW_SELECTOR = "tr.rgAltRow, tr.rgRow"
    DATE_ROW_SELECTOR = "td.rgSorted"
    DATE_FORMAT = "%m/%d/%Y"
    MIN_YEAR = 2021
    URL_HREF = 'a[href*="View.ashx?M=M"]'
    PAGINATION_SELECTOR = 'a[title="Next Page"]'

    def __init__(
        self,
        url: str,
        municipality: str,
        commission: str,
        state: str,
        base_url: str,
        document_type: str = DOCUMENT_TYPE,
        file_extension: str = FILE_EXTENSION,
        url_href: str = URL_HREF,
        pagination: bool = False,
    ):
        super().__init__(
            url=url,
            municipality=municipality,
            commission=commission,
            state=state,
            document_type=document_type,
            file_extension=file_extension,
        )
        self.base_url = base_url
        self.pagination = pagination
        self.url_href = url_href

    @abstractmethod
    async def set_filters(self) -> None:
        raise NotImplementedError(
            "set_date_filter method must be implemented in the subclass."
        )

    async def perform_interactions(self) -> None:
        await self.set_filters()

    async def get_file_urls(self, existing_links: list) -> List[str]:
        if self.pagination:
            return await self.get_file_urls_with_pagination()
        return await self.get_file_urls_from_page()

    async def get_file_urls_from_page(self) -> List[str]:
        download_urls = []
        # Get all rows in the table
        rows = await self.get_page().query_selector_all(self.ROW_SELECTOR)

        # Iterate through each row
        for row in rows:
            date_text = await row.query_selector(self.DATE_ROW_SELECTOR)
            if date_text:
                row_date_year = await self.get_date_year_from_row(row)
                if row_date_year >= self.MIN_YEAR:
                    download_cell = await row.query_selector(self.URL_HREF)
                    if download_cell:
                        download_href = await download_cell.get_attribute("href")
                        if download_href:
                            download_url = urljoin(self.base_url, download_href)
                            download_urls.append(download_url)

        return download_urls

    async def get_file_urls_with_pagination(self) -> List[str]:
        download_urls = []
        page_number = 1

        while True:
            # Log the current page number
            self.logger.info(f"Processing page {page_number}")

            # Get file URLs from the current page
            page_urls = await self.get_file_urls_from_page()
            download_urls.extend(page_urls)

            # Try a more general approach to find the next page link
            self.logger.info("Trying to find the next page link")
            current_page_link = await self.get_page().query_selector("a.rgCurrentPage")

            if current_page_link:
                self.logger.info(f"Current page link found: {current_page_link}")
                next_sibling = await current_page_link.evaluate_handle(
                    "node => node.nextElementSibling"
                )

                # Check if the next sibling is a valid element
                if next_sibling:
                    next_page_link = next_sibling.as_element()

                    if next_page_link:
                        self.logger.info(f"Next page link found: {next_page_link}")
                        await next_page_link.click()
                        await self.get_page().wait_for_timeout(6000)
                        page_number += 1
                    else:
                        self.logger.info(
                            "Next sibling is not a valid clickable element"
                        )
                        break
                else:
                    self.logger.info("No next sibling found for the current page link")
                    break
            else:
                self.logger.info("Current page link not found")
                break

        return download_urls

    async def get_date_year_from_row(self, row) -> int:
        date_text = await row.query_selector(self.DATE_ROW_SELECTOR)
        if not date_text:
            self.logger.debug("Date text not found in row")
            return 0
        try:
            date_str = await date_text.inner_text()
            return datetime.strptime(date_str, self.DATE_FORMAT).year
        except ValueError:
            self.logger.debug(f"Failed to parse date text '{date_text}'")
            return 0
