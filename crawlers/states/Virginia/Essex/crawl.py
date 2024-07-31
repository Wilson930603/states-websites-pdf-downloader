import asyncio

from crawlers.base_crawlers.table_base import TableCrawler


class EssexCrawler(TableCrawler):
    def __init__(self):
        super().__init__(
            url="https://www.essex-virginia.org/meetings/recent?"
            "field_smart_date_value_2=2021-01-01&field_smart_date_end_value_2=2027-12-12&"
            "combine=&department=All&boards-commissions=2282",
            commission="Board of Zoning",
            municipality="Essex",
            state="Virginia",
            document_type="Minutes",
            file_extension="pdf",
            row_selector=".views-row",
            url_href='a[title*="Minutes"]',
        )

    async def should_crawl_row(self, row) -> bool:
        # Already filtered by date in the URL
        return True


if __name__ == "__main__":

    async def main():
        crawler = EssexCrawler()
        await crawler.crawl()

    asyncio.run(main())
