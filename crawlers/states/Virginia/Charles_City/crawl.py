import asyncio

from crawlers.base_crawlers.civicengage import CivicEngageCrawler


class CharlesCityCountyCrawler(CivicEngageCrawler):
    def __init__(self):
        super().__init__(
            url="https://www.charlescityva.us/AgendaCenter/Planning-Commission-2",
            commission="Planning Commission",
            municipality="Charles City County",
            state="Virginia",
            document_type="Minutes",
            url_href='td.minutes a[aria-label*="Minutes"]',
        )


if __name__ == "__main__":

    async def main():
        crawler = CharlesCityCountyCrawler()
        await crawler.crawl()

    asyncio.run(main())
