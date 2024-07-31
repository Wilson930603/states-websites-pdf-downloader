import { test, expect } from "@playwright/test";

test("Written with DeploySentinel Recorder", async ({ page }) => {
  // Load "https://goochlandcountyva.iqm2.com/Citizens/Calendar.aspx?From=1%2f1%2f2021&To=12%2f31%2f9999"
  await page.goto(
    "https://goochlandcountyva.iqm2.com/Citizens/Calendar.aspx?From=1%2f1%2f2021&To=12%2f31%2f9999"
  );

  // Resize window to 1920 x 921
  await page.setViewportSize({ width: 1920, height: 921 });

  // Click on <a> "Summary Minutes"
  await page.click('[href="FileOpen.aspx?Type=15&ID=1268&Inline=True"]');
});
