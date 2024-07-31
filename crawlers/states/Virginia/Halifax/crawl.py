import asyncio

from crawlers.base_crawlers.civicengage import CivicEngageCrawler


class HalifaxCountyCrawler(CivicEngageCrawler):
    def __init__(self):
        super().__init__(
            url="https://www.halifaxcountyva.gov/AgendaCenter/Planning-Commission-4",
            commission="Planning Commission",
            municipality="Halifax County",
            state="Virginia",
            document_type="Minutes",
            url_href='td.minutes a[aria-label*="Minutes"]',
        )


if __name__ == "__main__":

    async def main():
        crawler = HalifaxCountyCrawler()
        await crawler.crawl()

    asyncio.run(main())
