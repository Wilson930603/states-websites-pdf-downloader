import asyncio
from typing import List
from urllib.parse import urljoin
from crawlers.base_crawlers.base import BaseCrawler


class ClarkeCountyCrawler(BaseCrawler):
    def __init__(self):
        super().__init__(
            url="https://www.clarkecounty.gov/government/boards-commissions/"
            "planning-commission/pc-minutes/-folder-1032",
            municipality="Clarke County",
            commission="Planning Commission",
            state="Virginia",
            document_type="Minutes",
            file_extension="pdf",
        )

    async def get_file_urls(self, existing_links: List[str]) -> List[str]:
        download_urls = []

        # Open the landing page
        await self.get_page().wait_for_timeout(
            2000
        )  # Wait for the page to load completely

        # Get year links starting from 2021
        year_links = await self.get_page().query_selector_all("ul li a")
        for year_link in year_links:
            year_title = await year_link.get_attribute("title")
            if not year_title:
                continue
            if year_title.isdigit() and int(year_title) >= 2021:
                year_href = await year_link.get_attribute("href")
                year_url = urljoin(self.url, year_href)
                year_page = await self.get_browser().new_page()
                await year_page.goto(year_url)
                await year_page.wait_for_load_state("networkidle")

                # Get all regular meeting minutes links within the year page
                meeting_links = await year_page.query_selector_all(
                    'ul li a[href*=".pdf"]'
                )
                for meeting_link in meeting_links:
                    inner_text = await meeting_link.inner_text()
                    if "Business Meeting Minutes" in inner_text:
                        pdf_url = await meeting_link.get_attribute("href")
                        if pdf_url:
                            full_pdf_url = urljoin(year_url, pdf_url)
                            if full_pdf_url not in existing_links:
                                download_urls.append(full_pdf_url)
                                self.logger.debug(f"Found PDF: {full_pdf_url}")

                await year_page.close()

        return download_urls


if __name__ == "__main__":

    async def main():
        crawler = ClarkeCountyCrawler()
        await crawler.crawl(stealth=True)

    asyncio.run(main())
