import { test, expect } from "@playwright/test";

test("Written with DeploySentinel Recorder", async ({ page }) => {
  // Load "https://www.powhatanva.gov/AgendaCenter/Search/?term=&CIDs=10,7,&startDate=&endDate=&dateRange=&dateSelector="
  await page.goto(
    "https://www.powhatanva.gov/AgendaCenter/Search/?term=&CIDs=10,7,&startDate=&endDate=&dateRange=&dateSelector="
  );

  // Resize window to 1512 x 859
  await page.setViewportSize({ width: 1512, height: 859 });

  // Click on <a> [href="/AgendaCenter/ViewFile/Minutes/_05072024-1166"]
  await page.click('[href="/AgendaCenter/ViewFile/Minutes/_05072024-1166"]');

  // Click on <a> "View More"
  await page.click("#btnViewMore7");

  // Click on <a> "2021"
  await page.click("#anchYearDD37");

  // Click on <a> [href="/AgendaCenter/ViewFile/Minutes/_12072021-923"]
  await page.click('[href="/AgendaCenter/ViewFile/Minutes/_12072021-923"]');
});
