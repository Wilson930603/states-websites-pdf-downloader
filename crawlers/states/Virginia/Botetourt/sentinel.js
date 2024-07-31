import { test, expect } from '@playwright/test';

test('Written with DeploySentinel Recorder', async ({ page }) => {
  // Load "https://www.botetourtva.gov/AgendaCenter/Planning-Commission-6"
  await page.goto('https://www.botetourtva.gov/AgendaCenter/Planning-Commission-6');

  // Resize window to 1920 x 887
  await page.setViewportSize({ width: 1920, height: 887 });

  // Scroll wheel by X:0, Y:104
  await page.mouse.wheel(0, 104);

  // Scroll wheel by X:-7, Y:41
  await page.mouse.wheel(-7, 41);

  // Scroll wheel by X:0, Y:80
  await page.mouse.wheel(0, 80);

  // Click on <a> [href="/AgendaCenter/ViewFile/Minutes/_06102024-506"]
  await page.click('[href="/AgendaCenter/ViewFile/Minutes/_06102024-506"]');
});