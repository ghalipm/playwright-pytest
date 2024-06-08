from playwright.sync_api import Page


def test_drop_downs_1(page: Page):
    page.goto("https://practice.cydeo.com/dropdown")
    # simple drop down:
    page.select_option("#dropdown", "Option 1")
    selected_option = page.evaluate("document.querySelector('#dropdown').value")
    print('\n', "------------------New Line --------------------")
    print("selected_option: " + selected_option)
    assert selected_option == "1", f"Expected state to be 'Option 1', but got {selected_option}"

    print(selected_option)
    page.select_option("#year", "1987")
    page.select_option("#month", "February")
    page.select_option("#day", "2")

    actual_year = page.evaluate("document.querySelector('#year').value")
    actual_month = page.evaluate("document.querySelector('#month').value")
    actual_day = page.evaluate("document.querySelector('#day').value")

    page.wait_for_timeout(3000)

    print('\n', "------------------New Line --------------------")
    print("Selected year: " + actual_year)
    print("Selected month: " + actual_month)
    print("Selected day: " + actual_day)


def test_drop_downs_state_and_lang_selection(page: Page):
    page.goto("https://practice.cydeo.com/dropdown")
    page.wait_for_timeout(1000)
    page.select_option("#state", value="TX")
    page.wait_for_timeout(1000)
    # lang select is about options, not drop down
    page.locator("//select[@name='Languages']/option").nth(0)
    page.wait_for_timeout(1000)

    actual_state = page.evaluate("document.querySelector('#state').value")
    actual_lang = page.locator("//select[@name='Languages']/option").nth(0).inner_text()
    print('\n', "------------------New Line --------------------")
    print(f"Selected state: {actual_state}")
    print(f"Selected language: {actual_lang}")

    # Assertions to verify the selections
    assert actual_state == "TX", f"Expected state to be 'TX', but got {actual_state}"
    assert actual_lang == "Java", f"Expected language to be 'Java', but got {actual_lang}"


def test_selecting_links_from_drop_downs(page: Page):
    page.goto("https://practice.cydeo.com/dropdown")
    page.wait_for_timeout(1000)
    page.locator("#dropdownMenuLink").click()
    page.wait_for_timeout(1000)
    page.locator("text=Amazon").click()
    page.wait_for_timeout(1000)
    print('\n', "------------------New Line --------------------")
    print("Selected link: "+page.title())
    assert page.title().__contains__("Amazon"), f"Expected link to be 'Amazon', but got {page.title()}"
