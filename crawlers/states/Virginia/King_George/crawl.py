import asyncio

from crawlers.base_crawlers.civicengage import CivicEngageCrawler


class KingGeorgeCountyCrawler(CivicEngageCrawler):
    def __init__(self):
        super().__init__(
            url="https://www.kinggeorgecountyva.gov/AgendaCenter/"
            "Search/?term=&CIDs=3,5,&startDate=01/01/2021&endDate=&dateRange=&dateSelector=",
            commission="Board of Zoning / Planning Commission",
            municipality="King George County",
            state="Virginia",
            document_type="Minutes",
            url_href='td.minutes a[aria-label*="Minutes"]',
        )


if __name__ == "__main__":

    async def main():
        crawler = KingGeorgeCountyCrawler()
        await crawler.crawl()

    asyncio.run(main())
