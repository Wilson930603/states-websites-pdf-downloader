import { test, expect } from "@playwright/test";

test("Written with DeploySentinel Recorder", async ({ page }) => {
  // Load "https://www.yorkcounty.gov/AgendaCenter/Planning-Commission-3"
  await page.goto(
    "https://www.yorkcounty.gov/AgendaCenter/Planning-Commission-3"
  );

  // Resize window to 1920 x 970
  await page.setViewportSize({ width: 1920, height: 970 });

  // Scroll wheel by X:0, Y:224
  await page.mouse.wheel(0, 224);

  // Click on <a> [href="/AgendaCenter/ViewFile/Minutes/_12082021-776"]
  await page.click('[href="/AgendaCenter/ViewFile/Minutes/_12082021-776"]');

  // Click on <a> "View More"
  await page.click("#btnViewMore3");

  // Click on <a> "2021"
  await page.click("#anchYearDD33");

  // Click on <a> [href="/AgendaCenter/ViewFile/Minutes/_12082021-776"]
  await page.click('[href="/AgendaCenter/ViewFile/Minutes/_12082021-776"]');
});
