import { test, expect } from '@playwright/test';

test("Written with DeploySentinel Recorder", async ({ page }) => {  
    // Load "http://www.leecova.org/AgendaandMinutes.htm"
    await page.goto('http://www.leecova.org/AgendaandMinutes.htm');
  
    // Resize window to 1920 x 969
    await page.setViewportSize({ width: 1920, height: 969 });
  
    // Click on <a> "May 28, 2024 Recessed Mee..."
    await page.click('[href="Minutes/2024/Minutes 5-28-24 Recessed Meeting.pdf"]');
});