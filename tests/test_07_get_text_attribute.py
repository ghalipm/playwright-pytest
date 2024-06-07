from playwright.sync_api import Page


def test_get_text_attribute(page: Page):
    page.goto("https://practice.cydeo.com/registration_form")
    expected_title = "Registration form"
    actual_title = page.get_by_role("heading").inner_text()
    assert expected_title.__eq__(actual_title)
    placeholder = page.query_selector("//input[@name='firstname']").get_attribute("placeholder")
    print("placeholder = " + placeholder)
    assert placeholder.__eq__("first name")
    page.wait_for_timeout(1000)
