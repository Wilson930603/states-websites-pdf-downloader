import { test, expect } from "@playwright/test";

test("Written with DeploySentinel Recorder", async ({ page }) => {
  // Load "https://orangecountyva.gov/Archive.aspx"
  await page.goto("https://orangecountyva.gov/Archive.aspx");

  // Resize window to 1512 x 818
  await page.setViewportSize({ width: 1512, height: 818 });

  // Fill "-1" on <select> #amidDDN135
  await Promise.all([
    page.selectOption("#amidDDN135", "-1"),
    page.waitForNavigation(),
  ]);

  // Scroll wheel by X:0, Y:-9
  await page.mouse.wheel(0, -9);

  // Scroll wheel by X:1, Y:-3
  await page.mouse.wheel(1, -3);

  // Scroll wheel by X:0, Y:-2
  await page.mouse.wheel(0, -2);

  // Scroll wheel by X:1, Y:-3
  await page.mouse.wheel(1, -3);

  // Scroll wheel by X:0, Y:-2
  await page.mouse.wheel(0, -2);

  // Scroll wheel by X:1, Y:-2
  await page.mouse.wheel(1, -2);

  // Scroll wheel by X:0, Y:-2
  await page.mouse.wheel(0, -2);

  // Scroll wheel by X:2, Y:-3
  await page.mouse.wheel(2, -3);

  // Scroll wheel by X:0, Y:-3
  await page.mouse.wheel(0, -3);

  // Scroll wheel by X:2, Y:-3
  await page.mouse.wheel(2, -3);

  // Scroll wheel by X:0, Y:-3
  await page.mouse.wheel(0, -3);

  // Scroll wheel by X:4, Y:-8
  await page.mouse.wheel(4, -8);

  // Scroll wheel by X:0, Y:-2
  await page.mouse.wheel(0, -2);

  // Scroll wheel by X:3, Y:-5
  await page.mouse.wheel(3, -5);

  // Scroll wheel by X:0, Y:-2
  await page.mouse.wheel(0, -2);

  // Scroll wheel by X:4, Y:-4
  await page.mouse.wheel(4, -4);

  // Scroll wheel by X:0, Y:-2
  await page.mouse.wheel(0, -2);

  // Scroll wheel by X:2, Y:-2
  await page.mouse.wheel(2, -2);

  // Scroll wheel by X:0, Y:-2
  await page.mouse.wheel(0, -2);

  // Scroll wheel by X:5, Y:-8
  await page.mouse.wheel(5, -8);

  // Scroll wheel by X:0, Y:-2
  await page.mouse.wheel(0, -2);

  // Scroll wheel by X:2, Y:-4
  await page.mouse.wheel(2, -4);

  // Scroll wheel by X:0, Y:-2
  await page.mouse.wheel(0, -2);

  // Scroll wheel by X:1, Y:-1
  await page.mouse.wheel(1, -1);

  // Scroll wheel by X:0, Y:-3
  await page.mouse.wheel(0, -3);

  // Scroll wheel by X:0, Y:7
  await page.mouse.wheel(0, 7);

  // Scroll wheel by X:-35, Y:128
  await page.mouse.wheel(-35, 128);

  // Scroll wheel by X:0, Y:2
  await page.mouse.wheel(0, 2);

  // Scroll wheel by X:-2, Y:2
  await page.mouse.wheel(-2, 2);

  // Scroll wheel by X:0, Y:1
  await page.mouse.wheel(0, 1);

  // Click on <a> "Planning Commission Actio..."
  await page.click('[href="Archive.aspx?ADID=3242"]');

  // Click on <a> "All Archives"
  await Promise.all([
    page.click('[href="Archive.aspx"]'),
    page.waitForNavigation(),
  ]);

  // Scroll wheel by X:0, Y:-6
  await page.mouse.wheel(0, -6);

  // Scroll wheel by X:4, Y:-17
  await page.mouse.wheel(4, -17);

  // Scroll wheel by X:0, Y:-8
  await page.mouse.wheel(0, -8);

  // Scroll wheel by X:3, Y:-17
  await page.mouse.wheel(3, -17);

  // Scroll wheel by X:0, Y:-10
  await page.mouse.wheel(0, -10);

  // Scroll wheel by X:2, Y:-9
  await page.mouse.wheel(2, -9);

  // Scroll wheel by X:0, Y:-433
  await page.mouse.wheel(0, -433);

  // Scroll wheel by X:0, Y:2
  await page.mouse.wheel(0, 2);

  // Scroll wheel by X:-744, Y:2335
  await page.mouse.wheel(-744, 2335);

  // Scroll wheel by X:0, Y:2
  await page.mouse.wheel(0, 2);

  // Scroll wheel by X:-2, Y:2
  await page.mouse.wheel(-2, 2);

  // Scroll wheel by X:0, Y:2
  await page.mouse.wheel(0, 2);

  // Scroll wheel by X:-260, Y:715
  await page.mouse.wheel(-260, 715);

  // Scroll wheel by X:0, Y:1
  await page.mouse.wheel(0, 1);

  // Scroll wheel by X:-1, Y:1
  await page.mouse.wheel(-1, 1);

  // Scroll wheel by X:0, Y:2
  await page.mouse.wheel(0, 2);

  // Scroll wheel by X:-2, Y:2
  await page.mouse.wheel(-2, 2);

  // Scroll wheel by X:0, Y:3
  await page.mouse.wheel(0, 3);

  // Scroll wheel by X:-163, Y:583
  await page.mouse.wheel(-163, 583);

  // Press f on body
  await page.press(".cpTextResizeOn", "f");

  // Click on <select> #amidDDN141
  await page.click("#amidDDN141");

  // Fill "-1" on <select> #amidDDN141
  await Promise.all([
    page.selectOption("#amidDDN141", "-1"),
    page.waitForNavigation(),
  ]);

  // Scroll wheel by X:0, Y:1
  await page.mouse.wheel(0, 1);

  // Scroll wheel by X:-28, Y:77
  await page.mouse.wheel(-28, 77);

  // Scroll wheel by X:0, Y:1
  await page.mouse.wheel(0, 1);

  // Scroll wheel by X:-1, Y:1
  await page.mouse.wheel(-1, 1);

  // Scroll wheel by X:0, Y:2
  await page.mouse.wheel(0, 2);

  // Scroll wheel by X:-2, Y:0
  await page.mouse.wheel(-2, 0);

  // Click on <a> "Planning Commission Actio..."
  await page.click('[href="Archive.aspx?ADID=3482"]');
});
