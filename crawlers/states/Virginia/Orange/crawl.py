import asyncio

from crawlers.base_crawlers.base import BaseCrawler
from urllib.parse import urljoin


class OrangeCountyCrawler(BaseCrawler):
    base_url = "https://orangecountyva.gov"

    def __init__(self):
        super().__init__(
            url="https://orangecountyva.gov/Archive.aspx",
            commission="Planning Commission",
            municipality="Orange County",
            state="Virginia",
            document_type="Minutes",
            file_extension="pdf",
        )

    async def get_file_urls(self, existing_links):
        download_urls = []
        # They only have data from 2022 onwards
        dropdowns = (
            await self.get_page()
            .get_by_label("Planning Commission - Action Agendas 202")
            .all()
        )
        for dropdown in dropdowns:
            new_page = await self.get_browser().new_page()
            dropdown_id = await dropdown.get_attribute("id")
            await new_page.goto(self.url)
            await new_page.select_option(f"#{dropdown_id}", "All Archive Items")
            await new_page.wait_for_selector(
                'a:has-text("Planning Commission Action Agenda")'
            )
            links = await new_page.query_selector_all(
                'a:has-text("Planning Commission Action Agenda")'
            )
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
        crawler = OrangeCountyCrawler()
        await crawler.crawl()

    asyncio.run(main())
