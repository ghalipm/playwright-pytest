from playwright.sync_api import Page


# # Option1: knowing if Ads closed, it goes to Test Cases
# def test_automation_exercise(page: Page):
#     page.goto("https://automationexercise.com")
#     assert "Automation Exercise" in page.title()
#     page.clear_cookies()
#     page.locator("text=Test Cases").nth(1).click(delay=2000)
#     if page.url.__contains__("#google_vignette"):
#         # ads_frame = page.frame_locator("#aswift_5")
#         # ads_frame.get_by_label("aria-label=Close ad").click()
#         # # ads_frame.get_by_role("button").click()
#         page.wait_for_timeout(3000)
#         page.goto('https://automationexercise.com/test_cases')
#     assert "Test" in page.title()

# Option2: if http request contains "googleads",
#          just abort the request, so no chance for Ads.
#          working version without triggering ads =====

def test_automation_exercise(page_with_ad_blocking: Page):
    # see page_with_ad_blocking fixture in Conftest.py file
    page = page_with_ad_blocking
    # Navigate to the main page
    page.goto("https://automationexercise.com")

    # Verify the page title
    assert "Automation Exercise" in page.title()

    # Clear cookies to ensure a consistent state
    page.context.clear_cookies()

    # Click on the 'Test Cases' link
    test_cases_link = page.locator("text=Test Cases").nth(1)
    test_cases_link.click()
    page.wait_for_timeout(4000)

    # Ensure the title of the page contains 'Test Cases'
    assert "Test Cases" in page.title()
