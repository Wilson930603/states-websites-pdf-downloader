import { test, expect } from "@playwright/test";

test("Written with DeploySentinel Recorder", async ({ page }) => {
  const page = await browser.newPage();

  // Load "https://meetings.municode.com/PublishPage?cid=WYTHEVILVA&ppid=277ff12f-1d9e-4fe6-8d83-2a4a5bf2751a&p=1"
  await page.goto(
    "https://meetings.municode.com/PublishPage?cid=WYTHEVILVA&ppid=277ff12f-1d9e-4fe6-8d83-2a4a5bf2751a&p=1"
  );

  // Resize window to 1920 x 970
  await page.setViewportSize({ width: 1920, height: 970 });

  // Click on <a> [href="https://meetings.municode.com/d/f?u=https://mccmeetings.blob.core.usgovcloudapi.net/wythevilva-pubu/MEET-Minutes-80080b2e195f4750a1395fab75bf1145.pdf&n=Minutes-Wytheville%20Planning%20Commission%20Meeting-February 8, 2024 6.00 PM.pdf"]
  await page.click(
    '[href="https://meetings.municode.com/d/f?u=https://mccmeetings.blob.core.usgovcloudapi.net/wythevilva-pubu/MEET-Minutes-80080b2e195f4750a1395fab75bf1145.pdf&n=Minutes-Wytheville%20Planning%20Commission%20Meeting-February 8, 2024 6.00 PM.pdf"]'
  );

  // Click on <a> ">"
  await Promise.all([
    page.click(
      "[href=\"javascript:window.open('https://meetings.municode.com/PublishPage?cid=WYTHEVILVA&ppid=277ff12f-1d9e-4fe6-8d83-2a4a5bf2751a&p=' + (Number(document.getElementById('agendapal.page.dropbox').value) == 3 ? 3 : Number(document.getElementById('agendapal.page.dropbox').value) + 1), '_self');\"]"
    ),
    page.waitForNavigation(),
  ]);

  // Click on <a> [href="https://meetings.municode.com/d/f?u=https://mccmeetings.blob.core.usgovcloudapi.net/wythevilva-pubu/MEET-Minutes-f86d695c7c294e6db3b8eaff4081d88f.pdf&n=Minutes-Wytheville%20Planning%20Commission%20Meeting-June 8, 2023 6.00 PM.pdf"]
  await page.click(
    '[href="https://meetings.municode.com/d/f?u=https://mccmeetings.blob.core.usgovcloudapi.net/wythevilva-pubu/MEET-Minutes-f86d695c7c294e6db3b8eaff4081d88f.pdf&n=Minutes-Wytheville%20Planning%20Commission%20Meeting-June 8, 2023 6.00 PM.pdf"]'
  );

  // Click on <a> ">"
  await Promise.all([
    page.click(
      "[href=\"javascript:window.open('https://meetings.municode.com/PublishPage?cid=WYTHEVILVA&ppid=277ff12f-1d9e-4fe6-8d83-2a4a5bf2751a&p=' + (Number(document.getElementById('agendapal.page.dropbox').value) == 3 ? 3 : Number(document.getElementById('agendapal.page.dropbox').value) + 1), '_self');\"]"
    ),
    page.waitForNavigation(),
  ]);

  // Click on <a> [href="https://meetings.municode.com/d/f?u=https://mccmeetings.blob.core.usgovcloudapi.net/wythevilva-pubu/MEET-Minutes-755c4e3dd14b4c9d833cf177f998b81e.pdf&n=Minutes-Wytheville%20Planning%20Commission-September 8, 2022 6.00 PM.pdf"]
  await page.click(
    '[href="https://meetings.municode.com/d/f?u=https://mccmeetings.blob.core.usgovcloudapi.net/wythevilva-pubu/MEET-Minutes-755c4e3dd14b4c9d833cf177f998b81e.pdf&n=Minutes-Wytheville%20Planning%20Commission-September 8, 2022 6.00 PM.pdf"]'
  );

  // Click on <a> ">"
  await Promise.all([
    page.click(
      "[href=\"javascript:window.open('https://meetings.municode.com/PublishPage?cid=WYTHEVILVA&ppid=277ff12f-1d9e-4fe6-8d83-2a4a5bf2751a&p=' + (Number(document.getElementById('agendapal.page.dropbox').value) == 3 ? 3 : Number(document.getElementById('agendapal.page.dropbox').value) + 1), '_self');\"]"
    ),
    page.waitForNavigation(),
  ]);

  // Resize window to 1295 x 970
  await page.setViewportSize({ width: 1295, height: 970 });
});
