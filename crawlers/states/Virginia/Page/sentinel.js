import { test, expect } from "@playwright/test";

test("Written with DeploySentinel Recorder", async ({ page }) => {
  // Load "https://www.pagecounty.virginia.gov/AgendaCenter/Search/?term=&CIDs=7,5,&startDate=&endDate=&dateRange=&dateSelector="
  await page.goto(
    "https://www.pagecounty.virginia.gov/AgendaCenter/Search/?term=&CIDs=7,5,&startDate=&endDate=&dateRange=&dateSelector="
  );

  // Resize window to 1920 x 970
  await page.setViewportSize({ width: 1920, height: 970 });

  // Click on <a> [href="/AgendaCenter/ViewFile/Minutes/_03192024-900"]
  await page.click('[href="/AgendaCenter/ViewFile/Minutes/_03192024-900"]');

  // Click on <a> "View More"
  await page.click("#btnViewMore7");

  // Click on <a> "2021"
  await page.click("#anchYearDD37");

  // Click on <a> [href="/AgendaCenter/ViewFile/Minutes/_04202021-652"]
  await page.click('[href="/AgendaCenter/ViewFile/Minutes/_04202021-652"]');

  // Click on <a> [href="/AgendaCenter/ViewFile/Minutes/_06252024-930"]
  await page.click('[href="/AgendaCenter/ViewFile/Minutes/_06252024-930"]');

  // Click on <a> "View More"
  await page.click("#btnViewMore5");

  // Click on <li> "2021"
  await page.click("#yearDD5 li:nth-child(1)");

  // Click on <li> "2021"
  await page.click("#yearDD5 li:nth-child(1)");

  // Click on <a> "2021"
  await page.click("#anchYearDD35");

  // Click on <a> [href="/AgendaCenter/ViewFile/Minutes/_12142021-708"]
  await page.click('[href="/AgendaCenter/ViewFile/Minutes/_12142021-708"]');
});
