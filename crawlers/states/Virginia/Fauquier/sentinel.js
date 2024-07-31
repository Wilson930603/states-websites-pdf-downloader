import { test, expect } from '@playwright/test';

test('Written with DeploySentinel Recorder', async ({ page }) => {
    // Load "https://fauquier-va.granicus.com/ViewPublisher.php?view_id=6"
    await page.goto('https://fauquier-va.granicus.com/ViewPublisher.php?view_id=6');
  
    // Resize window to 1920 x 970
    await page.setViewportSize({ width: 1920, height: 970 });
  
    // Click on <div> "Planning Commission"
    await page.click('.CollapsiblePanelTab');
  
    // Click on <a> "Minutes"
    await page.click('[href="//fauquier-va.granicus.com/MinutesViewer.php?view_id=6&clip_id=1110&doc_id=30a0d1d8-32fd-11ef-81ef-005056a89546"]');
  
    // Click on <li> "2023"
    await page.click('.TabbedPanelsTabHover');
  
    // Click on <a> "Minutes"
    await page.click('[href="//fauquier-va.granicus.com/MinutesViewer.php?view_id=6&clip_id=1071&doc_id=9e066a02-b959-11ee-8fe8-0050569183fa"]');
  
    
});