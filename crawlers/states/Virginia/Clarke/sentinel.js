import { test, expect } from '@playwright/test';

test('Written with DeploySentinel Recorder', async ({ page }) => {
  // Load "https://www.clarkecounty.gov/government/boards-commissions/planning-commission/pc-minutes/-folder-1032"
  await page.goto('https://www.clarkecounty.gov/government/boards-commissions/planning-commission/pc-minutes/-folder-1032');

  // Resize window to 1920 x 887
  await page.setViewportSize({ width: 1920, height: 887 });

  // Click on <a> "2024"
  await Promise.all([
    page.click('[href="/government/boards-commissions/planning-commission/pc-minutes/-folder-1381"]'),
    page.waitForNavigation()
  ]);

  // Click on <a> "2024-05-03 PC Business Me..."
  await page.click('[href="/home/showpublisheddocument/12292/638533660250470000"]');
});