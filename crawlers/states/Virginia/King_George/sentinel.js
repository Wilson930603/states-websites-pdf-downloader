import { test, expect } from '@playwright/test';

test("Written with DeploySentinel Recorder", async ({ page }) => {  
    // Load "https://www.kinggeorgecountyva.gov/AgendaCenter/Search/?term=&CIDs=3,5,&startDate=01/01/2020&endDate=&dateRange=&dateSelector="
    await page.goto('https://www.kinggeorgecountyva.gov/AgendaCenter/Search/?term=&CIDs=3,5,&startDate=01/01/2020&endDate=&dateRange=&dateSelector=');
  
    // Resize window to 1920 x 970
    await page.setViewportSize({ width: 1920, height: 970 });
  
    // Scroll wheel by X:0, Y:496
    await page.mouse.wheel(0, 496);
  
    // Click on <a> "View More"
    await page.click('#btnViewMore3');
  
    // Click on <a> "2021"
    await page.click('#anchYearDD33');
  
    // Click on <a> [href="/AgendaCenter/ViewFile/Minutes/_08242021-656"]
    await page.click('[href="/AgendaCenter/ViewFile/Minutes/_08242021-656"]');
  
    // Click on <a> [href="/AgendaCenter/ViewFile/Minutes/_01092024-1063"]
    await page.click('[href="/AgendaCenter/ViewFile/Minutes/_01092024-1063"]');
  
    // Click on <a> "View More"
    await page.click('#btnViewMore5');
  
    // Click on <a> "2021"
    await page.click('#anchYearDD35');
  
    // Click on <a> [href="/AgendaCenter/ViewFile/Minutes/_12142021-685"]
    await page.click('[href="/AgendaCenter/ViewFile/Minutes/_12142021-685"]');
});