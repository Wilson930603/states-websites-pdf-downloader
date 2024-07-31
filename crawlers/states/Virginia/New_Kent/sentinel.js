import { test, expect } from "@playwright/test";

test("Written with DeploySentinel Recorder", async ({ page }) => {
  // Load "https://www.co.new-kent.va.us/Archive.aspx"
  await page.goto("https://www.co.new-kent.va.us/Archive.aspx");

  // Resize window to 1512 x 859
  await page.setViewportSize({ width: 1512, height: 859 });

  // Scroll wheel by X:0, Y:-1
  await page.mouse.wheel(0, -1);

  // Scroll wheel by X:-15, Y:-97
  await page.mouse.wheel(-15, -97);

  // Scroll wheel by X:0, Y:-542
  await page.mouse.wheel(0, -542);

  // Scroll wheel by X:0, Y:7
  await page.mouse.wheel(0, 7);

  // Scroll wheel by X:-15, Y:138
  await page.mouse.wheel(-15, 138);

  // Scroll wheel by X:0, Y:856
  await page.mouse.wheel(0, 856);

  // Scroll wheel by X:-233, Y:600
  await page.mouse.wheel(-233, 600);

  // Scroll wheel by X:0, Y:2
  await page.mouse.wheel(0, 2);

  // Scroll wheel by X:-2, Y:2
  await page.mouse.wheel(-2, 2);

  // Scroll wheel by X:-2, Y:0
  await page.mouse.wheel(-2, 0);

  // Scroll wheel by X:0, Y:2
  await page.mouse.wheel(0, 2);

  // Press f on body
  await page.press(".cpTextResizeOn", "f");

  // Resize window to 1512 x 818
  await page.setViewportSize({ width: 1512, height: 818 });

  // Scroll wheel by X:0, Y:28
  await page.mouse.wheel(0, 28);

  // Scroll wheel by X:-6, Y:28
  await page.mouse.wheel(-6, 28);

  // Scroll wheel by X:0, Y:4
  await page.mouse.wheel(0, 4);

  // Scroll wheel by X:-9, Y:43
  await page.mouse.wheel(-9, 43);

  // Resize window to 1512 x 859
  await page.setViewportSize({ width: 1512, height: 859 });

  // Scroll wheel by X:-20, Y:53
  await page.mouse.wheel(-20, 53);

  // Scroll wheel by X:0, Y:2
  await page.mouse.wheel(0, 2);

  // Scroll wheel by X:-4, Y:4
  await page.mouse.wheel(-4, 4);

  // Scroll wheel by X:0, Y:71
  await page.mouse.wheel(0, 71);

  // Scroll wheel by X:-35, Y:87
  await page.mouse.wheel(-35, 87);

  // Scroll wheel by X:0, Y:103
  await page.mouse.wheel(0, 103);

  // Scroll wheel by X:-4, Y:13
  await page.mouse.wheel(-4, 13);

  // Scroll wheel by X:0, Y:6
  await page.mouse.wheel(0, 6);

  // Scroll wheel by X:-31, Y:86
  await page.mouse.wheel(-31, 86);

  // Scroll wheel by X:0, Y:2
  await page.mouse.wheel(0, 2);

  // Scroll wheel by X:-1, Y:1
  await page.mouse.wheel(-1, 1);

  // Scroll wheel by X:0, Y:1
  await page.mouse.wheel(0, 1);

  // Scroll wheel by X:-2, Y:2
  await page.mouse.wheel(-2, 2);

  // Scroll wheel by X:0, Y:2
  await page.mouse.wheel(0, 2);

  // Scroll wheel by X:-2, Y:2
  await page.mouse.wheel(-2, 2);

  // Scroll wheel by X:0, Y:2
  await page.mouse.wheel(0, 2);

  // Scroll wheel by X:-2, Y:2
  await page.mouse.wheel(-2, 2);

  // Scroll wheel by X:-2, Y:0
  await page.mouse.wheel(-2, 0);

  // Scroll wheel by X:0, Y:4
  await page.mouse.wheel(0, 4);

  // Scroll wheel by X:-1, Y:3
  await page.mouse.wheel(-1, 3);

  // Scroll wheel by X:0, Y:4
  await page.mouse.wheel(0, 4);

  // Scroll wheel by X:-155, Y:558
  await page.mouse.wheel(-155, 558);

  // Scroll wheel by X:0, Y:1
  await page.mouse.wheel(0, 1);

  // Scroll wheel by X:-20, Y:30
  await page.mouse.wheel(-20, 30);

  // Scroll wheel by X:0, Y:2
  await page.mouse.wheel(0, 2);

  // Scroll wheel by X:-3, Y:3
  await page.mouse.wheel(-3, 3);

  // Scroll wheel by X:0, Y:2
  await page.mouse.wheel(0, 2);

  // Scroll wheel by X:-2, Y:2
  await page.mouse.wheel(-2, 2);

  // Scroll wheel by X:0, Y:4
  await page.mouse.wheel(0, 4);

  // Scroll wheel by X:-2, Y:0
  await page.mouse.wheel(-2, 0);

  // Scroll wheel by X:0, Y:2
  await page.mouse.wheel(0, 2);

  // Scroll wheel by X:-4, Y:0
  await page.mouse.wheel(-4, 0);

  // Fill "-1" on <select> #amidDDN382
  await Promise.all([
    page.selectOption("#amidDDN382", "-1"),
    page.waitForNavigation(),
  ]);

  // Scroll wheel by X:0, Y:1
  await page.mouse.wheel(0, 1);

  // Scroll wheel by X:-25, Y:48
  await page.mouse.wheel(-25, 48);

  // Scroll wheel by X:0, Y:2
  await page.mouse.wheel(0, 2);

  // Scroll wheel by X:-2, Y:3
  await page.mouse.wheel(-2, 3);

  // Scroll wheel by X:0, Y:1
  await page.mouse.wheel(0, 1);

  // Scroll wheel by X:-1, Y:1
  await page.mouse.wheel(-1, 1);

  // Scroll wheel by X:0, Y:1
  await page.mouse.wheel(0, 1);

  // Scroll wheel by X:-2, Y:2
  await page.mouse.wheel(-2, 2);

  // Scroll wheel by X:0, Y:2
  await page.mouse.wheel(0, 2);

  // Scroll wheel by X:-2, Y:2
  await page.mouse.wheel(-2, 2);

  // Click on <a> "December 20, 2021 Minutes..."
  await page.click('[href="Archive.aspx?ADID=6077"]');

  // Click on <a> "All Archives"
  await Promise.all([
    page.click('[href="Archive.aspx"]'),
    page.waitForNavigation(),
  ]);

  // Scroll wheel by X:0, Y:1201
  await page.mouse.wheel(0, 1201);

  // Scroll wheel by X:-19, Y:130
  await page.mouse.wheel(-19, 130);

  // Scroll wheel by X:0, Y:568
  await page.mouse.wheel(0, 568);

  // Scroll wheel by X:-330, Y:1175
  await page.mouse.wheel(-330, 1175);

  // Scroll wheel by X:0, Y:4
  await page.mouse.wheel(0, 4);

  // Scroll wheel by X:-30, Y:119
  await page.mouse.wheel(-30, 119);

  // Scroll wheel by X:0, Y:1015
  await page.mouse.wheel(0, 1015);

  // Scroll wheel by X:-11, Y:89
  await page.mouse.wheel(-11, 89);

  // Scroll wheel by X:0, Y:396
  await page.mouse.wheel(0, 396);

  // Scroll wheel by X:-19, Y:157
  await page.mouse.wheel(-19, 157);

  // Scroll wheel by X:0, Y:585
  await page.mouse.wheel(0, 585);

  // Scroll wheel by X:-15, Y:69
  await page.mouse.wheel(-15, 69);

  // Scroll wheel by X:0, Y:540
  await page.mouse.wheel(0, 540);

  // Scroll wheel by X:-3, Y:16
  await page.mouse.wheel(-3, 16);

  // Scroll wheel by X:0, Y:529
  await page.mouse.wheel(0, 529);

  // Scroll wheel by X:-15, Y:79
  await page.mouse.wheel(-15, 79);

  // Scroll wheel by X:0, Y:450
  await page.mouse.wheel(0, 450);

  // Scroll wheel by X:-9, Y:32
  await page.mouse.wheel(-9, 32);

  // Scroll wheel by X:0, Y:225
  await page.mouse.wheel(0, 225);

  // Scroll wheel by X:-13, Y:88
  await page.mouse.wheel(-13, 88);

  // Scroll wheel by X:0, Y:642
  await page.mouse.wheel(0, 642);

  // Scroll wheel by X:-17, Y:30
  await page.mouse.wheel(-17, 30);

  // Scroll wheel by X:0, Y:114
  await page.mouse.wheel(0, 114);

  // Scroll wheel by X:-14, Y:65
  await page.mouse.wheel(-14, 65);

  // Scroll wheel by X:0, Y:332
  await page.mouse.wheel(0, 332);

  // Scroll wheel by X:-15, Y:107
  await page.mouse.wheel(-15, 107);

  // Scroll wheel by X:0, Y:871
  await page.mouse.wheel(0, 871);

  // Scroll wheel by X:0, Y:-1
  await page.mouse.wheel(0, -1);

  // Scroll wheel by X:18, Y:-73
  await page.mouse.wheel(18, -73);

  // Scroll wheel by X:0, Y:-243
  await page.mouse.wheel(0, -243);

  // Scroll wheel by X:2, Y:-2
  await page.mouse.wheel(2, -2);

  // Scroll wheel by X:0, Y:-2
  await page.mouse.wheel(0, -2);

  // Scroll wheel by X:17, Y:-32
  await page.mouse.wheel(17, -32);

  // Scroll wheel by X:0, Y:-3
  await page.mouse.wheel(0, -3);

  // Scroll wheel by X:5, Y:-6
  await page.mouse.wheel(5, -6);

  // Scroll wheel by X:0, Y:-4
  await page.mouse.wheel(0, -4);

  // Scroll wheel by X:2, Y:-2
  await page.mouse.wheel(2, -2);

  // Scroll wheel by X:0, Y:-5
  await page.mouse.wheel(0, -5);

  // Scroll wheel by X:-2, Y:0
  await page.mouse.wheel(-2, 0);

  // Scroll wheel by X:0, Y:5
  await page.mouse.wheel(0, 5);

  // Scroll wheel by X:-57, Y:138
  await page.mouse.wheel(-57, 138);

  // Scroll wheel by X:0, Y:3
  await page.mouse.wheel(0, 3);

  // Scroll wheel by X:12, Y:32
  await page.mouse.wheel(12, 32);

  // Scroll wheel by X:0, Y:26
  await page.mouse.wheel(0, 26);

  // Scroll wheel by X:-21, Y:100
  await page.mouse.wheel(-21, 100);

  // Scroll wheel by X:0, Y:309
  await page.mouse.wheel(0, 309);

  // Scroll wheel by X:-1, Y:1
  await page.mouse.wheel(-1, 1);

  // Scroll wheel by X:0, Y:3
  await page.mouse.wheel(0, 3);

  // Scroll wheel by X:-7, Y:18
  await page.mouse.wheel(-7, 18);

  // Scroll wheel by X:0, Y:4
  await page.mouse.wheel(0, 4);

  // Scroll wheel by X:-1, Y:5
  await page.mouse.wheel(-1, 5);

  // Scroll wheel by X:0, Y:5
  await page.mouse.wheel(0, 5);

  // Scroll wheel by X:-4, Y:10
  await page.mouse.wheel(-4, 10);

  // Scroll wheel by X:0, Y:11
  await page.mouse.wheel(0, 11);

  // Scroll wheel by X:-39, Y:100
  await page.mouse.wheel(-39, 100);

  // Scroll wheel by X:0, Y:1
  await page.mouse.wheel(0, 1);

  // Scroll wheel by X:-1, Y:1
  await page.mouse.wheel(-1, 1);

  // Scroll wheel by X:-1, Y:0
  await page.mouse.wheel(-1, 0);

  // Fill "-1" on <select> #amidDDN416
  await Promise.all([
    page.selectOption("#amidDDN416", "-1"),
    page.waitForNavigation(),
  ]);

  // Scroll wheel by X:0, Y:1
  await page.mouse.wheel(0, 1);

  // Scroll wheel by X:-19, Y:39
  await page.mouse.wheel(-19, 39);

  // Scroll wheel by X:0, Y:4
  await page.mouse.wheel(0, 4);

  // Scroll wheel by X:-1, Y:6
  await page.mouse.wheel(-1, 6);

  // Scroll wheel by X:0, Y:7
  await page.mouse.wheel(0, 7);

  // Scroll wheel by X:-18, Y:45
  await page.mouse.wheel(-18, 45);

  // Scroll wheel by X:0, Y:110
  await page.mouse.wheel(0, 110);

  // Click on <td> "December 18, 2022 Minutes..."
  await page.click(".pageStyles > table:nth-child(5) td:nth-child(2)");

  // Click on <a> "December 18, 2022 Minutes..."
  await page.click('[href="Archive.aspx?ADID=7395"]');
});
