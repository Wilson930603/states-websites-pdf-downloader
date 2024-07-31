import { test, expect } from '@playwright/test';

test('Written with DeploySentinel Recorder', async ({ page }) => {
  // Load "https://www.co.campbell.va.us/AgendaCenter/Search/?term=&CIDs=12,6,&startDate=&endDate=&dateRange=&dateSelector="
  await page.goto('https://www.co.campbell.va.us/AgendaCenter/Search/?term=&CIDs=12,6,&startDate=&endDate=&dateRange=&dateSelector=');

  // Resize window to 1920 x 887
  await page.setViewportSize({ width: 1920, height: 887 });

  // Click on <a> [href="/AgendaCenter/ViewFile/Minutes/_04222024-452"]
  await page.click('[href="/AgendaCenter/ViewFile/Minutes/_04222024-452"]');
});