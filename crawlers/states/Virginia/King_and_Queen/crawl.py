import asyncio

from crawlers.base_crawlers.table_base import TableCrawler


class KingAndQueenCountyCrawler(TableCrawler):
    def __init__(self):
        super().__init__(
            url="https://kingandqueenco.net/planning-commission-meetings/",
            commission="Planning Commission",
            municipality="King And Queen County",
            state="Virginia",
            document_type="Minutes",
            file_extension="pdf",
            row_selector="tr",
            url_href='a:has-text("Minutes")',
        )

    async def should_crawl_row(self, row) -> bool:
        date_cell = await row.query_selector("td:nth-child(1)")
        if not date_cell:
            return False
        date = await date_cell.inner_text()
        year = date.split(", ")[-1]
        if int(year) < self.MIN_YEAR:
            return False
        return True


if __name__ == "__main__":

    async def main():
        crawler = KingAndQueenCountyCrawler()
        await crawler.crawl()

    asyncio.run(main())
