import { test, expect } from '@playwright/test';

test("Written with DeploySentinel Recorder", async ({ page }) => {
  // Load "https://www.halifaxcountyva.gov/AgendaCenter/Planning-Commission-4"
  await page.goto(
    "https://www.halifaxcountyva.gov/AgendaCenter/Planning-Commission-4"
  );

  // Resize window to 1920 x 970
  await page.setViewportSize({ width: 1920, height: 970 });

  // Click on <a> [href="/AgendaCenter/ViewFile/Minutes/_05212024-506"]
  await page.click('[href="/AgendaCenter/ViewFile/Minutes/_05212024-506"]');
});