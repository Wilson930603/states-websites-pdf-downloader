import { test, expect } from "@playwright/test";

test("Written with DeploySentinel Recorder", async ({ page }) => {
  // Load "https://richmondva.legistar.com/Calendar.aspx"
  await page.goto("https://richmondva.legistar.com/Calendar.aspx");

  // Resize window to 1920 x 970
  await page.setViewportSize({ width: 1920, height: 970 });

  // Click on <input> #ctl00_ContentPlaceHolder1_lstYears_Input
  await page.click("#ctl00_ContentPlaceHolder1_lstYears_Input");

  // Click on <li> "All Years"
  await page.click(".rcbHovered");

  // Click on <input> #ctl00_ContentPlaceHolder1_lstBodies_Input
  await page.click("#ctl00_ContentPlaceHolder1_lstBodies_Input");

  // Click on <li> "Planning Commission"
  await page.click(".rcbHovered:nth-child(13)");

  // Scroll wheel by X:0, Y:832
  await page.mouse.wheel(0, 832);

  // Click on <td> " Action Summary"
  await page.click(
    "#ctl00_ContentPlaceHolder1_gridCalendar_ctl00__18 > td:nth-child(9)"
  );

  // Click on <a> "Action Summary"
  await page.click(
    "#ctl00_ContentPlaceHolder1_gridCalendar_ctl00_ctl40_hypMinutes"
  );
});
