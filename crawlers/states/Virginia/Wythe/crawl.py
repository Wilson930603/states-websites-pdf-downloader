import asyncio
from crawlers.base_crawlers.base import BaseCrawler


class WythevilleCrawler(BaseCrawler):
    base_url = (
        "https://meetings.municode.com/PublishPage?"
        "cid=WYTHEVILVA&ppid=277ff12f-1d9e-4fe6-8d83-2a4a5bf2751a"
    )

    def __init__(self):
        super().__init__(
            url="https://meetings.municode.com/PublishPage?"
            "cid=WYTHEVILVA&ppid=277ff12f-1d9e-4fe6-8d83-2a4a5bf2751a&p=1",
            commission="Planning Commission",
            municipality="Wytheville",
            state="Virginia",
            document_type="Minutes",
            file_extension="pdf",
        )

    async def get_file_urls(self, existing_links):
        download_urls = []
        for page_number in range(1, 4):
            await self.get_page().goto(f"{self.base_url}&p={page_number}")
            await self.get_page().wait_for_load_state("networkidle")
            await self.get_page().wait_for_timeout(2000)  # Wait for content to load

            # Get all meeting minutes links
            meeting_links = await self.get_page().query_selector_all(
                "tr td.div-table-col.minutes a"
            )

            # Iterate through each link and download the PDF
            for link in meeting_links:
                pdf_url = await link.get_attribute("href")
                if pdf_url:
                    download_urls.append(pdf_url)
                    self.logger.debug(f"Found PDF: {pdf_url}")

        return download_urls


if __name__ == "__main__":

    async def main():
        crawler = WythevilleCrawler()
        await crawler.crawl()

    asyncio.run(main())
