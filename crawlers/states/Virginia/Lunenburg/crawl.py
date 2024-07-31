import asyncio

from crawlers.base_crawlers.table_base import TableCrawler


class LunnenburgCounty(TableCrawler):
    def __init__(self):
        super().__init__(
            url="https://lunenburgva.gov/government/planning_commission/agendas___minutes.php",
            commission="Planning Commission",
            municipality="Lunenburg County",
            state="Virginia",
            document_type="Minutes",
            file_extension="pdf",
            row_selector="tr",
            url_href='a:has-text("Minutes")',
        )

    async def should_crawl_row(self, row) -> bool:
        # They do not have data prior to 2022
        return True


if __name__ == "__main__":

    async def main():
        crawler = LunnenburgCounty()
        await crawler.crawl()

    asyncio.run(main())
