import { test, expect } from '@playwright/test';

test('Written with DeploySentinel Recorder', async ({ page }) => {
  // Load "https://co.caroline.va.us/AgendaCenter/Planning-Commission-3"
  await page.goto('https://co.caroline.va.us/AgendaCenter/Planning-Commission-3');

  // Resize window to 1920 x 887
  await page.setViewportSize({ width: 1920, height: 887 });

  // Click on <a> [href="/AgendaCenter/ViewFile/Minutes/_03212024-453"]
  await page.click('[href="/AgendaCenter/ViewFile/Minutes/_03212024-453"]');
});