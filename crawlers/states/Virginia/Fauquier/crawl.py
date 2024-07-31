import asyncio

from crawlers.base_crawlers.granicus import GranicusCrawler


class FauquierCrawler(GranicusCrawler):
    def __init__(self):
        super().__init__(
            url="https://fauquier-va.granicus.com/ViewPublisher.php?view_id=6",
            commission="Planning Commission",
            municipality="Fauquier",
            state="Virginia",
            base_url="https://fauquier-va.granicus.com",
            has_redirect=True,
            row_filter_keyword="Planning Commission",
            row_selector="tr.listingRow",
            date_column_header='td[headers*="Date Planning-Commission"]',
            date_format="%b %d, %Y",
            url_href='a:has-text("Minutes")',
        )

    async def perform_interactions(self) -> None:
        await self.get_page().click(".CollapsiblePanelTab")
        await self.get_page().wait_for_selector("tr.listingRow", timeout=6000)


if __name__ == "__main__":

    async def main():
        crawler = FauquierCrawler()
        await crawler.crawl()

    asyncio.run(main())
