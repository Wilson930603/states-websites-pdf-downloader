import { test, expect } from '@playwright/test';

test('Written with DeploySentinel Recorder', async ({ page }) => {
  // Load "https://www.charlottecountyva.gov/departments/planning___zoning/agendas___minutes.php"
  await page.goto('https://www.charlottecountyva.gov/departments/planning___zoning/agendas___minutes.php');

  // Resize window to 1920 x 887
  await page.setViewportSize({ width: 1920, height: 887 });

  // Click on <a> "Minutes"
  await page.click('[href="Document_Center/Departments/Planning & Zoning/Agenda & Minutes/2024/Minutes/2024-04-18 Minutes.pdf"]');
});