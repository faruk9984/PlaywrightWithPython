
import pytest
from playwright.sync_api import Playwright, expect
from requests import session


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
    page.locator("[data-test=\"password\"]").fill("secret_sauce", timeout=2000)
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
def go_to_new_collection_page(page):
    page.goto("https://www.automationtesting.co.uk/contactForm.html")
    page.wait_for_load_state("networkidle")

    yield page