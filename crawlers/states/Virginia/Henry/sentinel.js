import { test, expect } from '@playwright/test';

test("Written with DeploySentinel Recorder", async ({ page }) => {
  // Load "https://www.henrycountyva.gov/AgendaCenter/Search/?term=&CIDs=9,8,&startDate=&endDate=&dateRange=&dateSelector="
  await page.goto(
    "https://www.henrycountyva.gov/AgendaCenter/Search/?term=&CIDs=9,8,&startDate=&endDate=&dateRange=&dateSelector="
  );

  // Resize window to 1920 x 970
  await page.setViewportSize({ width: 1920, height: 970 });

  // Click on <a> [href="/AgendaCenter/ViewFile/Minutes/_04242024-186"]
  await page.click('[href="/AgendaCenter/ViewFile/Minutes/_04242024-186"]');

  // Scroll wheel by X:0, Y:160
  await page.mouse.wheel(0, 160);

  // Click on <a> [href="/AgendaCenter/ViewFile/Minutes/_04102024-181"]
  await page.click('[href="/AgendaCenter/ViewFile/Minutes/_04102024-181"]');
});