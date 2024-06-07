from playwright.sync_api import Page


def test_profile_search(page: Page):
    page.goto("https://www.google.com/")
    #  inspect, click area of interest, click "Properties",
    #  then look at what locator options are available.

    # get_by_test_id did not work:
    # page.get_by_test_id("APjFqb").press_sequentially("Jensen Huang", delay=5)

    # the following each of them works
    page.get_by_title("Search").press_sequentially("Jensen Huang", delay=50)
    # page.get_by_role("combobox").press_sequentially("Jensen Huang", delay=50)
    page.keyboard.press("Enter")
    assert "Jensen Huang" in page.title()