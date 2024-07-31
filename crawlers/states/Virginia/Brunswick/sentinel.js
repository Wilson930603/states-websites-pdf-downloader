import { test, expect } from '@playwright/test';

test('Written with DeploySentinel Recorder', async ({ page }) => {
  // Load "https://www.brunswickco.com/cms/One.aspx?pageId=11500977&portalId=10858880"
  await page.goto('https://www.brunswickco.com/cms/One.aspx?pageId=11500977&portalId=10858880');

  // Resize window to 1920 x 887
  await page.setViewportSize({ width: 1920, height: 887 });

  // Click on <div> "2023"
  await page.click('.folder:nth-child(4) .docTitle');

  // Scroll wheel by X:0, Y:57
  await page.mouse.wheel(0, 57);

  // Scroll wheel by X:-14, Y:27
  await page.mouse.wheel(-14, 27);

  // Scroll wheel by X:0, Y:2
  await page.mouse.wheel(0, 2);

  // Scroll wheel by X:2, Y:0
  await page.mouse.wheel(2, 0);

  // Click on <a> "01-10-23 Regular Meeting"
  await page.click('.titleUser > [href="https://www.brunswickco.com/common/pages/DownloadFileByUrl.aspx?key=cPspLtzKGmg7UBuU5fRPG2a%2fWnKH65JeUsPLicyBC5gaOkvyF7eB2SxG%2f1rDpDuJGatdUu%2fiXc0TcO6MEioSY9dIJrXCg78pqnAk57Omu06ZsvYPoCLDkRa4MEwk3bO4ysL4Sna1olf2sJ6TqH8jvJFkHNhDSsmMNC%2b9Mnx1WsgcMz%2fTa2dLXoWTjDMZZCRbWQZUrGaz0s3V4drpyeIBNqczosA%3d"]');
});