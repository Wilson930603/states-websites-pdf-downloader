import asyncio

from crawlers.base_crawlers.civicengage import CivicEngageCrawler


class HenryCountyCrawler(CivicEngageCrawler):
    def __init__(self):
        super().__init__(
            url="https://www.henrycountyva.gov/AgendaCenter/"
            "Search/?term=&CIDs=9,8,&startDate=&endDate=&dateRange=&dateSelector=",
            commission="Board of Zoning / Planning Commission",
            municipality="Henry County",
            state="Virginia",
            document_type="Minutes",
            url_href='td.minutes a[aria-label*="Minutes"]',
        )


if __name__ == "__main__":

    async def main():
        crawler = HenryCountyCrawler()
        await crawler.crawl()

    asyncio.run(main())
