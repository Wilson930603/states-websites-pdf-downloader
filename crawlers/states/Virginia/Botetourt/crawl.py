import asyncio

from crawlers.base_crawlers.civicengage import CivicEngageCrawler


class BotetourtCountyCrawler(CivicEngageCrawler):
    def __init__(self):
        super().__init__(
            url="https://www.botetourtva.gov/AgendaCenter/Planning-Commission-6",
            commission="Planning Commission",
            municipality="Botetourt County",
            state="Virginia",
            document_type="Minutes",
            url_href='td.minutes a[aria-label*="Minutes"]',
        )


if __name__ == "__main__":

    async def main():
        crawler = BotetourtCountyCrawler()
        await crawler.crawl()

    asyncio.run(main())
