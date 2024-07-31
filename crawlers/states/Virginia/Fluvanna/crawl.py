import asyncio

from crawlers.base_crawlers.table_base import TableCrawler


class FluvannaCrawler(TableCrawler):
    def __init__(self):
        super().__init__(
            url="https://www.fluvannacounty.org/meetings?date_filter%5Bvalue%5D%5Bmonth%5D=1"
            "&date_filter%5Bvalue%5D%5Bday%5D=1&date_filter%5Bvalue%5D%5Byear%5D=2021&"
            "date_filter_1%5Bvalue%5D%5Bmonth%5D=12&date_filter_1%5Bvalue%5D%5Bday%5D=31"
            "&date_filter_1%5Bvalue%5D%5Byear%5D=2027&field_microsite_tid=All&field_microsite_tid_1=28",
            commission="Planning Commission",
            municipality="Fluvanna County",
            state="Virginia",
            document_type="Minutes",
            file_extension="pdf",
            row_selector="tr",
            url_href='a:has-text("Minutes")',
        )

    async def should_crawl_row(self, row) -> bool:
        # Already filtered by date in the URL
        return True


if __name__ == "__main__":

    async def main():
        crawler = FluvannaCrawler()
        await crawler.crawl()

    asyncio.run(main())
