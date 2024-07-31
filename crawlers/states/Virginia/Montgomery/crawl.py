import os
import asyncio
from urllib.parse import urljoin

from crawlers.base_crawlers.base import BaseCrawler


class MontgomeryCountyCrawler(BaseCrawler):
    base_url = "https://weblink.montva.com/WebLink/"

    def __init__(self):
        super().__init__(
            url="https://montva.com/1/government/meeting-agendas-minutes",
            commission="Planning Commission",
            municipality="Montgomery County",
            state="Virginia",
            document_type="Minutes",
            file_extension="pdf",
        )

    async def download_file(self, url: str, download_without_link=False) -> None:
        if not download_without_link:
            await super().download_file(url)
            return
        new_page = await self.open_url_in_new_page(url)

        filename = self.get_filename()
        save_path = os.path.join(self.download_dir, filename)
        if not os.path.exists(self.download_dir):
            os.makedirs(self.download_dir)
        try:
            await new_page.wait_for_timeout(12000)  # Takes a lot to load
            download_button = await new_page.query_selector("button#STR_DOWNLOAD")
            if download_button:
                async with new_page.expect_download() as download_info:
                    await download_button.click()
                    download = await download_info.value
            await download.save_as(save_path)
            self.logger.info(
                f"Downloaded PDF from {url} by clicking on the download button"
            )
        except Exception:
            self.logger.exception(f"Failed to download PDF from {url}")

        await new_page.close()

    async def open_url_in_new_page(self, url, timeout=3000):
        full_url = urljoin(self.base_url, url)
        new_page = await self.get_browser().new_page()
        await new_page.goto(full_url)
        await new_page.wait_for_timeout(timeout)
        return new_page

    async def download_viewer_files_for_previous_years(self, url):
        # Define the URLs to scrape for each year
        year_urls = {
            2023: "Browse.aspx?id=940&dbid=4&repo=PIO",
            2022: "Browse.aspx?id=1085&dbid=4&repo=PIO",
            2021: "Browse.aspx?id=1087&dbid=4&repo=PIO",
        }

        for year, year_url in year_urls.items():
            # Open the year's minutes folder in a new page and get its meeting links
            year_page = await self.open_url_in_new_page(year_url)
            await year_page.wait_for_load_state("networkidle")
            await year_page.wait_for_timeout(2000)
            meeting_links = await year_page.query_selector_all(
                'a[href*="/WebLink/DocView.aspx"]'
            )

            # Iterate through each link and click on the Download button as there is no direct link to the PDF
            for link in meeting_links:
                href = await link.get_attribute("href")
                await self.download_file(href, download_without_link=True)

            await year_page.close()

    async def get_download_urls_for_2024_onwards(self, existing_links):
        url_for_2024 = "https://go.boarddocs.com/va/montva/Board.nsf/Public"
        await self.get_page().goto(url_for_2024)
        await self.get_page().wait_for_load_state("networkidle")

        base_url_for_2024 = "https://go.boarddocs.com"
        download_urls = []
        await self.get_page().click(".featured-container > .committeename")
        await self.get_page().click("#ui-id-17")
        await self.get_page().wait_for_timeout(2000)
        meeting_links = await self.get_page().query_selector_all("#ui-id-18 > a")
        for link in meeting_links:
            await link.click()
            await self.get_page().wait_for_timeout(1000)
            await self.get_page().click("#btn-view-agenda")

            meeting_minutes_section = await self.get_page().query_selector(
                'span.title:has-text("Minutes")'
            )
            if meeting_minutes_section:
                await meeting_minutes_section.click()
                await self.get_page().wait_for_timeout(6000)
                links = await self.get_page().query_selector_all(
                    'a.public-file:has-text("Minutes")'
                )
                for link in links:
                    href = await link.get_attribute("href")
                    full_url = urljoin(base_url_for_2024, href)
                    download_urls.append(full_url)
                    self.logger.debug(f"Found download URL: {full_url}")
            await self.get_page().click("#mainMeetings")  # Go back too metings section
        return download_urls

    async def get_file_urls(self, existing_links):
        download_urls = []
        # For 2023 - 2021, this page has a viewer without direct links to the PDFs,
        # so we have to click on every download button
        await self.download_viewer_files_for_previous_years(self.url)

        # For 2024 onwards, we can get the download links directly as usual
        download_urls = await self.get_download_urls_for_2024_onwards(self)

        return download_urls


if __name__ == "__main__":

    async def main():
        crawler = MontgomeryCountyCrawler()
        await crawler.crawl()

    asyncio.run(main())
