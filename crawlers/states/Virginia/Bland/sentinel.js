import { test, expect } from '@playwright/test';

test('Written with DeploySentinel Recorder', async ({ page }) => {
  // Load "https://www.blandcountyva.gov/page/agendas-and-minutes/"
  await page.goto('https://www.blandcountyva.gov/page/agendas-and-minutes/');

  // Resize window to 1920 x 887
  await page.setViewportSize({ width: 1920, height: 887 });

  // Click on <a> "MINUTES"
  await page.click('[href="/uploads/docs/BOS%20Minutes%2001022024.pdf"]');
});