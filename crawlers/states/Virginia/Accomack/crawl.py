import asyncio
from datetime import datetime
from crawlers.base_crawlers.table_base import TableCrawler


class AccomackCountyCrawler(TableCrawler):
    def __init__(self):
        super().__init__(
            url="https://www.co.accomack.va.us/government/board-appointed-bodies/"
            "accomack-county-planning-commission/minutes-copy-",
            municipality="Accomack County",
            commission="Planning Commission",
            state="Virginia",
            row_selector="tbody tr",
            url_href='a[href$=".pdf"]',
            document_type="Minutes",
            file_extension="pdf",
        )

    async def should_crawl_row(self, row) -> bool:
        # Retrieve the header element to extract the year
        header_element = await self.get_page().query_selector("thead p u")
        if not header_element:
            return False
        year_text = await header_element.inner_text()
        year = int(
            year_text.strip().split()[-1]
        )  # Extract the year from the header text

        # Retrieve the meeting date from the row
        date_element = await row.query_selector("td")
        date_text = await date_element.inner_text()
        date_str = f"{date_text.strip()} {year}"

        try:
            # Parse the date and check if it's from 2021 onwards
            meeting_date = datetime.strptime(date_str, "%B %d %Y")
            return meeting_date.year >= 2021
        except ValueError:
            self.logger.warning(f"Invalid date format: {date_str}")
            return False


if __name__ == "__main__":

    async def main():
        crawler = AccomackCountyCrawler()
        await crawler.crawl(stealth=True)

    asyncio.run(main())
