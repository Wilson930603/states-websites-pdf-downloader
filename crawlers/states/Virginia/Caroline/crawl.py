import asyncio

from crawlers.base_crawlers.civicengage import CivicEngageCrawler


class CarolineCountyCrawler(CivicEngageCrawler):
    def __init__(self):
        super().__init__(
            url="https://co.caroline.va.us/AgendaCenter/Planning-Commission-3",
            commission="Planning Commission",
            municipality="Caroline County",
            state="Virginia",
            document_type="Minutes",
            url_href='td.minutes a[aria-label*="Minutes"]',
        )


if __name__ == "__main__":

    async def main():
        crawler = CarolineCountyCrawler()
        await crawler.crawl()

    asyncio.run(main())
