from playwright.sync_api import Page


def test_query_selector_text_content(page: Page):
    page.goto("https://login1.nextbasecrm.com/")
    page.query_selector("[name=USER_LOGIN]").fill("incorrectuser")
    page.query_selector("[name='USER_PASSWORD']").fill("incorrectpassword")
    page.query_selector(".login-btn").click()
    # page.query_selector("input.login-btn").click()
    error_message = page.query_selector(".errortext").text_content()
    print("error message = " + error_message)
