import { test, expect } from "@playwright/test";

test("Written with DeploySentinel Recorder", async ({ page }) => {
  // Load "https://www.nelsoncounty-va.gov/departments-offices/planning-zoning/planning-commission/"
  await page.goto(
    "https://www.nelsoncounty-va.gov/departments-offices/planning-zoning/planning-commission/"
  );

  // Resize window to 1920 x 970
  await page.setViewportSize({ width: 1920, height: 970 });

  // Scroll wheel by X:0, Y:352
  await page.mouse.wheel(0, 352);

  // Click on <a> "Minutes – January 24, 202..."
  await page.click(
    '[href="https://www.nelsoncounty-va.gov/wp-content/uploads/2024/04/Minutes_PC-Meeting_2024-01-24final.pdf"]'
  );

  // Click on <a> "Minutes – October 25, 202..."
  await page.click(
    '[href="https://www.nelsoncounty-va.gov/wp-content/uploads/2024/04/Minutes_PC-Meeting_2023-10-25final.pdf"]'
  );

  // Scroll wheel by X:0, Y:912
  await page.mouse.wheel(0, 912);

  // Click on <a> "June 22, 2022"
  await page.click(
    '[href="https://www.nelsoncounty-va.gov/wp-content/uploads/2023/04/2022-06-22.pdf"]'
  );

  // Click on <a> "November 17, 2021"
  await page.click(
    '[href="https://www.nelsoncounty-va.gov/wp-content/uploads/2023/04/2021-11-17.pdf"]'
  );
});
