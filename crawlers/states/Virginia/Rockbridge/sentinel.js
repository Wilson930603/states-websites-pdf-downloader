import { test, expect } from "@playwright/test";

test("Written with DeploySentinel Recorder", async ({ page }) => {
  // Load "https://www.co.rockbridge.va.us/AgendaCenter/Search/?term=&CIDs=3,6,&startDate=&endDate=&dateRange=&dateSelector="
  await page.goto(
    "https://www.co.rockbridge.va.us/AgendaCenter/Search/?term=&CIDs=3,6,&startDate=&endDate=&dateRange=&dateSelector="
  );

  // Resize window to 1920 x 970
  await page.setViewportSize({ width: 1920, height: 970 });

  // Scroll wheel by X:0, Y:240
  await page.mouse.wheel(0, 240);

  // Click on <a> "View More"
  await page.click("#btnViewMore3");

  // Click on <a> "2021"
  await page.click("#anchYearDD33");

  // Click on <a> [href="/AgendaCenter/ViewFile/Minutes/_07212021-706"]
  await page.click('[href="/AgendaCenter/ViewFile/Minutes/_07212021-706"]');

  // Scroll wheel by X:0, Y:256
  await page.mouse.wheel(0, 256);

  // Click on <a> "View More"
  await page.click("#btnViewMore6");

  // Click on <a> "2021"
  await page.click("#anchYearDD36");

  // Click on <a> [href="/AgendaCenter/ViewFile/Minutes/_09082021-715"]
  await page.click('[href="/AgendaCenter/ViewFile/Minutes/_09082021-715"]');
});
