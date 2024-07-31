import { test, expect } from '@playwright/test';

test("Written with DeploySentinel Recorder", async ({ page }) => {
    const page = await browser.newPage();
  
    // Load "https://pub-gloucesterva.escribemeetings.com/?Year=2024&Expanded=Planning%20Commission"
    await page.goto('https://pub-gloucesterva.escribemeetings.com/?Year=2024&Expanded=Planning%20Commission');
  
    // Resize window to 1920 x 921
    await page.setViewportSize({ width: 1920, height: 921 });
  
    // Scroll wheel by X:0, Y:1200
    await page.mouse.wheel(0, 1200);
  
    // Scroll wheel by X:0, Y:-80
    await page.mouse.wheel(0, -80);
  
    // Scroll wheel by X:0, Y:48
    await page.mouse.wheel(0, 48);
  
    // Click on <a> "PDF"
    await page.click('[href="FileStream.ashx?DocumentId=21087"]');
  
    
});