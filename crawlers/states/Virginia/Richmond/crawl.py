import asyncio

from crawlers.base_crawlers.legistar import LegistarCrawler


class RichmondCrawler(LegistarCrawler):
    def __init__(self):
        super().__init__(
            url="https://richmondva.legistar.com/Calendar.aspx",
            commission="Planning Commission",
            municipality="Richmond",
            state="Virginia",
            base_url="https://richmondva.legistar.com/",
        )

    async def set_filters(self) -> None:
        # Select the "Planning Commision" from the dropdown
        await self.get_page().click("#ctl00_ContentPlaceHolder1_lstBodies_Input")
        await self.get_page().click('li:has-text("Planning Commission")')
        await self.get_page().wait_for_load_state("networkidle")

        # Select "All Years" from the year dropdown
        await self.get_page().click("#ctl00_ContentPlaceHolder1_lstYears_Input")
        await self.get_page().click('li:has-text("All Years")')
        await self.get_page().wait_for_load_state("networkidle")


if __name__ == "__main__":

    async def main():
        crawler = RichmondCrawler()
        await crawler.crawl()

    asyncio.run(main())
