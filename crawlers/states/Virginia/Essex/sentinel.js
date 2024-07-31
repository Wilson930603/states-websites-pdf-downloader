import { test, expect } from "@playwright/test";

test("Written with DeploySentinel Recorder", async ({ page }) => {
  // Load "https://www.essex-virginia.org/meetings/recent?field_smart_date_value_2=2021-01-01&field_smart_date_end_value_2=2027-12-12&combine=&department=All&boards-commissions=2282"
  await page.goto(
    "https://www.essex-virginia.org/meetings/recent?field_smart_date_value_2=2021-01-01&field_smart_date_end_value_2=2027-12-12&combine=&department=All&boards-commissions=2282"
  );

  // Resize window to 1920 x 970
  await page.setViewportSize({ width: 1920, height: 970 });

  // Click on <a> [href="/media/5386"]
  await page.click('[href="/media/5386"]');
});
