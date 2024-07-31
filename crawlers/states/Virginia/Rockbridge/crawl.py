import asyncio

from crawlers.base_crawlers.civicengage import CivicEngageCrawler


class RockbridgeCountyCrawler(CivicEngageCrawler):
    def __init__(self):
        super().__init__(
            url="https://www.co.rockbridge.va.us/AgendaCenter/Search/"
            "?term=&CIDs=3,6,&startDate=&endDate=&dateRange=&dateSelector=",
            commission="Board of Zoning / Planning Commission",
            municipality="Rockbridge County",
            state="Virginia",
            document_type="Minutes",
            url_href='td.minutes a[aria-label*="Minutes"]',
        )


if __name__ == "__main__":

    async def main():
        crawler = RockbridgeCountyCrawler()
        await crawler.crawl()

    asyncio.run(main())
