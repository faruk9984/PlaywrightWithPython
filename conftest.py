import os
import time

import playwright
import pytest
from playwright.sync_api import Playwright, expect


PASSWORD = os.environ['PASSWORD']
# PASSWORD = os.getenv("PASSWORD")



# @pytest.fixture(scope="session")
@pytest.fixture(scope="function")
def set_up(browser):
    # browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()
    page.set_default_timeout(15000)
    page.goto("https://www.saucedemo.com/")
    page.wait_for_load_state("networkidle")

    yield page
    page.close()



# @pytest.fixture(scope="session")
@pytest.fixture(scope="function")
def login_set_up(set_up):
    page = set_up

    page.locator("[data-test=\"username\"]").fill("standard_user")
    # page.locator("[data-test=\"password\"]").fill(utils.secret_config.PASSWORD, timeout=2000)
    page.locator("[data-test=\"password\"]").fill(PASSWORD, timeout=2000)
    expect(page.locator('[data-test="login-button"]')).to_have_value("Login", timeout=2000)
    page.locator("[data-test=\"login-button\"]").click(timeout=3000)
    expect(page.locator(".app_logo")).to_have_text("Swag Labs")

    page.wait_for_selector("[data-test='footer-copy']")
    expect(page.locator("[data-test='footer-copy']")).to_be_visible()
    expect(page.locator("[data-test='footer-copy']")).to_contain_text(
        "© 2026 Sauce Labs. All Rights Reserved. Terms of Service | Privacy Policy")
    print("Footer text is correct and visible.")

    yield page
    page.close()




@pytest.fixture()
def go_to_new_collection_page(page, assert_snapshot):
    page.goto("https://www.automationtesting.co.uk/contactForm.html")
    page.wait_for_load_state("networkidle")
    # assert_snapshot(page.screenshot())

    yield page







@pytest.fixture(scope="session")
def context_creation(playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.saucedemo.com/")
    page.wait_for_load_state("networkidle")

    page.locator("[data-test=\"username\"]").fill("standard_user")
    # page.locator("[data-test=\"password\"]").fill(utils.secret_config.PASSWORD, timeout=2000)
    page.locator("[data-test=\"password\"]").fill(PASSWORD, timeout=2000)
    expect(page.locator('[data-test="login-button"]')).to_have_value("Login", timeout=2000)
    page.locator("[data-test=\"login-button\"]").click(timeout=3000)
    expect(page.locator(".app_logo")).to_have_text("Swag Labs")

    page.wait_for_load_state(timeout=10000)
    context.storage_state(path="storage_state.json")

    yield context
    time.sleep(3)



@pytest.fixture()
def login_set_up2(context_creation, browser, playwright):
    # browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context(storage_state="storage_state.json")
    page = context.new_page()
    page.goto("https://www.saucedemo.com/inventory.html")
    page.wait_for_load_state("networkidle")
    expect(page.get_by_text("Products")).to_have_text("Products", timeout=2000)
    # page.get_by_role("button", name="Open Menu").click()
    # page.locator("[data-test=\"logout-sidebar-link\"]").click()
    print('Yay!')

    yield page
    time.sleep(1)
    context.close()
    # browser.close()