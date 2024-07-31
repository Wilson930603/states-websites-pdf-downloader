import asyncio
import os
import re
from datetime import datetime
from urllib.parse import unquote

from crawlers.base_crawlers.table_base import TableCrawler


class ArlingtonCountyCrawler(TableCrawler):
    def __init__(self):
        super().__init__(
            url="https://arlington.granicus.com/ViewPublisher.php?view_id=44",
            municipality="Arlington County",
            commission="Planning Commission",
            state="Virginia",
            row_selector="table#archive tbody tr",
            url_href="a",
            document_type="Minutes",
            file_extension="pdf",
            has_redirect=True,
        )

    async def download_file(self, url: str) -> None:
        filename = self.get_filename()
        save_path = os.path.join(self.download_dir, filename)
        if not os.path.exists(self.download_dir):
            os.makedirs(self.download_dir)
        try:
            new_page = await self.get_browser().new_page()
            await new_page.goto(url)
            await new_page.wait_for_load_state("networkidle")
            await new_page.pdf(path=save_path)
            self.logger.info(f"Saved PDF from {url} to {save_path}")
            await new_page.close()
        except Exception:
            self.logger.exception(f"Failed to download PDF from {url}")

    async def should_crawl_row(self, row) -> bool:
        date_element = await row.query_selector('td[headers^="Date"]')
        if date_element:
            date_text = await date_element.inner_text()
            # Use regex to extract the visible date part
            match = re.search(r"[a-zA-Z]+\s+\d{1,2},\s+\d{4}", date_text)
            if match:
                visible_date_text = match.group()
                try:
                    meeting_date = datetime.strptime(visible_date_text, "%b %d, %Y")
                    return meeting_date.year >= 2021
                except ValueError:
                    self.logger.warning(f"Invalid date format: {visible_date_text}")
                    return False
            else:
                self.logger.warning(f"Date extraction failed: {date_text}")
                return False
        return False

    async def get_redirected_url(self, url: str) -> str:
        try:
            redirected_url = await self.get_redirect(url)
            if redirected_url:
                doc_url_encoded = redirected_url.split("url=")[-1].split("&")[0]
                doc_url = unquote(doc_url_encoded)
                return doc_url
            else:
                self.logger.warning(f"Failed to get redirected URL for {url}")
        except Exception:
            self.logger.exception(
                f"Error encountered while getting redirected URL for {url}"
            )
        return url


if __name__ == "__main__":

    async def main():
        crawler = ArlingtonCountyCrawler()
        await crawler.crawl()

    asyncio.run(main())
