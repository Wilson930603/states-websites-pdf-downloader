import { test, expect } from "@playwright/test";

test("Written with DeploySentinel Recorder", async ({ page }) => {
  // Load "https://www.co.northumberland.va.us/meetings?date_filter%5Bvalue%5D%5Bmonth%5D=1&date_filter%5Bvalue%5D%5Bday%5D=1&date_filter%5Bvalue%5D%5Byear%5D=2021&date_filter_1%5Bvalue%5D%5Bmonth%5D=12&date_filter_1%5Bvalue%5D%5Bday%5D=31&date_filter_1%5Bvalue%5D%5Byear%5D=2027&field_microsite_tid_1=28"
  await page.goto(
    "https://www.co.northumberland.va.us/meetings?date_filter%5Bvalue%5D%5Bmonth%5D=1&date_filter%5Bvalue%5D%5Bday%5D=1&date_filter%5Bvalue%5D%5Byear%5D=2021&date_filter_1%5Bvalue%5D%5Bmonth%5D=12&date_filter_1%5Bvalue%5D%5Bday%5D=31&date_filter_1%5Bvalue%5D%5Byear%5D=2027&field_microsite_tid_1=28"
  );

  // Resize window to 1920 x 970
  await page.setViewportSize({ width: 1920, height: 970 });

  // Scroll wheel by X:0, Y:-464
  await page.mouse.wheel(0, -464);

  // Scroll wheel by X:0, Y:464
  await page.mouse.wheel(0, 464);

  // Click on <a> "Minutes"
  await page.click(
    '[href="https://www.co.northumberland.va.us/sites/default/files/fileattachments/planning_commission/meeting/4725/april_18_2024_minutes.pdf"]'
  );
});
