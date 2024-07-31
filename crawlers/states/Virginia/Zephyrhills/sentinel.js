import { test, expect } from '@playwright/test';

test('Written with DeploySentinel Recorder', async ({ page }) => {
  // Load "https://zephyrhillsfl.portal.civicclerk.com/?category_id=29"
  await page.goto('https://zephyrhillsfl.portal.civicclerk.com/?category_id=29');

  // Resize window to 1536 x 695
  await page.setViewportSize({ width: 1536, height: 695 });

  // Scroll wheel by X:0, Y:400
  await page.mouse.wheel(0, 400);

  // Click on <div> #downloadFilesMenu-102-menu > div:nth-child(1)
  await page.click('#downloadFilesMenu-102-menu > div:nth-child(1)');

  // Scroll wheel by X:0, Y:4400
  await page.mouse.wheel(0, 4400);

  // Scroll wheel by X:0, Y:-200
  await page.mouse.wheel(0, -200);

  // Click on <svg> #downloadFilesMenu-506 .cpp-MuiSvgIcon-root
  await page.click('#downloadFilesMenu-506 .cpp-MuiSvgIcon-root');

  // Click on <li> "Agenda (PDF)"
  await page.click('#downloadFilesMenu-506-menuitem-0');
});