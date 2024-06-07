from playwright.sync_api import Page


def test_navigation_options(page: Page):
    page.goto("https://practice.cydeo.com/")
    page.wait_for_timeout(1000)
    page.goto("https://google.com")
    page.wait_for_timeout(1000)

    # go back to : practice.cydeo.com
    page.go_back()
    page.waitForTimeout(1000)

    # go forward to next page: google.com
    page.go_forward()
    page.wait_for_timeout(1000)
    print(" URL: " + page.url)
    assert "Google" in page.title()
    # refresh the page
    page.reload()

