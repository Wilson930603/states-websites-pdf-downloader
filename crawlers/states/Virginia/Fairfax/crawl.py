import asyncio
from crawlers.base_crawlers.base import BaseCrawler
from urllib.parse import urljoin


class FairfaxCrawler(BaseCrawler):
    base_url = "https://www.fairfaxcounty.gov/"

    def __init__(self):
        super().__init__(
            url="https://www.fairfaxcounty.gov/planningcommission/minutes-home",
            commission="Planning Commmission",
            municipality="Fairfax County",
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

    async def get_file_urls(self, existing_links):
        download_urls = []
        year_links = await self.get_page().query_selector_all(
            "a[href*='meeting-minutes']"
        )
        for year_link in year_links:
            year = await year_link.inner_text()
            if int(year) < self.MIN_YEAR:
                continue
            # Open a new page for each year
            href = await year_link.get_attribute("href")
            new_page = await self.open_url_in_new_page(href)

            # Open all the accordions in the page and select its links
            accordion_months = await new_page.query_selector_all(
                "button.accordion-dept"
            )
            for accordion_month in accordion_months:
                await accordion_month.click()
                await new_page.wait_for_timeout(1000)

            meeting_links = await new_page.query_selector_all(
                "a.nav-link[href*='minutes'][href*='.pdf']"
            )

            for link in meeting_links:
                url = await link.get_attribute("href")
                download_url = urljoin(self.base_url, url)
                download_urls.append(download_url)
                self.logger.debug(f"Download URL found: {download_url}")

            await new_page.close()

        return download_urls


if __name__ == "__main__":

    async def main():
        crawler = FairfaxCrawler()
        await crawler.crawl()

    asyncio.run(main())
