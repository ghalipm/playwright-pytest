from playwright.async_api import ElementHandle
from playwright.sync_api import Page


# The use of ElementHandle is discouraged,
# use Locator objects and web-first assertions instead.

def test_element_handle(page: Page):
    page.goto("https://practice.cydeo.com/forgot_password")
    home_link: ElementHandle = page.query_selector("a.nav-link")
    email_label: ElementHandle = page.query_selector("div label")
    assert home_link.is_visible()
    print(home_link.text_content())
    assert email_label.is_visible()
    print(email_label.text_content())
