import { test, expect } from "@playwright/test";

test("Written with DeploySentinel Recorder", async ({ page }) => {
  const page = await browser.newPage();

  // Load "https://www.fairfaxcounty.gov/planningcommission/minutes-home"
  await page.goto('https://www.fairfaxcounty.gov/planningcommission/minutes-home');

  // Resize window to 1920 x 921
  await page.setViewportSize({ width: 1920, height: 921 });

  // Scroll wheel by X:0, Y:448
  await page.mouse.wheel(0, 448);

  // Click on <a> "2024"
  await Promise.all([
    page.click('[href="/planningcommission/meeting-minutes-2024"]'),
    page.waitForNavigation()
  ]);

  // Click on <a> "January 10, 2024"
  await Promise.all([
    page.click('[href="https://www.fairfaxcounty.gov/planningcommission/sites/planningcommission/files/Assets/Documents/PDF/2024%20minutes/minutes011024.pdf"]'),
    page.waitForNavigation()
  ]);  
});
