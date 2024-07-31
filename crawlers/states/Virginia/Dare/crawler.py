import asyncio
from datetime import datetime
import sys
import time
import os
from urllib.parse import urljoin
import httpx
sys.path.append('../../../../../muni-crawlers-wilson-main')
from crawlers.base_crawlers.table_base import TableCrawler


class DareCountyCrawler(TableCrawler):
    def __init__(self):
        super().__init__(
            url="https://www.darenc.gov/departments/planning/planning-board/agenda-minutes",
            municipality="Dare County",
            commission="Planning Commission",
            state="Virginia",
            row_selector="tbody tr",
            url_href='a[href$="0000"]',
            document_type="Minutes",
            file_extension="pdf",
        )

    async def should_crawl_row(self, row) -> bool:
        # Retrieve the header element to extract the year
        td_elements = await row.query_selector_all('td')
        i = 0
        for td_element in td_elements:
            if i == 1:
                year_text = await td_element.inner_text()
                try:
                    year = int(
                        year_text.strip().split(",")[-1]
                    )  # Extract the year from the header text
                except:
                    continue
                if year >= 2021:
                    return True
                else:
                    return False
            i +=1 
    
    async def get_file_urls(self, existing_links: list[str]):
        file_urls = []
        time.sleep(5)
        rows = await self.get_page().query_selector_all(self.row_selector)
        for row in rows:
            if not await self.should_crawl_row(row):
                continue
            download_elements = await row.query_selector_all(self.url_href)
            for download_element in download_elements:
                if not download_element:
                    continue
                download_text = await download_element.inner_text()
                print(download_text)
                if download_text == "Official Minutes":
                    download_link = download_element
                else:
                    download_link = None
                if download_link:
                    pdf_url = await download_link.get_attribute("href")
                    if pdf_url:
                        full_pdf_url = urljoin(self.url, pdf_url)
                        if self.has_redirect:
                            full_pdf_url = await self.get_redirect(full_pdf_url)
                        if self.base_url:
                            full_pdf_url = urljoin(self.base_url, pdf_url)
                        if full_pdf_url not in existing_links:
                            file_urls.append(full_pdf_url)
                            self.logger.debug(f"Found PDF: {full_pdf_url}")

        return file_urls

    async def download_file(self, url: str) -> None:
        filename = self.get_filename()
        print("==========================",filename)
        save_path = os.path.join(self.download_dir, filename)
        if not os.path.exists(self.download_dir):
            os.makedirs(self.download_dir)

        headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9,ko;q=0.8',
            # 'cookie': '_gid=GA1.2.1754396536.1722358912; _ga_SML18LLTRP=GS1.2.1722372702.3.0.1722372702.0.0.0; ASP.NET_SessionId=tkr1demsk1jb0i0ys1lvdqe3; BIGipServer~AUTO-VISION~visionlive~www.darenc.gov_443=!8MAjE7dmb3yh/+tedm1Xf9THDYxJhJT8vWugkmusrkv5sNGbQZfGbCBmGdjUIn+4Z5GkHZXV/69e9EY=; TS01af151e=0106cf681b6a8ac0df35cc1062e81a21f4f5c494c235cdeb227a3e13f43dc5ef2a99afefc0b0305177822cf703cb00b78342dabb4b0b33aefe49188ac5eac2f672ee090d6783c16346bf6e0832d2cbcc2ad09d07f1; TS3b44c919027=08b9428c85ab20003e51789ab199b851debd379509fd8c6489107c301abd9a2b8f8dc5d903fed6050852095faf1130002c10228dfc8790c9989f71ce266925dada046485cf7436f1a116bf5b7761aa39761439fc77a1dd79f00f407600c8ec56; _gat_gtag_UA_215772536_1=1; _ga_9JVPENXKS0=GS1.1.1722409599.2.1.1722409612.0.0.0; _ga=GA1.2.1151266210.1722358911; RT="z=1&dm=www.darenc.gov&si=c10a5490-06d7-4bb0-8c6e-eb363b7ac382&ss=lz9i7awo&sl=1&tt=2z1&rl=1"',
            'priority': 'u=1, i',
            'referer': 'https://www.darenc.gov/departments/planning/planning-board/agenda-minutes',
            'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }

        backoff_time = 1  # initial backoff time in seconds

        while True:
            try:
                async with httpx.AsyncClient(verify=False) as client:
                    response = await client.get(url, headers=headers)
                    if response.status_code == 200:
                        with open(save_path, "wb") as f:
                            f.write(response.content)
                        return
                    elif response.status_code == 429:
                        self.logger.warning(
                            f"Rate limited. Retrying after {backoff_time} seconds. URL: {url}"
                        )
                        await asyncio.sleep(backoff_time)
                        backoff_time = min(
                            backoff_time * 2, 60
                        )  # exponential backoff, max 60 seconds
                    else:
                        self.logger.warning(
                            f"Failed to download PDF from {url}, status code: {response.status_code}"
                        )
                        return
            except Exception as e:
                self.logger.exception(
                    f"Failed to download PDF from {url}. Error: {str(e)}"
                )
                return

if __name__ == "__main__":

    async def main():
        crawler = DareCountyCrawler()
        await crawler.crawl(debug=True,stealth=True)

    asyncio.run(main())
