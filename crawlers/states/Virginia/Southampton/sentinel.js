import { test, expect } from "@playwright/test";

test("Written with DeploySentinel Recorder", async ({ page }) => {
  // Load "https://www.southamptoncounty.org/departments/planning/archived_planning_commission_minutes.php"
  await page.goto(
    "https://www.southamptoncounty.org/departments/planning/archived_planning_commission_minutes.php"
  );

  // Resize window to 1920 x 970
  await page.setViewportSize({ width: 1920, height: 970 });

  // Click on <a> "PC Minutes 2024"
  await Promise.all([
    page.click('[href="departments/planning/pc_minutes_2024.php"]'),
    page.waitForNavigation(),
  ]);

  // Click on <a> "January 11, 2024"
  await Promise.all([
    page.click(
      '[href="PC Minutes/2024/Planning Commission  (1-11-2024) FINAL.pdf"]'
    ),
    page.waitForNavigation(),
  ]);

  // Click on <a> "PC Minutes 2023"
  await Promise.all([
    page.click('[href="departments/planning/pc_minutes_2023.php"]'),
    page.waitForNavigation(),
  ]);

  // Click on <a> "January 12, 2023"
  await Promise.all([
    page.click('[href="PC Minutes/2023/01122023.pdf"]'),
    page.waitForNavigation(),
  ]);

  // Click on <a> "PC Minutes 2022"
  await Promise.all([
    page.click('[href="departments/planning/pc_minutes_2022.php"]'),
    page.waitForNavigation(),
  ]);

  // Click on <a> "Thursday, January 13, 202..."
  await Promise.all([
    page.click('[href="Planning Commission January2022.pdf"]'),
    page.waitForNavigation(),
  ]);

  // Click on <a> "PC Minutes 2021"
  await Promise.all([
    page.click('[href="departments/planning/pc_minutes_2021.php"]'),
    page.waitForNavigation(),
  ]);

  // Click on <a> "Thursday, January 14, 202..."
  await page.click(
    '[href="Planning Commission Agendas/2021/Feb 2021/DRAFT Jan 2021 PC minutes.pdf"]'
  );
});
