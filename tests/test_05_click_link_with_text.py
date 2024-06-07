from playwright.sync_api import Page


def test_click_link_with_text(page: Page):
    page.goto("https://practice.cydeo.com/")
    page.wait_for_timeout(1000)
    page.click("text=Autocomplete")
    # page.click("//a[@href='/autocomplete']")
    page.wait_for_timeout(1000)
    print(page.title())
