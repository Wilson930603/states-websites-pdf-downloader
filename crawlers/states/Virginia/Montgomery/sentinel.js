import { test, expect } from "@playwright/test";

test("Written with DeploySentinel Recorder", async ({ page }) => {

  const browser = await playwright['chromium'].launch({
    // headless: false, slowMo: 100, // Uncomment to visualize test
  });
  const page = await browser.newPage();

  // Load "https://montva.com/1/government/meeting-agendas-minutes"
  await page.goto('https://montva.com/1/government/meeting-agendas-minutes');

    // Collect 2023, 2022, and 2021 Planning Commission minutes  
    // Load "https://weblink.montva.com/WebLink/Browse.aspx?id=802&dbid=4&repo=PIO"
    await page.goto('https://weblink.montva.com/WebLink/Browse.aspx?id=802&dbid=4&repo=PIO');
  
  
    // Click on <a> "2023"
    await Promise.all([
      page.click('[href="Browse.aspx?id=850&dbid=4&repo=PIO"]'),
      page.waitForNavigation()
    ]);
  
    // Click on <a> "Minutes"
    await Promise.all([
      page.click('[href="Browse.aspx?id=940&dbid=4&repo=PIO"]'),
      page.waitForNavigation()
    ]);
  
    // Click on <a> "01-11-2023, Planning Comm..."
    await page.click('[href="/WebLink/DocView.aspx?id=1561&dbid=4&repo=PIO"]');
  
    // Click on <a> "Planning Commission "
    await Promise.all([
      page.click('li:nth-child(4) > [href="javascript:void(0)"]'),
      page.waitForNavigation()
    ]);
  
    // Click on <a> "2022"
    await Promise.all([
      page.click('[href="Browse.aspx?id=1080&dbid=4&repo=PIO"]'),
      page.waitForNavigation()
    ]);
  
    // Click on <span> "Minutes"
    await page.click('.ui-datatable-odd > .GridColumnWidth:nth-child(2) > .ui-cell-data');
  
    // Click on <a> "Minutes"
    await Promise.all([
      page.click('[href="Browse.aspx?id=1085&dbid=4&repo=PIO"]'),
      page.waitForNavigation()
    ]);
  
    // Click on <a> "02-16-2022, Planning Comm..."
    await page.click('[href="/WebLink/DocView.aspx?id=1649&dbid=4&repo=PIO"]');
  
    // Click on <a> "Planning Commission "
    await Promise.all([
      page.click('li:nth-child(4) > [href="javascript:void(0)"]'),
      page.waitForNavigation()
    ]);
  
    // Click on <td> "2021"
    await page.click('.ui-datatable-odd:nth-child(2) > .GridColumnWidth:nth-child(2)');
  
    // Click on <a> "2021"
    await Promise.all([
      page.click('[href="Browse.aspx?id=1081&dbid=4&repo=PIO"]'),
      page.waitForNavigation()
    ]);
  
    // Click on <span> "Minutes"
    await page.click('.ui-datatable-odd > .GridColumnWidth:nth-child(2) > .ui-cell-data');
  
    // Click on <a> "Minutes"
    await Promise.all([
      page.click('[href="Browse.aspx?id=1087&dbid=4&repo=PIO"]'),
      page.waitForNavigation()
    ]);
  
    // Click on <a> "02-17-2021, Planning Comm..."
    await page.click('[href="/WebLink/DocView.aspx?id=1637&dbid=4&repo=PIO"]');
  
    // For 2024 onwards:
 
    
    // Load "https://go.boarddocs.com/va/montva/Board.nsf/Public#"
    await page.goto('https://go.boarddocs.com/va/montva/Board.nsf/Public#');

    // Resize window to 1920 x 970
    await page.setViewportSize({ width: 1920, height: 970 });

    // Click on <div> "Wednesday, July 17, 2024 ..."
    await page.click('.wrap-links');

    // Click on <a> "Wednesday, July 17, 2024 ..."
    await page.click('#D6YNME609775');

    // Click on <section> "2024"
    await page.click('#ui-id-17');

    // Click on <a> "Jun 12, 2024 (Wed) Montgo..."
    await page.click('#D5WJAG4AC9F8');

    // Click on <a> "View the Agenda"
    await page.click('#btn-view-agenda');

    // Click on <li> "B. Approval of Minutes Th..."
    await page.click('#D5WJAR4ACA06');

    // Click on <a> "1.10.24 Minutes - DRAFT P..."
    await page.click('[href="/va/montva/Board.nsf/files/D5XSCT6E01EB/$file/1.10.24%20Minutes%20-%20DRAFT%20PDF.pdf"]');

    // Click on <a> "3.13.24 Minutes - DRAFT P..."
    await page.click('[href="/va/montva/Board.nsf/files/D5XSCW6E0667/$file/3.13.24%20Minutes%20-%20DRAFT%20PDF.pdf"]');

    

})