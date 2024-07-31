import { test, expect } from '@playwright/test';

test("Written with DeploySentinel Recorder", async ({ page }) => {
  // Load "https://kingandqueenco.net/planning-commission-meetings/"
  await page.goto("https://kingandqueenco.net/planning-commission-meetings/");

  // Resize window to 1920 x 970
  await page.setViewportSize({ width: 1920, height: 970 });

  // Click on <a> "Minutes"
  await page.click(
    '[href="https://p63d74.p3cdn1.secureserver.net/wp-content/uploads/2024/04/01.02.2024-PC.pdf"]'
  );

  
});