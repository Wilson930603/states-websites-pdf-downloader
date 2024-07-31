import asyncio
import re

from crawlers.base_crawlers.table_base import TableCrawler


class SmythCountyCrawler(TableCrawler):
    def __init__(self):
        super().__init__(
            url="https://www.smythcounty.org/government/agendas___minutes_/"
            "planning_commission_agendas___minutes.php",
            commission="Planning Commission",
            municipality="Smyth County",
            state="Virginia",
            document_type="Minutes",
            file_extension="pdf",
            row_selector="tr",
            has_redirect=True,
            url_href='a:has-text("Minutes")',
        )

    async def should_crawl_row(self, row) -> bool:
        date_cell = await row.query_selector("td:nth-child(1)")
        if not date_cell:
            return False
        full_date_text = await date_cell.inner_text()

        date_match = re.search(r"\d{2}/\d{2}/\d{2}", full_date_text)
        if not date_match:
            return False
        date_only = date_match.group()
        year = date_only.split("/")[-1]
        full_year = "20" + year
        if int(full_year) < self.MIN_YEAR:
            return False
        return True

    async def get_redirect(self, url):
        url = url.replace(
            "https://www.smythcounty.org/government/agendas___minutes_/",
            "https://cms2.revize.com/revize/smythcountyva/",
        )
        return url


if __name__ == "__main__":

    async def main():
        crawler = SmythCountyCrawler()
        await crawler.crawl()

    asyncio.run(main())
