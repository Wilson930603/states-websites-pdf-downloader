import asyncio

from crawlers.base_crawlers.civicengage import CivicEngageCrawler


class CampbellCountyCrawler(CivicEngageCrawler):
    def __init__(self):
        super().__init__(
            url="https://www.co.campbell.va.us/AgendaCenter/Search/"
            "?term=&CIDs=12,6,&startDate=&endDate=&dateRange=&dateSelector=",
            commission="Planning Commission",
            municipality="Campbell County",
            state="Virginia",
            document_type="Minutes",
            url_href='td.minutes a[aria-label*="Minutes"]',
        )


if __name__ == "__main__":

    async def main():
        crawler = CampbellCountyCrawler()
        await crawler.crawl()

    asyncio.run(main())
