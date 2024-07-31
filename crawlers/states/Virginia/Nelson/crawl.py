import asyncio
from crawlers.base_crawlers.base import BaseCrawler
from urllib.parse import urljoin


class NelsonCountyCrawler(BaseCrawler):
    base_url = "https://www.nelsoncounty-va.gov/"

    def __init__(self):
        super().__init__(
            url="https://www.nelsoncounty-va.gov/departments-offices/planning-zoning/planning-commission/",
            commission="Planning Commission",
            municipality="Nelson County",
            state="Virginia",
            document_type="Minutes",
            file_extension="pdf",
        )

    async def get_file_urls(self, existing_links):
        download_urls = []
        # Select all minutes link + 2021 and 2022, whose href changes
        links = await self.get_page().query_selector_all(
            "a[href$='.pdf'][href*='Minutes'], a:not([href*='Minutes'])[href*='2022'], "
            "a:not([href*='Minutes'])[href*='2021']"
        )

        for link in links:
            href = await link.get_attribute("href")
            full_pdf_url = urljoin(self.base_url, href)
            download_urls.append(full_pdf_url)
            self.logger.debug(f"Found PDF: {full_pdf_url}")

        return download_urls


if __name__ == "__main__":

    async def main():
        crawler = NelsonCountyCrawler()
        await crawler.crawl()

    asyncio.run(main())
