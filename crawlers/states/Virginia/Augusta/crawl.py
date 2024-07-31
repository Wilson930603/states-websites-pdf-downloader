import asyncio

from crawlers.base_crawlers.granicus import GranicusCrawler


class AugustaCountyCrawler(GranicusCrawler):
    def __init__(self):
        super().__init__(
            url="https://augustava.granicus.com/ViewPublisher.php?view_id=1",
            commission="Planning Commission",
            municipality="Augusta County",
            state="Virginia",
            base_url="https://augustava.granicus.com/ViewPublisher.php?view_id=1",
            row_filter_keyword="Planning Commission",
            row_selector="tr.listingRow",
            date_column_header='td[headers*="Date"]',
            url_href='a[href*="minutes"]',
            has_redirect=True,
        )


if __name__ == "__main__":

    async def main():
        crawler = AugustaCountyCrawler()
        await crawler.crawl()

    asyncio.run(main())
