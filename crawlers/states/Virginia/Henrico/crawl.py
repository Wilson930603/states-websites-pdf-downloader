import asyncio

from crawlers.base_crawlers.table_base import TableCrawler


class HenricoCounty(TableCrawler):
    def __init__(self):
        super().__init__(
            url="https://henrico.gov/planning/minutes/minutes-2020-2029/",
            commission="Planning Commision / Board of Zoning",
            municipality="Henrico County",
            state="Virginia",
            document_type="Minutes",
            file_extension="pdf",
            row_selector="tr",
            url_href='a[href*="minutes"]:not(a:has-text("Work Session"))',
        )

    async def should_crawl_row(self, row) -> bool:
        row_link = await row.query_selector("td:nth-child(1) > a[href*='minutes']")
        if not row_link:
            return False

        href = await row_link.get_attribute("href")
        # The oldest year is 2020, represented as "20mm" in the last part of the URL (20feb, 20jan...etc)
        if "20" in href.split("/")[-1]:
            return False
        return True


if __name__ == "__main__":

    async def main():
        crawler = HenricoCounty()
        await crawler.crawl()

    asyncio.run(main())
