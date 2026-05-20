import pytest
from playwright.sync_api import Playwright

@pytest.fixture
def set_up(page):
    # browser = playwright.chromium.launch(headless=False, slow_mo=500)
    # context = browser.new_context()
    # page = context.new_page()
    # page.set_default_timeout(15000)
    # page.goto("https://www.saucedemo.com/")
    # page.wait_for_load_state("networkidle")

    yield page