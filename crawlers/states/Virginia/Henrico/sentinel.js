import { test, expect } from '@playwright/test';


test("Written with DeploySentinel Recorder", async ({ page }) => {
  // Load "https://henrico.gov/planning/minutes/minutes-2020-2029/"
  await page.goto("https://henrico.gov/planning/minutes/minutes-2020-2029/");

  // Resize window to 1920 x 969
  await page.setViewportSize({ width: 1920, height: 969 });

  // Click on <a> "January 11, 2024"
  await Promise.all([
    page.click(
      '[href="https://henrico.gov/pdfs/planning/minutes/rezone/jan24rez.pdf"]'
    ),
    page.waitForNavigation(),
  ]);

  // Click on <a> "January 25, 2024"
  await Promise.all([
    page.click(
      '[href="https://henrico.gov/pdfs/planning/minutes/bza/jan24bza.pdf"]'
    ),
    page.waitForNavigation(),
  ]);

  
});