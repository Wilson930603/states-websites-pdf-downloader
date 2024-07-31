import { test, expect } from '@playwright/test';

test("Written with DeploySentinel Recorder", async ({ page }) => {
    // Load "https://lunenburgva.gov/government/planning_commission/agendas___minutes.php"
    await page.goto('https://lunenburgva.gov/government/planning_commission/agendas___minutes.php');
  
    // Resize window to 1920 x 969
    await page.setViewportSize({ width: 1920, height: 969 });
  
    // Scroll wheel by X:0, Y:384
    await page.mouse.wheel(0, 384);
  
    // Click on <a> "Minutes"
    await page.click('[href="1.4.24 PC Mtg Minutes.pdf"]');
  
});