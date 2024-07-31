import asyncio
import re

from crawlers.base_crawlers.base import BaseCrawler


class BathCountyCrawler(BaseCrawler):
    def __init__(self):
        super().__init__(
            url="https://www.bathcountyva.gov/cms/One.aspx?pageId=11781522&portalId=11366390",
            commission="Planning Commission",
            municipality="Bath County",
            state="Virginia",
            document_type="Minutes",
            file_extension="pdf",
        )

    async def get_file_urls(self, existing_links):
        download_urls = []

        # wait 2 seconds for the page to load
        await self.get_page().wait_for_timeout(2000)
        # Find all year folders from 2021 onwards
        year_folders = await self.get_page().query_selector_all(
            'a.documentDetailsToggle.content_folder.dataRowItem[title^="Click here to navigate folder"]'
        )
        for year_folder in year_folders:
            year_title = await year_folder.get_attribute("title")
            match = re.search(r"(\d{4}) Meeting Minutes", year_title)
            if match:
                year = int(match.group(1))
                if year >= 2021:
                    # Click the year folder to navigate into it
                    await year_folder.click()
                    await self.get_page().wait_for_load_state("networkidle")
                    await self.get_page().wait_for_timeout(
                        2000
                    )  # Wait for content to load

                    # Get all meeting minutes links
                    meeting_links = await self.get_page().query_selector_all(
                        "a.item.docItemTitle.downloaditem"
                    )

                    # Iterate through each link and download the PDF
                    for link in meeting_links:
                        pdf_url = await link.get_attribute("href")
                        if pdf_url:
                            full_pdf_url = f"https://www.bathcountyva.gov/{pdf_url}"
                            download_urls.append(full_pdf_url)
                            self.logger.debug(f"Found PDF: {full_pdf_url}")

                    # Navigate back to the parent directory
                    await self.get_page().go_back()
                    await self.get_page().wait_for_load_state("networkidle")
                    await self.get_page().wait_for_timeout(
                        2000
                    )  # Wait for content to load
                else:
                    self.logger.debug(f"Skipping folder for year {year}")

        return download_urls


if __name__ == "__main__":

    async def main():
        crawler = BathCountyCrawler()
        await crawler.crawl(stealth=True)

    asyncio.run(main())
