import { test, expect } from '@playwright/test';

test('Written with DeploySentinel Recorder', async ({ page }) => {
  // Load "https://www.charlescityva.us/AgendaCenter/Planning-Commission-2"
  await page.goto('https://www.charlescityva.us/AgendaCenter/Planning-Commission-2');

  // Resize window to 1920 x 887
  await page.setViewportSize({ width: 1920, height: 887 });

  // Click on <a> [href="/AgendaCenter/ViewFile/Minutes/_05092024-521"]
  await page.click('[href="/AgendaCenter/ViewFile/Minutes/_05092024-521"]');
});