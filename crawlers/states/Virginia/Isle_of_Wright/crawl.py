import asyncio

from crawlers.base_crawlers.novusagenda import NovusAgendaCrawler


class IsleOfWright(NovusAgendaCrawler):
    def __init__(self):
        super().__init__(
            url="https://isleofwight.novusagenda.com/agendapublic/meetingsgeneral.aspx?MeetingType=2",
            commission="Planning Commission",
            municipality="Isle of Wright",
            state="Virginia",
            pagination_element="div.rgWrap.rgInfoPart strong:nth-child(2)",
        )

    async def interactions(self) -> None:
        await self.interactions_template(
            date_range_id="#SearchAgendasMeetings_ddlDateRange",
            calendar_from_id="#SearchAgendasMeetings_radCalendarFrom_dateInput",
            calendar_to_id="#SearchAgendasMeetings_radCalendarTo_dateInput",
            meeting_type_id="#SearchAgendasMeetings_ctl00",
            search_button_id="#SearchAgendasMeetings_imageButtonSearch",
            meeting_label="Planning Commission Meeting",
        )


if __name__ == "__main__":

    async def main():
        crawler = IsleOfWright()
        await crawler.crawl()

    asyncio.run(main())
