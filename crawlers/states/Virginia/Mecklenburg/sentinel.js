import { test, expect } from '@playwright/test';

test("Written with DeploySentinel Recorder", async ({ page }) => {
  // Load "https://www.mecklenburgva.com/AgendaCenter/Search/?term=&CIDs=5,8,&startDate=&endDate=&dateRange=&dateSelector="
  await page.goto(
    "https://www.mecklenburgva.com/AgendaCenter/Search/?term=&CIDs=5,8,&startDate=&endDate=&dateRange=&dateSelector="
  );

  // Resize window to 1920 x 970
  await page.setViewportSize({ width: 1920, height: 970 });

  // Scroll wheel by X:0, Y:192
  await page.mouse.wheel(0, 192);

  // Click on <a> [href="/AgendaCenter/ViewFile/Minutes/_03262024-142"]
  await page.click('[href="/AgendaCenter/ViewFile/Minutes/_03262024-142"]');

  // Click on <a> "2023"
  await page.click("#a15");

  // Click on <a> [href="/AgendaCenter/ViewFile/Minutes/_09262023-123"]
  await page.click('[href="/AgendaCenter/ViewFile/Minutes/_09262023-123"]');

  // Scroll wheel by X:0, Y:592
  await page.mouse.wheel(0, 592);

  // Click on <a> "2024"
  await page.click("#a08");

  // Click on <a> [href="/AgendaCenter/ViewFile/Minutes/_04252024-145"]
  await page.click('[href="/AgendaCenter/ViewFile/Minutes/_04252024-145"]');

  // Click on <a> "View More"
  await page.click("#btnViewMore8");

  // Click on <a> "2021"
  await page.click("#anchYearDD38");

  // Click on <a> [href="/AgendaCenter/ViewFile/Minutes/_03252021-70"]
  await page.click('[href="/AgendaCenter/ViewFile/Minutes/_03252021-70"]');
});