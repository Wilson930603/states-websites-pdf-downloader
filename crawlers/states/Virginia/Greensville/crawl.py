import asyncio

from crawlers.base_crawlers.base import BaseCrawler
from urllib.parse import urljoin


class GreensvilleCountyCrawler(BaseCrawler):
    base_url = "https://www.greensvillecountyva.gov/"

    def __init__(self):
        super().__init__(
            url="https://www.greensvillecountyva.gov/boards___commissions/"
            "board_of_supervisors/agendas___minutes/planning_commission.php#outer-1188",
            commission="Planning Commission",
            municipality="Greensville County",
            state="Virginia",
            document_type="Minutes",
            file_extension="pdf",
        )

    async def get_year_folder_locators(self):
        year_folders = []
        all_year_folders = await self.get_page().query_selector_all(
            'h3.docs-toggle.clearfix:has-text("202")'
        )
        for year_folder in all_year_folders:
            year_folder_text = await year_folder.inner_text()
            year = year_folder_text.split("\n")[0]
            if int(year) < self.MIN_YEAR:
                continue
            year_folders.append(year_folder)
        return year_folders

    async def get_file_urls(self, existing_links):
        download_urls = []

        year_folders = await self.get_year_folder_locators()
        for year_folder in year_folders:
            await year_folder.click()
            await self.get_page().wait_for_timeout(1000)

            # Expand minutes section, taking into account only visible locators (to avoid targeting all)
            minutes_section = await self.get_page().query_selector(
                'h4.docs-toggle.clearfix:has-text("Minutes"):visible'
            )
            await minutes_section.click()
            await self.get_page().wait_for_timeout(1000)

            # Extract all meeting minutes links from the current year
            # taking into account only visible locators (to avoid targeting all)
            meeting_links = await self.get_page().query_selector_all(
                'ul a[href*="Minutes"]:visible'
            )

            for link in meeting_links:
                pdf_url = await link.get_attribute("href")
                if pdf_url:
                    full_pdf_url = urljoin(self.base_url, pdf_url)
                    download_urls.append(full_pdf_url)
                    self.logger.debug(f"Found PDF: {full_pdf_url}")

        return download_urls


if __name__ == "__main__":

    async def main():
        crawler = GreensvilleCountyCrawler()
        await crawler.crawl()

    asyncio.run(main())
