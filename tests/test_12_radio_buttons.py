from playwright.sync_api import Page


def test_radio_buttons(page: Page):
    page.goto("https://practice.cydeo.com/radio_buttons")
    # it will not work because there is no connection between label and input tag
    radio_red = page.locator("#red")
    assert not radio_red.is_checked()
    page.wait_for_timeout(1000)
    radio_red.check()
    page.wait_for_timeout(1000)
    assert radio_red.is_checked()
    page.wait_for_timeout(2000)

    radio_hockey=page.locator("#hockey")
    assert not radio_hockey.is_checked()
    radio_hockey.check()
    page.wait_for_timeout(1000)
    assert radio_hockey.is_checked()
