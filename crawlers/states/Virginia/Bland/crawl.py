import asyncio
import re

from crawlers.base_crawlers.base import BaseCrawler


class BlandCountyCrawler(BaseCrawler):
    def __init__(self):
        super().__init__(
            url="https://www.blandcountyva.gov/page/agendas-and-minutes/",
            commission="Planning Commission",
            municipality="Bland County",
            state="Virginia",
            document_type="Minutes",
            file_extension="pdf",
        )

    async def get_file_urls(self, existing_links):
        download_urls = []

        # Add the current year (2024) page to be processed first
        await self.process_year_page(self.url, download_urls)

        # Select the year links from 2021 onwards
        year_links = await self.get_page().query_selector_all(
            "ul.left-nav li.left-sub-nav a"
        )

        for year_link in year_links:
            year_text = await year_link.inner_text()
            year_match = re.search(r"(\d{4})", year_text)
            if year_match:
                year = int(year_match.group(1))
                if year >= 2021:
                    year_url = await year_link.get_attribute("href")
                    full_year_url = f"https://www.blandcountyva.gov{year_url}"

                    # Process the year page
                    await self.process_year_page(full_year_url, download_urls)

        return download_urls

    async def process_year_page(self, year_url, download_urls):
        # Open the year page
        year_page = await self.get_browser().new_page()
        await year_page.goto(year_url)
        await year_page.wait_for_load_state("networkidle")

        # Get all minutes links by checking inner text "MINUTES"
        minutes_links = await year_page.query_selector_all('td a:text("MINUTES")')

        # Iterate through each link and download the PDF
        for link in minutes_links:
            pdf_url = await link.get_attribute("href")
            if pdf_url:
                full_pdf_url = f"https://www.blandcountyva.gov{pdf_url}"
                download_urls.append(full_pdf_url)
                self.logger.debug(f"Found PDF: {full_pdf_url}")

        # Close the year page
        await year_page.close()


if __name__ == "__main__":

    async def main():
        crawler = BlandCountyCrawler()
        await crawler.crawl()

    asyncio.run(main())
