import asyncio

from crawlers.base_crawlers.base import BaseCrawler
from urllib.parse import urljoin


class PittsylvaniaCountyCrawler(BaseCrawler):
    base_url = "https://www.pittsylvaniacountyva.gov"

    def __init__(self):
        super().__init__(
            url="https://www.pittsylvaniacountyva.gov/government/"
            "boards-and-commissions/planning-commission/-toggle-allpast",
            commission="Planning Commission",
            municipality="Pittsylvania County",
            state="Virginia",
            document_type="Minutes",
            file_extension="pdf",
        )

    async def open_url_in_new_page(self, url, timeout=3000):
        base_url_for_2021 = "https://weblink.pittgov.net"
        new_page = await self.get_browser().new_page()
        full_url = urljoin(base_url_for_2021, url)
        await new_page.goto(full_url)
        await new_page.wait_for_timeout(timeout)
        return new_page

    async def get_file_urls_for_2021(self, existing_links):
        download_urls = []
        await self.get_page().goto(
            "https://weblink.pittgov.net/WebLink/Browse.aspx?id=446345&dbid=0&repo=PittGovDocs"
        )
        await self.get_page().wait_for_selector('a:has-text("Minutes")')
        links = await self.get_page().query_selector_all('a:has-text("Minutes")')
        for link in links:
            # open a new page
            minutes_page_href = await link.get_attribute("href")
            minutes_page = await self.open_url_in_new_page(minutes_page_href)
            # get the download link
            download_link = await minutes_page.query_selector('a[href*="Minutes"]')
            if not download_link:
                continue
            href = await download_link.get_attribute("href")
            full_url = urljoin(self.base_url, href)
            download_urls.append(full_url)
            self.logger.debug(f"Found PDF: {full_url}")
            await minutes_page.close()
        return download_urls

    async def get_file_urls(self, existing_links):
        download_urls = []
        # Collect links 2022 onwards
        links = await self.get_page().query_selector_all('a:has-text("Minutes")')
        for link in links:
            href = await link.get_attribute("href")
            full_url = urljoin(self.base_url, href)
            download_urls.append(full_url)
            self.logger.debug(f"Found PDF: {full_url}")
        download_urls += await self.get_file_urls_for_2021(existing_links)
        return download_urls


if __name__ == "__main__":

    async def main():
        crawler = PittsylvaniaCountyCrawler()
        await crawler.crawl(
            debug=True
        )  # Seems not to be work using a headless browser, so we need to use debug=True

    asyncio.run(main())
