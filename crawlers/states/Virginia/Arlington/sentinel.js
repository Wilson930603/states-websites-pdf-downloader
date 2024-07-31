import { test, expect } from '@playwright/test';

test('Written with DeploySentinel Recorder', async ({ page }) => {
  // Load "https://arlington.granicus.com/ViewPublisher.php?view_id=44"
  await page.goto('https://arlington.granicus.com/ViewPublisher.php?view_id=44');

  // Resize window to 1800 x 957
  await page.setViewportSize({ width: 1800, height: 957 });

  // Click on <a> "Minutes"
  await page.click('[href="//arlington.granicus.com/MinutesViewer.php?view_id=44&clip_id=4294"]');
});