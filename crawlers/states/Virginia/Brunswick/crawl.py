import asyncio
import re

from crawlers.base_crawlers.base import BaseCrawler


class BrunswickCountyCrawler(BaseCrawler):
    def __init__(self):
        super().__init__(
            url="https://www.brunswickco.com/cms/One.aspx?pageId=11500977&portalId=10858880",
            commission="Planning Commission",
            municipality="Brunswick County",
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
            match = re.search(r"Click here to navigate folder\s*'(\d{4})'", year_title)
            if match:
                year = int(match.group(1))
                if year >= 2021:
                    # Open a new page for the year folder
                    new_page = await self.get_browser().new_page()
                    await new_page.goto(self.url)
                    await new_page.wait_for_load_state("networkidle")

                    # Find the specific year folder on the new page and click it
                    specific_year_folder = await new_page.query_selector(
                        f"a.documentDetailsToggle.content_folder.dataRowItem"
                        f"[title=\"Click here to navigate folder  '{year}'\"]"
                    )
                    if specific_year_folder:
                        await specific_year_folder.click()
                        await new_page.wait_for_load_state("networkidle")
                        await new_page.wait_for_timeout(
                            2000
                        )  # Wait for content to load

                        # Get all meeting minutes links
                        meeting_links = await new_page.query_selector_all(
                            "a.item.docItemTitle.downloaditem"
                        )

                        # Iterate through each link and download the PDF
                        for link in meeting_links:
                            pdf_url = await link.get_attribute("href")
                            if pdf_url:
                                download_urls.append(pdf_url)
                                self.logger.debug(f"Found PDF: {pdf_url}")

                    # Close the new page
                    await new_page.close()
                else:
                    self.logger.debug(f"Skipping folder for year {year}")

        return download_urls


if __name__ == "__main__":

    async def main():
        crawler = BrunswickCountyCrawler()
        await crawler.crawl()

    asyncio.run(main())
