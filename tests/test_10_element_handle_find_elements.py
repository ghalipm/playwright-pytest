from playwright.sync_api import Page, ElementHandle


def test_find_elements(page_with_ad_blocking: Page):
    # see page_with_ad_blocking fixture in conftest.py file
    page = page_with_ad_blocking
    # Navigate to the main page
    page.goto("https://automationexercise.com")
    page.wait_for_timeout(2000)
    # # Clear cookies to ensure a consistent state
    # page.context.clear_cookies()

    # Click on the 'Test Cases' link
    test_cases_link = page.locator("text=Test Cases").nth(1)
    test_cases_link.click()
    page.wait_for_timeout(3000)

    # Ensure the title of the page contains 'Test Cases'
    assert "Test Cases" in page.title()
    page.wait_for_timeout(6000)

    title_links: list[ElementHandle] = page.query_selector_all("//h4/a/u")
    link_hrefs: list[ElementHandle] = page.query_selector_all("//h4/a")
    print('\n', '------------ Link Titles ---------------:  ')
    for title_link in title_links:
        print(title_link.text_content())

    print('\n', '------------ Link hrefs ---------------:  ')
    for link_href in link_hrefs:
        print(link_href)
