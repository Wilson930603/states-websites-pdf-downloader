import { test, expect } from '@playwright/test';

test('Written with DeploySentinel Recorder', async ({ page }) => {
  // Load "https://www.bathcountyva.gov/cms/One.aspx?pageId=11781522&portalId=11366390&objectId.191101=19352253&contextId.191101=11781523&parentId.191101=11781524"
  await page.goto('https://www.bathcountyva.gov/cms/One.aspx?pageId=11781522&portalId=11366390&objectId.191101=19352253&contextId.191101=11781523&parentId.191101=11781524');

  // Resize window to 1920 x 887
  await page.setViewportSize({ width: 1920, height: 887 });

  // Click on <div> "2024 Planning Commission ..."
  await page.click('.folder:nth-child(3) .docTitle');

  // Click on <a> "01-22-2024 Planning Commi..."
  await page.click('.titleUser > [href="/common/pages/DownloadFileByUrl.aspx?key=EMN%2beugQFcfeQIgPDoYbg6CeAVwKYY%2bL9zYEIW5LyCF9ho7SDa50CHCubeJVpQpmRHppYSEoodONe6Qko2mAdiUBYu1fn6z2Q%2bruyLdqaDcLu1UIm2T1qxYEMxPaH5NlKpx93yrb3Z3ZEHS2Wvu0A%2fXAhFCFui6CrVFVeAE92ZFJS%2bC9ve749wD1JzuxiGJvJTJif6imW9uTvkDY11IFu1xOfFcu9MnOx3lGINej28mqpRom24m8H1mMp1ylEQ6alRJlrKEuQ2SGnyPjGaKJdp3tZrM%3d"]');
});