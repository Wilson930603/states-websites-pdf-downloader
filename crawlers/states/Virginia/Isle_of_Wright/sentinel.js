import { test, expect } from '@playwright/test';

test('Written with DeploySentinel Recorder', async ({ page }) => {
    // Load "https://isleofwight.novusagenda.com/agendapublic/meetingsgeneral.aspx?MeetingType=2"
    await page.goto('https://isleofwight.novusagenda.com/agendapublic/meetingsgeneral.aspx?MeetingType=2');
  
    // Resize window to 1920 x 970
    await page.setViewportSize({ width: 1920, height: 970 });
  
    // Click on <select> #SearchAgendasMeetings_ddlDateRange
    await page.click('#SearchAgendasMeetings_ddlDateRange');
  
    // Fill "cus" on <select> #SearchAgendasMeetings_ddlDateRange
    await page.selectOption('#SearchAgendasMeetings_ddlDateRange', 'cus');
  
    // Click on <input> #SearchAgendasMeetings_radCalendarFrom_dateInput
    await page.click('#SearchAgendasMeetings_radCalendarFrom_dateInput');
  
    // Click on <input> #SearchAgendasMeetings_radCalendarFrom_dateInput
    await page.click('#SearchAgendasMeetings_radCalendarFrom_dateInput');
  
    // Click on <input> #SearchAgendasMeetings_radCalendarFrom_dateInput
    await page.click('#SearchAgendasMeetings_radCalendarFrom_dateInput');
  
    // Fill "01/01/2021" on <input> #SearchAgendasMeetings_radCalendarFrom_dateInput
    await page.fill('#SearchAgendasMeetings_radCalendarFrom_dateInput', '01/01/2021');
  
    // Click on <input> #SearchAgendasMeetings_radCalendarTo_dateInput
    await page.click('#SearchAgendasMeetings_radCalendarTo_dateInput');
  
    // Click on <input> #SearchAgendasMeetings_radCalendarTo_dateInput
    await page.click('#SearchAgendasMeetings_radCalendarTo_dateInput');
  
    // Click on <input> #SearchAgendasMeetings_radCalendarTo_dateInput
    await page.click('#SearchAgendasMeetings_radCalendarTo_dateInput');
  
    // Fill "01/01/2026" on <input> #SearchAgendasMeetings_radCalendarTo_dateInput
    await page.fill('#SearchAgendasMeetings_radCalendarTo_dateInput', '01/01/2026');
  
    // Click on <input> #SearchAgendasMeetings_imageButtonSearch
    await page.click('#SearchAgendasMeetings_imageButtonSearch');
  
    // Click on <a> #SearchAgendasMeetings_radGridMeetings_ctl00_ctl22_hypMinutesPDF
    await page.click('#SearchAgendasMeetings_radGridMeetings_ctl00_ctl22_hypMinutesPDF');
  
    // Click on <a> "2"
    await page.click('[href="javascript:__doPostBack(\'SearchAgendasMeetings$radGridMeetings$ctl00$ctl03$ctl01$ctl07\',\'\')"]');
  
    // Click on <center> #SearchAgendasMeetings_radGridMeetings_ctl00__0 > td:nth-child(7) > center
    await page.click('#SearchAgendasMeetings_radGridMeetings_ctl00__0 > td:nth-child(7) > center');
  
    // Click on <a> #SearchAgendasMeetings_radGridMeetings_ctl00_ctl04_hypMinutesPDF
    await page.click('#SearchAgendasMeetings_radGridMeetings_ctl00_ctl04_hypMinutesPDF');
  
 
});