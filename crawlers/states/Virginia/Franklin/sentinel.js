import { test, expect } from "@playwright/test";

test("Written with DeploySentinel Recorder", async ({ page }) => {
  // Load "https://www.dinwiddieva.us/AgendaCenter/Search/?term=&CIDs=3,1,&startDate=01/01/2021&endDate=12/12/2027&dateRange=&dateSelector="
  await page.goto(
    "https://www.dinwiddieva.us/AgendaCenter/Search/?term=&CIDs=3,1,&startDate=01/01/2021&endDate=12/12/2027&dateRange=&dateSelector="
  );

  // Resize window to 1920 x 970
  await page.setViewportSize({ width: 1920, height: 970 });

  // Click on <a> "Board of Zoning Appeals O..."
  await page.click(
    'p > [href="/AgendaCenter/ViewFile/Agenda/_01172024-692?html=true"]'
  );

  // Scroll wheel by X:0, Y:128
  await page.mouse.wheel(0, 128);

  // Click on <a> "2023"
  await page.click("#a13");

  // Click on <a> "Board of Zoning Appeals R..."
  await page.click(
    'p > [href="/AgendaCenter/ViewFile/Agenda/_03152023-640?html=true"]'
  );

  // Click on <a> "2022"
  await page.click("#a23");

  // Click on <p> "Board of Zoning Appeals R..."
  await page.click("#row586bbe2166c p");

  // Click on <a> "Board of Zoning Appeals R..."
  await page.click(
    'p > [href="/AgendaCenter/ViewFile/Agenda/_05182022-586?html=true"]'
  );

  // Scroll wheel by X:0, Y:336
  await page.mouse.wheel(0, 336);

  // Click on <a> "2023"
  await page.click("#a11");

  // Click on <a> [href="/AgendaCenter/ViewFile/Minutes/_11082023-680"]
  await page.click('[href="/AgendaCenter/ViewFile/Minutes/_11082023-680"]');

  // Click on <a> "2022"
  await page.click("#a21");

  // Click on <a> [href="/AgendaCenter/ViewFile/Minutes/_11092022-616"]
  await page.click('[href="/AgendaCenter/ViewFile/Minutes/_11092022-616"]');

  // Click on <a> "View More"
  await page.click("#btnViewMore1");

  // Click on <a> "2021"
  await page.click("#anchYearDD31");

  // Click on <a> [href="/AgendaCenter/ViewFile/Minutes/_12082021-554"]
  await page.click('[href="/AgendaCenter/ViewFile/Minutes/_12082021-554"]');
});
