import { test, expect } from "@playwright/test";

test("Written with DeploySentinel Recorder", async ({ page }) => {
  // Load "https://www.pittsylvaniacountyva.gov/government/boards-and-commissions/planning-commission/-toggle-allpast"
  await page.goto(
    "https://www.pittsylvaniacountyva.gov/government/boards-and-commissions/planning-commission/-toggle-allpast"
  );

  // Resize window to 1920 x 970
  await page.setViewportSize({ width: 1920, height: 970 });

  // Scroll wheel by X:0, Y:176
  await page.mouse.wheel(0, 176);

  // Click on <a> "09052023 PC Minutes "
  await page.click(
    '[href="/home/showpublisheddocument/4194/638320207908630000"]'
  );

  / Load "https://weblink.pittgov.net/WebLink/Browse.aspx?id=446345&dbid=0&repo=PittGovDocs"
  await page.goto('https://weblink.pittgov.net/WebLink/Browse.aspx?id=446345&dbid=0&repo=PittGovDocs');

  // Resize window to 1920 x 970
  await page.setViewportSize({ width: 1920, height: 970 });

  // Click on <a> "PC Minutes 01 05 2021"
  await page.click('[href="/WebLink/DocView.aspx?id=446346&dbid=0&repo=PittGovDocs"]');

});
