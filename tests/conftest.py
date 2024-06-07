# this file serves like parent class in Java
# So we do not have to repeat fixtures in "test_" files
#  fixtures are comparable to Before, After
#  class , methods in TestNG.
# great site for reference:
# https://playwright.dev/python/
import pytest
from playwright.sync_api import sync_playwright, Browser, BrowserContext, Page


@pytest.fixture(scope="session")
def browser() -> [Browser, None]:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=300)
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def context(browser: Browser) -> [BrowserContext, None]:
    context = browser.new_context()
    yield context
    context.close()


@pytest.fixture(scope="function")
def page(context: BrowserContext) -> [Page, None]:
    page = context.new_page()
    yield page
    page.close()


@pytest.fixture(scope="function")
def page_with_ad_blocking(context: BrowserContext) -> [Page, None]:
    # with sync_playwright() as p:
    #     browser = p.chromium.launch(headless=False)
    #     context = browser.new_context()

    # Block Google Ads by intercepting and aborting requests
    context.route("**/*", lambda route: route.abort() if "googleads" in route.request.url else route.continue_())

    page = context.new_page()
    yield page
    page.close()
    # context.close()
    # browser.close()
