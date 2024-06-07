from playwright.sync_api import Page


def test_playwright_page(page: Page):
    page.goto("https://playwright.dev/python/")
    print(page.title())
    assert "Playwright" in page.title()
    page.get_by_text("Get started").click()
    assert "Installation" in page.title()
