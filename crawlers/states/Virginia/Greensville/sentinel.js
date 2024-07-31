import { test, expect } from '@playwright/test';


test("Written with DeploySentinel Recorder", async ({ page }) => {
  // Load "https://www.greensvillecountyva.gov/boards___commissions/board_of_supervisors/agendas___minutes/planning_commission.php#outer-1188"
  await page.goto('https://www.greensvillecountyva.gov/boards___commissions/board_of_supervisors/agendas___minutes/planning_commission.php#outer-1188');

  // Click on <h3> "2024 6 documents"
  await Promise.all([
    page.click('.outer-cat:nth-child(1) > .docs-toggle'),
    page.waitForNavigation()
  ]);

  // Click on <h4> "Minutes No documents"
  await Promise.all([
    page.click('.outer-1322 > .inner-cat:nth-child(5) > .docs-toggle'),
    page.waitForNavigation()
  ]);

  // Click on <h3> "2023 10 documents"
  await Promise.all([
    page.click('.outer-cat:nth-child(2) > .docs-toggle'),
    page.waitForNavigation()
  ]);

  // Click on <h4> "Minutes 2 documents"
  await Promise.all([
    page.click('.outer-1188 > .inner-cat:nth-child(5) > .docs-toggle'),
    page.waitForNavigation()
  ]);

  // Click on <a> "March 14, 2023"
  await page.click('[href="Documents Center/Agenda & Minutes/Planning Commission/2023/Minutes/Planning Minutes - 03142023.pdf"]');

  // Scroll wheel by X:0, Y:192
  await page.mouse.wheel(0, 192);

  // Click on <h3> "2022 20 documents"
  await Promise.all([
    page.click('.outer-cat:nth-child(3) > .docs-toggle'),
    page.waitForNavigation()
  ]);

  // Click on <h4> "Minutes 10 documents"
  await Promise.all([
    page.click('.outer-988 > .inner-cat:nth-child(5) > .docs-toggle'),
    page.waitForNavigation()
  ]);

  // Click on <a> "December 13, 2022"
  await page.click('[href="Documents Center/Agenda & Minutes/Planning Commission/2023/Minutes/Planning Minutes 12132022.pdf"]');

  // Scroll wheel by X:0, Y:240
  await page.mouse.wheel(0, 240);

  // Scroll wheel by X:0, Y:-272
  await page.mouse.wheel(0, -272);

  // Scroll wheel by X:0, Y:336
  await page.mouse.wheel(0, 336);

  // Click on <h3> "2021 10 documents"
  await Promise.all([
    page.click('.outer-cat:nth-child(4) > .docs-toggle'),
    page.waitForNavigation()
  ]);

  // Scroll wheel by X:0, Y:-192
  await page.mouse.wheel(0, -192);

  // Click on <h4> "Minutes 5 documents"
  await Promise.all([
    page.click('.outer-182 > .inner-cat:nth-child(5) > .docs-toggle'),
    page.waitForNavigation()
  ]);

  // Click on <a> "April 13, 2021"
  await page.click('[href="Documents Center/Agenda & Minutes/Planning Commission/2021/Minutes/Minutes_04-13-2021.pdf"]');

})