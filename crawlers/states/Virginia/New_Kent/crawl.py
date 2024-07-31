import asyncio

from crawlers.base_crawlers.base import BaseCrawler
from urllib.parse import urljoin


class NewKentCountyCrawler(BaseCrawler):
    base_url = "https://www.co.new-kent.va.us/Archive.aspx"

    def __init__(self):
        super().__init__(
            url="https://www.co.new-kent.va.us/Archive.aspx",
            commission="Planning Commission",
            municipality="New Kent County",
            state="Virginia",
            document_type="Minutes",
            file_extension="pdf",
        )

    async def get_file_urls(self, existing_links):
        download_urls = []
        dropdowns = (
            await self.get_page()
            .get_by_label("Planning Commission Minutes 202")
            .filter(has_not_text="2020")
            .all()
        )
        for dropdown in dropdowns:
            new_page = await self.get_browser().new_page()
            dropdown_id = await dropdown.get_attribute("id")
            await new_page.goto(self.url)
            await new_page.select_option(f"#{dropdown_id}", "All Archive Items")
            await new_page.wait_for_selector('a:has-text("Minutes")')
            links = await new_page.query_selector_all('a:has-text("Minutes")')
            for link in links:
                href = await link.get_attribute("href")
                full_url = urljoin(self.base_url, href)
                final_url = await self.get_redirect(full_url)

                download_urls.append(final_url)
                self.logger.debug(f"Found PDF: {final_url}")
            await new_page.close()

        return download_urls


if __name__ == "__main__":

    async def main():
        crawler = NewKentCountyCrawler()
        await crawler.crawl()

    asyncio.run(main())
