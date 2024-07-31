import { test, expect } from "@playwright/test";

test("Written with DeploySentinel Recorder", async ({ page }) => {

    // Load "https://www.rockinghamcountyva.gov/AgendaCenter/Search/?term=&CIDs=15,2,&startDate=&endDate=&dateRange=&dateSelector="
    await page.goto('https://www.rockinghamcountyva.gov/AgendaCenter/Search/?term=&CIDs=15,2,&startDate=&endDate=&dateRange=&dateSelector=');
  
    // Resize window to 1920 x 970
    await page.setViewportSize({ width: 1920, height: 970 });
  
    // Scroll wheel by X:0, Y:400
    await page.mouse.wheel(0, 400);
  
    // Click on <a> "This is the agenda for th..."
    await page.click('p > [href="/AgendaCenter/ViewFile/Agenda/_10122022-695"]');
  
    // Scroll wheel by X:0, Y:96
    await page.mouse.wheel(0, 96);
  
    // Scroll wheel by X:0, Y:-320
    await page.mouse.wheel(0, -320);
  
    // Click on <a> "View More"
    await page.click('#btnViewMore15');
  
    // Click on <a> "View More"
    await page.click('#btnViewMore2');
  
    // Click on <a> "2021"
    await page.click('#anchYearDD32');
  
    // Scroll wheel by X:0, Y:176
    await page.mouse.wheel(0, 176);
  
    // Click on <a> "This is the meeting packe..."
    await page.click('p > [href="/AgendaCenter/ViewFile/Agenda/_08032021-621"]');
  
    // Click on <a> "2024"
    await page.click('#a02');
  
    // Click on <a> "This is the agenda packet..."
    await page.click('p > [href="/AgendaCenter/ViewFile/Agenda/_04022024-802"]');
  
});
