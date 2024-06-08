from playwright.sync_api import Page


def test_checkbox_radio(page: Page):
    page.goto("https://practice.cydeo.com/checkboxes")
    checkbox1 = page.locator("#box1")
    # checkbox1= page.get_by_role(AriaRole.CHECKBOX).nth(0)
    checkbox2 = page.locator("#box2")
    print('\n', "------------------New Line --------------------")
    print("default before clicking box1: " + str(checkbox1.is_checked()))
    print("default before clicking box2: " + str(checkbox2.is_checked()))

    page.wait_for_timeout(2000)

    # checkbox1.click()
    checkbox1.check()
    assert checkbox1.is_checked()
    # checkbox2.click()
    checkbox2.uncheck()
    assert not checkbox2.is_checked(), "Checkbox 2 should be unchecked"
    page.wait_for_timeout(3000)

    print("default after clicking box1: " + str(checkbox1.is_checked()))
    print("default after clicking box2: " + str(checkbox2.is_checked()))
