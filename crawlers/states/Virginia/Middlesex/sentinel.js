import { test, expect } from '@playwright/test';

test("Written with DeploySentinel Recorder", async ({ page }) => {
    // Load "https://www.co.middlesex.va.us/AgendaCenter/Search/?term=&CIDs=8,2,&startDate=&endDate=&dateRange=&dateSelector="
    await page.goto('https://www.co.middlesex.va.us/AgendaCenter/Search/?term=&CIDs=8,2,&startDate=&endDate=&dateRange=&dateSelector=');
  
    // Resize window to 1920 x 970
    await page.setViewportSize({ width: 1920, height: 970 });
  
    // Click on <a> "View More"
    await page.click('#btnViewMore8');
  
    // Click on <a> "2021"
    await page.click('#anchYearDD38');
  
    // Click on <a> [href="/AgendaCenter/ViewFile/Minutes/_06212021-265"]
    await page.click('[href="/AgendaCenter/ViewFile/Minutes/_06212021-265"]');
  
    // Click on <a> [href="/AgendaCenter/ViewFile/Minutes/_03142024-517"]
    await page.click('[href="/AgendaCenter/ViewFile/Minutes/_03142024-517"]');
  
    // Click on <a> "View More"
    await page.click('#btnViewMore2');
  
    // Click on <a> "2021"
    await page.click('#anchYearDD32');
  
    // Click on <a> [href="/AgendaCenter/ViewFile/Minutes/_10142021-290"]
    await page.click('[href="/AgendaCenter/ViewFile/Minutes/_10142021-290"]');
});