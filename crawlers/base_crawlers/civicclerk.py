from typing import List

from crawlers.base_crawlers.base import BaseCrawler


class CivicClerkCrawler(BaseCrawler):
    MIN_DATE = "01/01/2021"
    MIN_DATE_SELECTOR = "#mui-2"
    DEFAULT_STOP_SCROLL_SIGNAL_PAST = (
        "There are no past events for your selected filters"
    )
    DEFAULT_STOP_SCROLL_SIGNAL_UPCOMING = "There are no more upcoming events"
    DOCUMENT_TYPE = "Minutes"
    FILE_EXTENSION = "pdf"
    DEFAULT_SCROLL_CONTAINER_SELECTOR = ".cpp-MuiListSubheader-root"
    DEFAULT_DOWNLOAD_BUTTON_TEXT = "Minutes (PDF)"

    def __init__(
        self,
        url: str,
        municipality: str,
        commission: str,
        state: str,
        document_type: str = DOCUMENT_TYPE,
        file_extension: str = FILE_EXTENSION,
        scroll_container_selector: str = DEFAULT_SCROLL_CONTAINER_SELECTOR,
        stop_scroll_signal_upcoming: str = DEFAULT_STOP_SCROLL_SIGNAL_UPCOMING,
        stop_scroll_signal_past: str = DEFAULT_STOP_SCROLL_SIGNAL_PAST,
        download_button_text: str = DEFAULT_DOWNLOAD_BUTTON_TEXT,
    ):
        super().__init__(
            url=url,
            municipality=municipality,
            commission=commission,
            state=state,
            document_type=document_type,
            file_extension=file_extension,
        )
        self.scroll_container_selector: str = scroll_container_selector
        self.stop_scroll_signal_upcoming: str = stop_scroll_signal_upcoming
        self.stop_scroll_signal_past: str = stop_scroll_signal_past
        self.download_button_text: str = download_button_text

    async def perform_interactions(self) -> None:
        await self.set_date_filter()
        await self.scroll_to_load_all()

    async def get_file_urls(self, existing_links: list) -> List[str]:
        download_urls = []

        async def intercept_route(route, request):
            if "GetMeetingFileStream" in request.url:
                self.logger.debug(f"Intercepted request: {request.url}")
                download_urls.append(request.url)
            await route.continue_()

        # Intercepting the network requests
        await self.get_page().route("**/*", intercept_route)

        download_buttons = await self.get_page().query_selector_all(
            '[id^="downloadFilesMenu-"]:not([id*="-menu"]):not([id*="-menuitem"])'
        )

        for button in download_buttons:
            button_id = await button.get_attribute("id")
            
            try:
                # Ensure the button is in view and click it using JavaScript to avoid interception issues
                await self.get_page().evaluate(
                    f'document.getElementById("{button_id}").scrollIntoView()'
                )
                await self.get_page().evaluate(
                    f'document.getElementById("{button_id}").click()'
                )
                await self.get_page().wait_for_timeout(
                    1000
                )  # wait for the menu to appear

                # Find the correct menu item
                menu_items = await self.get_page().query_selector_all(
                    f"#{button_id}-menu li"
                )
                #print(menu_items)
                download_menu_item = None
                for item in menu_items:
                    item_text = await item.inner_text()
                    if self.download_button_text in item_text:
                        download_menu_item = item
                        break

                if not download_menu_item:
                    self.logger.debug(
                        f"No download menu item found for button: {button_id}"
                    )
                    continue

                # Click the menu item using JavaScript to trigger the download request
                await self.get_page().evaluate(
                    "(item) => item.click()", download_menu_item
                )
                await self.get_page().wait_for_timeout(
                    1000
                )  # wait for the download request to be captured

            except Exception as e:
                self.logger.exception(
                    f"Error encountered while extracting file URLs: {e}"
                )

        return download_urls

    async def set_date_filter(self):
        try:
            await self.get_page().click(self.MIN_DATE_SELECTOR)
            await self.wait_for_timeout()
            await self.get_page().fill(self.MIN_DATE_SELECTOR, self.MIN_DATE)
            await self.wait_for_timeout()
        except Exception:
            self.logger.exception("Error encountered while setting the date filter.")

    async def scroll_to_load_all(self):
        await self.get_page().click(self.scroll_container_selector)
        await self.get_page().mouse.wheel(0, -1000)

        while (
            await self.get_page()
            .locator("p", has_text=self.stop_scroll_signal_upcoming)
            .count()
            == 0
        ):
            await self.get_page().click(self.scroll_container_selector)
            await self.get_page().mouse.wheel(0, 10000)
            await self.get_page().wait_for_timeout(2000)

        while (
            await self.get_page()
            .locator("p", has_text=self.stop_scroll_signal_past)
            .count()
            == 0
        ):
            await self.get_page().click(self.scroll_container_selector)
            await self.get_page().mouse.wheel(0, -10000)
            await self.get_page().wait_for_timeout(2000)

    async def wait_for_timeout(self):
        await self.get_page().wait_for_timeout(1000)
