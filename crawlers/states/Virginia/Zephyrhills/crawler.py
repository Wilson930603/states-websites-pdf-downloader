import asyncio
import sys
sys.path.append('../../../../../muni-crawlers-wilson-main')
from crawlers.base_crawlers.civicclerk import CivicClerkCrawler


class ZephyrhillsPortalCrawler(CivicClerkCrawler):
    def __init__(self):
        super().__init__(
            url="https://zephyrhillsfl.portal.civicclerk.com/?category_id=29",
            commission="Planning Commission",
            municipality="Zephyrhills Portal",
            state="Virginia",
            document_type="Minutes",
            file_extension="pdf",
        )
    

if __name__ == "__main__":

    async def main():
        crawler = ZephyrhillsPortalCrawler()
        await crawler.crawl()

    asyncio.run(main())
