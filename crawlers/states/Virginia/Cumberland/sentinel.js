import { test, expect } from "@playwright/test";

test("Written with DeploySentinel Recorder", async ({ page }) => {
  // Load "https://www.cumberlandcounty.virginia.gov/AgendaCenter/Search/?term=&CIDs=4,3,&startDate=01/01/2021&endDate=12/12/2027&dateRange=&dateSelector="
  await page.goto(
    "https://www.cumberlandcounty.virginia.gov/AgendaCenter/Search/?term=&CIDs=4,3,&startDate=01/01/2021&endDate=12/12/2027&dateRange=&dateSelector="
  );

  // Resize window to 1920 x 970
  await page.setViewportSize({ width: 1920, height: 970 });

  // Click on <a> "Board of Zoning Appeals M..."
  await page.click('p > [href="/AgendaCenter/ViewFile/Agenda/_06142023-604"]');

  // Scroll wheel by X:0, Y:96
  await page.mouse.wheel(0, 96);

  // Click on <a> "2022"
  await page.click("#a14");

  // Click on <a> "2022"
  await page.click("#a14");

  // Click on <a> "BZA Meeting Agenda"
  await page.click('p > [href="/AgendaCenter/ViewFile/Agenda/_05112022-547"]');

  // Click on <a> "2021"
  await page.click("#a24");

  // Click on <a> "Board of Zoning Appeals A..."
  await page.click('p > [href="/AgendaCenter/ViewFile/Agenda/_09082021-507"]');

  // Click on <a> [href="/AgendaCenter/ViewFile/Minutes/_02262024-641"]
  await page.click('[href="/AgendaCenter/ViewFile/Minutes/_02262024-641"]');

  // Click on <a> "2023"
  await page.click("#a13");

  // Click on <a> [href="/AgendaCenter/ViewFile/Minutes/_12042023-630"]
  await page.click('[href="/AgendaCenter/ViewFile/Minutes/_12042023-630"]');

  // Click on <a> "2022"
  await page.click("#a23");

  // Click on <a> [href="/AgendaCenter/ViewFile/Minutes/_11142022-575"]
  await page.click('[href="/AgendaCenter/ViewFile/Minutes/_11142022-575"]');

  // Click on <div> "View More"
  await page.click(".popUpParent");

  // Click on <a> "View More"
  await page.click("#btnViewMore3");

  // Click on <a> "2021"
  await page.click("#anchYearDD33");

  // Click on <a> [href="/AgendaCenter/ViewFile/Minutes/_11152021-514"]
  await page.click('[href="/AgendaCenter/ViewFile/Minutes/_11152021-514"]');
});
