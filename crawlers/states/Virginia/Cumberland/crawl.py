import asyncio
from crawlers.base_crawlers.civicengage import CivicEngageCrawler


class CumberlandCrawler(CivicEngageCrawler):
    def __init__(self):
        super().__init__(
            url=(
                "https://www.cumberlandcounty.virginia.gov/AgendaCenter/Search/"
                "?term=&CIDs=4,3,&startDate=01/01/2021&endDate=12/12/2027"
                "&dateRange=&dateSelector="
            ),
            commission="Planning Commision / Board of Zoning",
            municipality="Cumberland County",
            state="Virginia",
            document_type="Minutes",
            url_href='a[aria-label*="Minutes"]:not(a:has-text("Workshop")),'
            'a:has-text("Zoning"), a:has-text("BZA")',
            file_extension="pdf",
        )


if __name__ == "__main__":

    async def main():
        crawler = CumberlandCrawler()
        await crawler.crawl()

    asyncio.run(main())
