import asyncio

from crawlers.base_crawlers.base import BaseCrawler
from urllib.parse import urljoin


class SouthamptonCountyCrawler(BaseCrawler):
    base_url = "https://www.southamptoncounty.org"

    def __init__(self):
        super().__init__(
            url="https://www.southamptoncounty.org/departments/planning/"
            "archived_planning_commission_minutes.php",
            commission="Planning Commission",
            municipality="Southampton County",
            state="Virginia",
            document_type="Minutes",
            file_extension="pdf",
        )

    async def open_url_in_new_page(self, url, timeout=3000):
        new_page = await self.get_browser().new_page()
        full_url = urljoin(self.base_url, url)
        await new_page.goto(full_url)
        await new_page.wait_for_timeout(timeout)
        return new_page

    async def get_year_links(self):
        year_links = []
        all_year_links = await self.get_page().query_selector_all(
            'a:has-text("PC Minutes")'
        )
        for year_folder in all_year_links:
            year_folder_text = await year_folder.inner_text()
            year = year_folder_text.split(" ")[-1]
            if int(year) < self.MIN_YEAR:
                continue
            year_links.append(year_folder)
        return year_links

    async def get_file_urls(self, existing_links):
        download_urls = []
        year_links = await self.get_year_links()
        for link in year_links:
            href = await link.get_attribute("href")
            new_page = await self.open_url_in_new_page(href)
            meeting_links = await new_page.query_selector_all(
                'a[href*="Minutes"], a[href*="MINUTES"]'
            )

            for link in meeting_links:
                href = await link.get_attribute("href")
                full_url = urljoin(self.base_url, href)
                final_url = await self.get_redirect(full_url)
                download_urls.append(final_url)
                self.logger.debug(f"Found PDF: {final_url}")
            await new_page.close()

        return download_urls


if __name__ == "__main__":

    async def main():
        crawler = SouthamptonCountyCrawler()
        await crawler.crawl()

    asyncio.run(main())
