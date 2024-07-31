import asyncio
from crawlers.base_crawlers.base import BaseCrawler
from urllib.parse import urljoin


class GloucesterCrawler(BaseCrawler):
    base_url = "https://pub-gloucesterva.escribemeetings.com"
    YEARS_TO_CRAWL = ["2021", "2022", "2023", "2024"]

    def __init__(self):
        super().__init__(
            url="https://pub-gloucesterva.escribemeetings.com/?Year=2024&Expanded=Planning%20Commission",
            commission="County Commission",
            municipality="Gloucester County",
            state="Georgia",
            document_type="Agenda Packet",
            file_extension="pdf",
        )

    async def open_url_in_new_page(self, url, timeout=3000):
        new_page = await self.get_browser().new_page()
        full_url = urljoin(self.base_url, url)
        await new_page.goto(full_url)
        await new_page.wait_for_timeout(timeout)
        return new_page

    async def get_file_urls(self, existing_links):
        download_urls = []

        year_links = [
            f"https://pub-gloucesterva.escribemeetings.com/?Year={year}&Expanded=Planning%20Commission"
            for year in self.YEARS_TO_CRAWL
        ]

        for year_link in year_links:
            new_page = await self.open_url_in_new_page(year_link)

            meeting_links = await new_page.query_selector_all(
                "a[aria-label*='PDF Agenda for Planning Commission']"
            )

            for link in meeting_links:
                url = await link.get_attribute("href")
                download_url = urljoin(self.base_url, url)
                download_urls.append(download_url)
                self.logger.debug(f"Download URL found: {download_url}")

            await new_page.close()

        return download_urls


if __name__ == "__main__":

    async def main():
        crawler = GloucesterCrawler()
        await crawler.crawl()

    asyncio.run(main())
