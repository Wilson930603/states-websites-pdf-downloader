import asyncio
from datetime import datetime

from crawlers.base_crawlers.table_base import TableCrawler


class AmeliaCountyCrawler(TableCrawler):
    def __init__(self):
        super().__init__(
            url="https://ameliacova.com/departments/boards_and_commissions/"
            "planning_commission.php#outer-116sub-117",
            municipality="Amelia County",
            commission="Planning Commission",
            state="Virginia",
            row_selector="ul.file-group.sub-117 li",
            url_href='a[href$=".pdf"]',
            document_type="Agenda Packet",
            file_extension="pdf",
            has_redirect=True,
        )

    async def should_crawl_row(self, row) -> bool:
        link_text = await row.inner_text()
        if "PC Packet" in link_text:
            try:
                # Extract and parse the date from the link text
                date_text = link_text.split("PC Packet")[0].strip()
                meeting_date = datetime.strptime(date_text, "%B %d, %Y")
                return meeting_date.year >= 2021
            except (ValueError, IndexError):
                self.logger.warning(f"Invalid date format in row: {link_text}")
                return False
        return False

    async def get_redirect(self, url):
        url = url.replace(
            "https://ameliacova.com/departments/boards_and_commissions/",
            "https://cms2.revize.com/revize/ameliacountyva/",
        )
        return url


if __name__ == "__main__":

    async def main():
        crawler = AmeliaCountyCrawler()
        await crawler.crawl()

    asyncio.run(main())
