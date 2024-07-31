import { test, expect } from "@playwright/test";

test("Written with DeploySentinel Recorder", async ({ page }) => {

    // Load "https://tazewellcountyva.org/government/boards-and-commissions/planning-commission/"
    await page.goto('https://tazewellcountyva.org/government/boards-and-commissions/planning-commission/');
  
    // Resize window to 1920 x 970
    await page.setViewportSize({ width: 1920, height: 970 });
  
    // Click on <a> "(Minutes)"
    await page.click('[href="http://tazewellcountyva.org/wp-content/uploads/2024/04/March-14-2024-Minutes.pdf"]');
  
});
