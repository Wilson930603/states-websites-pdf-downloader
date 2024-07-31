from datetime import datetime
from typing import List, Optional
from urllib.parse import urljoin

from crawlers.base_crawlers.base import BaseCrawler


class GranicusCrawler(BaseCrawler):
    DOCUMENT_TYPE = "Minutes"
    FILE_EXTENSION = "pdf"
    MIN_YEAR = 2021
    DEFAULT_DATE_FORMAT = "%b %d, %Y"
    DEFAULT_DATE_COLUMN_HEADER = 'td[headers*="Date"]'
    DEFAULT_URL_HREF = 'a[href*="MinutesViewer"]'

    def __init__(
        self,
        url: str,
        municipality: str,
        commission: str,
        state: str,
        base_url: str,
        row_selector: str,
        document_type: str = DOCUMENT_TYPE,
        file_extension: str = FILE_EXTENSION,
        date_column_header: str = DEFAULT_DATE_COLUMN_HEADER,
        url_href: str = DEFAULT_URL_HREF,
        has_redirect: bool = False,
        date_format: str = DEFAULT_DATE_FORMAT,
        row_filter_keyword: Optional[str] = None,
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
        self.row_selector = row_selector
        self.date_column_header = date_column_header
        self.url_href = url_href
        self.has_redirect = has_redirect
        self.date_format = date_format
        self.row_filter_keyword = row_filter_keyword

    async def get_file_urls(self, existing_links: list) -> List[str]:
        download_urls = []

        # Get all rows related to the Planning and Zoning Board
        rows = await self.get_page().query_selector_all(self.row_selector)
        row_text = await rows[0].inner_text()
        if self.row_filter_keyword:
            rows = [
                row
                for row in rows
                if self.row_filter_keyword.lower() in row_text.lower()
            ]

        for row in rows:
            row_year = await self.get_date_year_from_row(row)

            if row_year >= self.MIN_YEAR:
                # Find the download link in the row
                download_url = await self.get_download_url_from_row(row)
                if not download_url:
                    continue
                self.logger.debug(f"Download URL: {download_url}")
                download_urls.append(download_url)
        return download_urls

    async def get_download_url_from_row(self, row):
        download_href = await row.query_selector(self.url_href)
        if download_href:
            download_url = urljoin(
                self.base_url, await download_href.get_attribute("href")
            )
            if self.has_redirect:
                download_url = await self.get_redirected_url(download_url)
            return download_url
        else:
            self.logger.debug("No download link found in row")
            return None

    async def get_date_year_from_row(self, row) -> int:
        date_cell = await row.query_selector(self.date_column_header)
        if not date_cell:
            self.logger.debug(f"No date cell found in row: {await row.inner_text()}")
            return 0
        date_text = await date_cell.inner_text()
        date_text = date_text.replace("\u00a0", " ").strip()
        date_text = date_text.split("-")[0].strip()
        try:
            date = datetime.strptime(date_text, self.date_format)
            return date.year
        except ValueError:
            self.logger.debug(f"Failed to parse date: {date_text}")
            return 0

    async def get_redirected_url(self, url: str) -> str:
        try:
            redirected_url = await self.get_redirect(url)
            return redirected_url
        except Exception:
            self.logger.exception(
                f"Error encountered while getting redirected URL for {url}"
            )
        return url
