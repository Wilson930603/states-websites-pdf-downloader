import asyncio

from crawlers.base_crawlers.civicengage import CivicEngageCrawler


class YorkCountyCrawler(CivicEngageCrawler):
    def __init__(self):
        super().__init__(
            url="https://www.yorkcounty.gov/AgendaCenter/Planning-Commission-3",
            commission="Planning Commission",
            municipality="York County",
            state="Virginia",
            document_type="Minutes",
            url_href='td a[aria-label*="Minutes"]',
        )


if __name__ == "__main__":

    async def main():
        crawler = YorkCountyCrawler()
        await crawler.crawl()

    asyncio.run(main())
