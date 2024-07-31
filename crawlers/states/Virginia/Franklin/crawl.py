import asyncio
from crawlers.base_crawlers.civicengage import CivicEngageCrawler


class FranklinCrawler(CivicEngageCrawler):
    def __init__(self):
        super().__init__(
            url=(
                "https://www.franklincountyva.gov/AgendaCenter/Search/"
                "?term=&CIDs=3,4,&startDate=01/01/2021&endDate=12/31/2027&dateRange=&dateSelector="
            ),
            commission="Planning Commision / Board of Zoning",
            municipality="Franklin County",
            state="Virgina",
            document_type="Minutes",
            url_href='a[aria-label*="Minutes"]:not(a:has-text("Workshop")), '
            'a:has-text("Zoning"):not(a:has-text("Hearing"))',
            file_extension="pdf",
        )


if __name__ == "__main__":

    async def main():
        crawler = FranklinCrawler()
        await crawler.crawl()

    asyncio.run(main())
