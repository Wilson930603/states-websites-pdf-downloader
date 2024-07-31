import { test, expect } from '@playwright/test';

test('Written with DeploySentinel Recorder', async ({ page }) => {
  // Load "https://www.darenc.gov/departments/planning/planning-board/agenda-minutes"
  await page.goto('https://www.darenc.gov/departments/planning/planning-board/agenda-minutes');

  // Resize window to 1536 x 695
  await page.setViewportSize({ width: 1536, height: 695 });

  // Scroll wheel by X:0, Y:500
  await page.mouse.wheel(0, 500);

  // Click on <a> "2021"
  await page.click('#ui-id-4');

  // Scroll wheel by X:0, Y:200
  await page.mouse.wheel(0, 200);

  // Click on <a> "Official Minutes"
  await page.click('[href="/home/showpublisheddocument/10534/637774876451270000"]');
});