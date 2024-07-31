import { test, expect } from '@playwright/test';

test('Written with DeploySentinel Recorder', async ({ page }) => {
  // Load "https://www.buckinghamcountyva.org/administration/boards___commissions/planning_commission.php"
  await page.goto('https://www.buckinghamcountyva.org/administration/boards___commissions/planning_commission.php');

  // Resize window to 1920 x 887
  await page.setViewportSize({ width: 1920, height: 887 });

  // Scroll wheel by X:0, Y:459
  await page.mouse.wheel(0, 459);

  // Click on <a> "Minutes"
  await page.click('[href="Document_Center/Agenda & Minutes/Planning Commission/2024/April 22.pdf"]');
});