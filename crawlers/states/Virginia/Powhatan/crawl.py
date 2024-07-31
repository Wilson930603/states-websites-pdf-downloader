import asyncio

from crawlers.base_crawlers.civicengage import CivicEngageCrawler


class PowhatanCountyCrawler(CivicEngageCrawler):
    def __init__(self):
        super().__init__(
            url="https://www.powhatanva.gov/AgendaCenter/Search/"
            "?term=&CIDs=10,7,&startDate=&endDate=&dateRange=&dateSelector=",
            commission="Board of Zoning / Planning Commission",
            municipality="Powhatan County",
            state="Virginia",
            document_type="Minutes",
            url_href='td.minutes a[aria-label*="Minutes"]',
        )


if __name__ == "__main__":

    async def main():
        crawler = PowhatanCountyCrawler()
        await crawler.crawl()

    asyncio.run(main())
