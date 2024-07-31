import asyncio

from crawlers.base_crawlers.civicengage import CivicEngageCrawler


class MecklenburgCountyCrawler(CivicEngageCrawler):
    def __init__(self):
        super().__init__(
            url="https://www.mecklenburgva.com/AgendaCenter/Search/?"
            "term=&CIDs=5,8,&startDate=&endDate=&dateRange=&dateSelector=",
            commission="Board of Zoning / Planning Commission",
            municipality="Mecklenburg County",
            state="Virginia",
            document_type="Minutes",
            url_href='td.minutes a[aria-label*="Minutes"]',
        )


if __name__ == "__main__":

    async def main():
        crawler = MecklenburgCountyCrawler()
        await crawler.crawl()

    asyncio.run(main())
