import asyncio

from crawlers.base_crawlers.civicengage import CivicEngageCrawler


class PageCountyCrawler(CivicEngageCrawler):
    def __init__(self):
        super().__init__(
            url="https://www.pagecounty.virginia.gov/AgendaCenter/Search/"
            "?term=&CIDs=7,5,&startDate=&endDate=&dateRange=&dateSelector=",
            commission="Board of Zoning / Planning Commission",
            municipality="Page County",
            state="Virginia",
            document_type="Minutes",
            url_href='td.minutes a[aria-label*="Minutes"]',
        )


if __name__ == "__main__":

    async def main():
        crawler = PageCountyCrawler()
        await crawler.crawl()

    asyncio.run(main())
