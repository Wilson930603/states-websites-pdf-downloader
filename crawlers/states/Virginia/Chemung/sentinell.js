import { test, expect } from '@playwright/test';

test('Written with DeploySentinel Recorder', async ({ page }) => {
  // Load "https://www.chemungcountyny.gov/506/Chemung-County-Planning-Board"
  await page.goto('https://www.chemungcountyny.gov/506/Chemung-County-Planning-Board');

  // Resize window to 1536 x 695
  await page.setViewportSize({ width: 1536, height: 695 });

  // Scroll wheel by X:0, Y:1600
  await page.mouse.wheel(0, 1600);

  // Click on <a> "Meeting Minutes"
  await page.click('li:nth-child(2) > [href="#tabba0f6144-b21b-489d-93a6-4b52ae475f15_1"]');

  // Click on <a> "2023 08 24 CCPB Meeting N..."
  await page.click('[href="/DocumentCenter/View/12845/2023-08-24-CCPB-Meeting-Notes-ApprovedKM"]');
});