import { test, expect } from '@playwright/test';

test('Written with DeploySentinel Recorder', async ({ page }) => {
  // Load "https://augustava.granicus.com/ViewPublisher.php?view_id=1"
  await page.goto('https://augustava.granicus.com/ViewPublisher.php?view_id=1');

  // Resize window to 1920 x 887
  await page.setViewportSize({ width: 1920, height: 887 });

  // Click on <a> "Minutes"
  await page.click('[href="https://augustava.granicus.com/services/minutes/reports/843aa789-98c9-4981-996d-31d0a8aac1e0/attachment"]');
});