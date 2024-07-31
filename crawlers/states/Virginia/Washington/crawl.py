import asyncio

from crawlers.base_crawlers.table_base import TableCrawler


class WashingtonCountyCrawler(TableCrawler):
    def __init__(self):
        super().__init__(
            url="https://washingtoncountyva.iqm2.com/Citizens/Calendar.aspx?"
            "From=1%2f1%2f2021&To=12%2f31%2f9999",
            commission="Planning Commission",
            municipality="Washington County",
            state="Virginia",
            document_type="Minutes",
            file_extension="pdf",
            row_selector=".MeetingRow",
            url_href='a:has-text("Minutes")',
        )

    async def perform_interactions(self) -> None:
        await self.get_page().click("#ContentPlaceholder1_DepartmentID")
        await self.get_page().select_option(
            "#ContentPlaceholder1_DepartmentID", "Planning Commission"
        )
        await self.get_page().wait_for_selector(
            "#ContentPlaceholder1_pnlMeetings", timeout=6000
        )

    async def should_crawl_row(self, row) -> bool:
        # Already filtered by date in the URL
        return True


if __name__ == "__main__":

    async def main():
        crawler = WashingtonCountyCrawler()
        await crawler.crawl()

    asyncio.run(main())
