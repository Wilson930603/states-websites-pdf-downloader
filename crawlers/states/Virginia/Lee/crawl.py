import asyncio

from crawlers.base_crawlers.base import BaseCrawler
from urllib.parse import urljoin


class LeeCountyCrawler(BaseCrawler):
    base_url = "http://www.leecova.org"

    def __init__(self):
        super().__init__(
            url="http://www.leecova.org/AgendaandMinutes.htm",
            commission="Boards of Supervisors",
            municipality="Lee County",
            state="Virginia",
            document_type="Minutes",
            file_extension="pdf",
        )

    async def get_file_urls(self, existing_links):
        download_urls = []
        links = await self.get_page().query_selector_all('a[href*="Minutes"]')
        for link in links:
            href = await link.get_attribute("href")
            year = href.split("/")[1]
            if int(year) < self.MIN_YEAR:
                continue
            full_url = urljoin(self.base_url, href)
            download_urls.append(full_url)
            self.logger.debug(f"Found PDF: {full_url}")
        return download_urls


if __name__ == "__main__":

    async def main():
        crawler = LeeCountyCrawler()
        await crawler.crawl()

    asyncio.run(main())
