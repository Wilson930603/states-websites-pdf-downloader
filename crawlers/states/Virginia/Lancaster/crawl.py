import os

import asyncio
from crawlers.base_crawlers.base import BaseCrawler
from urllib.parse import urljoin
import httpx


class LancovaCrawler(BaseCrawler):
    base_url = "https://lancova.civicweb.net"

    def __init__(self):
        super().__init__(
            url="https://lancova.civicweb.net/Portal/MeetingInformation.aspx?Id=5189",
            commission="Planning Commission",
            municipality="Lancaster County",
            state="Virginia",
            document_type="Minutes",
            file_extension="pdf",
        )

    # Override download_file to follow_redirect, using `get_redirect` does not seems to work properly here
    async def download_file(self, url: str) -> None:
        filename = self.get_filename()
        save_path = os.path.join(self.download_dir, filename)
        if not os.path.exists(self.download_dir):
            os.makedirs(self.download_dir)
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
            }
            async with httpx.AsyncClient(verify=False, follow_redirects=True) as client:
                response = await client.get(url, headers=headers)
                if response.status_code == 200:
                    with open(save_path, "wb") as f:
                        f.write(response.content)
                else:
                    self.logger.warning(
                        f"Failed to download PDF from {url}, status code: {response.status_code}"
                    )
        except Exception:
            self.logger.exception(f"Failed to download PDF from {url}")

    async def get_file_urls_for_page(self):
        download_urls = []
        links_in_current_page = await self.get_page().query_selector_all(
            "button.meeting-list-item-button:visible"
        )
        # Click on every link, wait for the pdf to appear and get the "minutes link"
        for link in links_in_current_page:
            await link.click()
            await self.get_page().wait_for_timeout(1000)

            minutes_button = await self.get_page().query_selector(
                "button#ctl00_MainContent_MinutesDocument:visible"
            )
            if not minutes_button:
                self.logger.debug("No minutes button found")
                continue
            await minutes_button.click()
            await self.get_page().wait_for_timeout(1000)

            # Download thel inks with the text "minutes" or "minutes packet"
            minutes_link = await self.get_page().query_selector(
                'a:has-text("Minutes"):visible'
            )
            if not minutes_link:
                minutes_link = await self.get_page().query_selector(
                    'a:has-text("Minutes Packet"):visible'
                )

            url = await minutes_link.get_attribute("href")
            full_pdf_url = urljoin(self.base_url, url)
            download_urls.append(full_pdf_url)
            self.logger.debug(f"Download URL found: {full_pdf_url}")
        return download_urls

    async def get_file_urls(self, existing_links):
        download_urls = []

        # Get the links in the first page
        download_urls += await self.get_file_urls_for_page()

        # Get the links in the rest of the pages
        next_page = await self.get_page().query_selector("div.button-next")
        while next_page:
            await next_page.click()
            await self.get_page().wait_for_timeout(2000)
            download_urls += await self.get_file_urls_for_page()
            next_page = await self.get_page().query_selector("div.button-next:visible")

        return download_urls


if __name__ == "__main__":

    async def main():
        crawler = LancovaCrawler()
        await crawler.crawl()

    asyncio.run(main())
