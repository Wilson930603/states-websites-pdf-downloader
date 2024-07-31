import { test, expect } from "@playwright/test";

test("Written with DeploySentinel Recorder", async ({ page }) => {
  // Load "https://www.smythcounty.org/government/agendas___minutes_/planning_commission_agendas___minutes.php"
  await page.goto(
    "https://www.smythcounty.org/government/agendas___minutes_/planning_commission_agendas___minutes.php"
  );

  // Resize window to 1920 x 970
  await page.setViewportSize({ width: 1920, height: 970 });

  // Click on <a> "Minutes"
  await page.click(
    '[href="Document Centers/Agendas & Minutes/Planning Commission Agendas & Minutes/Minutes/February 22 2024 Adopted Planning Commission Minutes.pdf"]'
  );
});
