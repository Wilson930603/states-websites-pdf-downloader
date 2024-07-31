import asyncio
import re

from crawlers.base_crawlers.table_base import TableCrawler


class CharlotteCountyCrawler(TableCrawler):
    def __init__(self):
        super().__init__(
            url="https://www.charlottecountyva.gov/departments/planning___zoning/agendas___minutes.php",
            commission="Planning & Zoning",
            municipality="Charlotte County",
            state="Virginia",
            document_type="Minutes",
            file_extension="pdf",
            row_selector="div.table-responsive table tbody tr",
            url_href='a:has-text("Minutes")',
            base_url="https://cms8.revize.com/revize/charlottecountyva/",
        )

    async def should_crawl_row(self, row) -> bool:
        date_element = await row.query_selector("td:nth-child(1)")
        date_text = await date_element.evaluate("el => el.innerText")
        cleaned_date_text = self.clean_date_text(date_text)
        return self.is_valid_date(cleaned_date_text) and "Regular Meeting" in date_text

    def clean_date_text(self, date_text: str) -> str:
        # Extract date part from the text using regex
        match = re.search(r"\d{2}/\d{2}/\d{2}", date_text)
        if match:
            return match.group(0)
        return ""

    def is_valid_date(self, date_text: str) -> bool:
        try:
            if date_text:
                date_parts = date_text.split("/")
                if len(date_parts) == 3:
                    year = (
                        int(date_parts[2]) + 2000
                    )  # Convert two-digit year to four-digit year
                    return year >= 2021
            return False
        except ValueError:
            self.logger.warning(f"Invalid date format: {date_text}")
            return False


if __name__ == "__main__":

    async def main():
        crawler = CharlotteCountyCrawler()
        await crawler.crawl()

    asyncio.run(main())