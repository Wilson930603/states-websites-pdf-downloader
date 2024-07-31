import asyncio

from crawlers.base_crawlers.table_base import TableCrawler


class TazewellCountyCrawler(TableCrawler):
    def __init__(self):
        super().__init__(
            url="https://tazewellcountyva.org/government/boards-and-commissions/planning-commission/",
            commission="Planning Commission",
            municipality="Tazewell County",
            state="Virginia",
            document_type="Minutes",
            file_extension="pdf",
            row_selector="ul li",
            url_href='a:has-text("Minutes")',
        )

    async def should_crawl_row(self, row) -> bool:
        # Latest year they have info is 2022
        return True


if __name__ == "__main__":

    async def main():
        crawler = TazewellCountyCrawler()
        await crawler.crawl()

    asyncio.run(main())
