from playwright.sync_api import Page


def test_playwright_methods(page: Page):
    page.goto("https://library2.cybertekschool.com/login.html")
    page.get_by_placeholder("Email address").fill("incorrectemail" + "@gmail.com")
    page.get_by_label("Password").fill("incorectpassword")
    page.get_by_placeholder("Password").fill("incorectpassword")
    # page.querySelector("#inputPassword").fill("incorectpassword")
    page.get_by_role("button", name="Sign in").click()
    print(page.get_by_role("button").inner_text())
    print(page.get_by_role("button").is_visible())
    page.wait_for_timeout(1000)
    message = "Sorry, Wrong Email or Password"
    assert page.content().__contains__(message)
    assert message in page.get_by_role("alert").inner_text()

