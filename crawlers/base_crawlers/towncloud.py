import re
from datetime import datetime

from crawlers.base_crawlers.table_base import TableCrawler


class TownCloudCrawler(TableCrawler):
    def __init__(
        self, url, commission, municipality, state, document_type, file_extension
    ):
        super().__init__(
            url=url,
            commission=commission,
            municipality=municipality,
            state=state,
            document_type=document_type,
            file_extension=file_extension,
            row_selector="tr",
            url_href='td.agenda-downloads a:has-text("Minutes")',
            has_redirect=True,
        )

    async def should_crawl_row(self, row) -> bool:
        date_element = await row.query_selector("td:nth-child(2)")
        date_text = await date_element.evaluate("el => el.innerText")
        cleaned_date_text = self.clean_date_text(date_text)
        return self.is_valid_date(cleaned_date_text)

    def clean_date_text(self, date_text: str) -> str:
        # Remove non-ASCII characters, strip whitespace, and remove time information
        cleaned_text = re.sub(r"[^\x00-\x7F]+", "", date_text).strip()
        cleaned_text = re.sub(r"\s+at\s+\d{1,2}:\d{2}(am|pm)", "", cleaned_text)
        return cleaned_text

    def is_valid_date(self, date_text: str) -> bool:
        try:
            # Attempt to parse the cleaned date text
            date = datetime.strptime(date_text, "%B %d, %Y")
            return date.year >= 2021
        except ValueError:
            self.logger.warning(f"Invalid date format: {date_text}")
            return False
