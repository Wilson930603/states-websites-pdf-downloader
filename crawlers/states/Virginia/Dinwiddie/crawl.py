import asyncio
from crawlers.base_crawlers.civicengage import CivicEngageCrawler


class DinwiddieCrawler(CivicEngageCrawler):
    def __init__(self):
        super().__init__(
            url=(
                "https://www.dinwiddieva.us/AgendaCenter/Search/?term=&CIDs=3,1"
                "&startDate=01/01/2021&endDate=12/12/2027&dateRange=&dateSelector="
            ),
            commission="Planning Commision / Board of Zoning",
            municipality="Dinwiddie County",
            state="Virgina",
            document_type="Minutes",
            url_href='a[aria-label*="Minutes"]:not(a:has-text("Workshop")), a:has-text("Zoning")',
            file_extension="pdf",
        )


if __name__ == "__main__":

    async def main():
        crawler = DinwiddieCrawler()
        await crawler.crawl()

    asyncio.run(main())
