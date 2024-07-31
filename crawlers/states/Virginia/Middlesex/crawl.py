import asyncio

from crawlers.base_crawlers.civicengage import CivicEngageCrawler


class MiddleSexCountyCrawler(CivicEngageCrawler):
    def __init__(self):
        super().__init__(
            url="https://www.co.middlesex.va.us/AgendaCenter/Search/?"
            "term=&CIDs=8,2,&startDate=&endDate=&dateRange=&dateSelector=",
            commission="Board of Zoning / Planning Commission",
            municipality="Middlesex County",
            state="Virginia",
            document_type="Minutes",
            url_href='td.minutes a[aria-label*="Minutes"]',
        )


if __name__ == "__main__":

    async def main():
        crawler = MiddleSexCountyCrawler()
        await crawler.crawl()

    asyncio.run(main())
