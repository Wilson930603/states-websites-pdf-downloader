import re
from typing import List
from urllib.parse import urljoin

from crawlers.base_crawlers.base import BaseCrawler


class NovusAgendaCrawler(BaseCrawler):
    DEFAULT_PAGINATION_ELEMENT: str = (
        "#ctl00_ContentPlaceHolder1_lblPageInfo, div.rgInfoPart strong:nth-child(3)"
    )
    DEFAULT_URL_HREF: str = 'a[id*="hypMinutesPDF"]'

    def __init__(
        self,
        url: str,
        commission: str,
        municipality: str,
        state: str,
        document_type: str = "Minutes",
        file_extension: str = "pdf",
        pagination_element: str = DEFAULT_PAGINATION_ELEMENT,
        url_href: str = DEFAULT_URL_HREF,
    ):
        super().__init__(
            url=url,
            commission=commission,
            municipality=municipality,
            state=state,
            document_type=document_type,
            file_extension=file_extension,
        )
        self.pagination_element = pagination_element
        self.url_href = url_href

    async def perform_interactions(self) -> None:
        await self.interactions()

    async def interactions(self) -> None:
        raise NotImplementedError("Subclasses must implement this method")

    async def interactions_template(
        self,
        date_range_id: str,
        calendar_from_id: str,
        calendar_to_id: str,
        meeting_type_id: str,
        search_button_id: str,
        meeting_label: str,
    ) -> None:
        await self.get_page().wait_for_selector(date_range_id, timeout=60000)
        await self.get_page().select_option(date_range_id, "cus")
        await self.get_page().fill(calendar_from_id, "1/1/2021")
        await self.get_page().fill(calendar_to_id, "1/1/2026")
        await self.get_page().select_option(meeting_type_id, label=meeting_label)
        await self.get_page().click(search_button_id)
        await self.get_page().wait_for_timeout(2000)

    async def get_file_urls(self, existing_links: List[str]) -> List[str]:
        file_urls = []
        current_page = 1
        total_pages = await self.get_total_pages()

        while current_page <= total_pages:
            file_urls.extend(await self.extract_file_urls_from_page(existing_links))

            if current_page < total_pages:
                await self.get_page().wait_for_timeout(1000)
                next_page = await self.get_page().query_selector(
                    'a[title="Next Page"], button#ctl00_ContentPlaceHolder1_btnNextMeeting'
                )
                if next_page:
                    await next_page.click()
                    await self.get_page().wait_for_load_state("networkidle")
            current_page += 1

        return file_urls

    async def get_total_pages(self) -> int:
        total_pages_element = await self.get_page().query_selector(
            self.pagination_element
        )
        if total_pages_element:
            total_pages_text = await total_pages_element.inner_text()
            match = re.search(r"Page \d+ of (\d+)", total_pages_text)
            if match:
                return int(match.group(1))
            try:
                return int(total_pages_text)
            except ValueError:
                self.logger.warning(
                    f"Failed to parse total pages from text: {total_pages_text}"
                )
        return 1

    async def extract_file_urls_from_page(self, existing_links: List[str]) -> List[str]:
        file_urls = []
        download_links = await self.get_page().query_selector_all(self.url_href)
        self.logger.debug(f"Found {len(download_links)} download links")

        for link in download_links:
            file_url = await link.get_attribute("href")
            if file_url:
                full_file_url = urljoin(self.url, file_url)
                if full_file_url not in existing_links:
                    file_urls.append(full_file_url)
                    self.logger.debug(f"Found PDF: {full_file_url}")

        return file_urls
