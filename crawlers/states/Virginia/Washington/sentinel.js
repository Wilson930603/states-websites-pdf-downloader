import { test, expect } from "@playwright/test";

test("Written with DeploySentinel Recorder", async ({ page }) => {
  // Load "https://washingtoncountyva.iqm2.com/Citizens/Calendar.aspx?From=1%2f1%2f2021&To=12%2f31%2f9999"
  await page.goto(
    "https://washingtoncountyva.iqm2.com/Citizens/Calendar.aspx?From=1%2f1%2f2021&To=12%2f31%2f9999"
  );

  // Resize window to 1920 x 970
  await page.setViewportSize({ width: 1920, height: 970 });

  // Click on <a> "Minutes"
  await page.click('[href="FileOpen.aspx?Type=12&ID=2341&Inline=True"]');
});
