import { test, expect } from '@playwright/test';

test('Written with DeploySentinel Recorder', async ({ page }) => {
  // Load "https://www.co.accomack.va.us/government/board-appointed-bodies/accomack-county-planning-commission/minutes-copy-"
  await page.goto('https://www.co.accomack.va.us/government/board-appointed-bodies/accomack-county-planning-commission/minutes-copy-');

  // Resize window to 1800 x 957
  await page.setViewportSize({ width: 1800, height: 957 });

  // Click on <a> "PDF"
  await page.click('[href="https://www.co.accomack.va.us/home/showpublisheddocument/16754/638120591816800000"]');
});