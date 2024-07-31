import asyncio

from crawlers.base_crawlers.civicengage import CivicEngageCrawler


class RockhinghamCountyCrawler(CivicEngageCrawler):
    def __init__(self):
        super().__init__(
            url="https://www.rockinghamcountyva.gov/AgendaCenter/Search/"
            "?term=&CIDs=15,2,&startDate=&endDate=&dateRange=&dateSelector=",
            commission="Board of Zoning / Planning Commission",
            municipality="Rockingham County",
            state="Virginia",
            document_type="Agenda Packet",
            url_href='td a[aria-label*="meeting"]',
        )


if __name__ == "__main__":

    async def main():
        crawler = RockhinghamCountyCrawler()
        await crawler.crawl()

    asyncio.run(main())
