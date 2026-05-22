from playwright.sync_api import Playwright, sync_playwright, expect
from pytest_playwright.pytest_playwright import context

import utils.secret_config
from pom.home_page_element import HomePage
from pom.swag_element import SwagPage
import pytest

@pytest.mark.integration
@pytest.mark.parametrize("username,password", [("standard_user", "secret_sauce"),
                                               pytest.param("locked_out_user", "secret_sauce", marks=pytest.mark.xfail),
                                               pytest.param("standard_user", "secret_test", marks=pytest.mark.xfail)])
def test_about_us_scrtion_verbiage(set_up, username, password) -> None:
    page = set_up
    # browser = playwright.chromium.launch(headless=False, slow_mo=500)
    # context = browser.new_context()
    # page=browser.new_page()
    # page.goto('https://www.saucedemo.com/')
    # page.wait_for_load_state("networkidle")
    home_page=HomePage(page)
    home_page.username.fill(username)
    home_page.password.fill(utils.secret_config.PASSWORD)
    home_page.login_button.click(timeout=1000)
    expect(home_page.text_verify).to_be_visible()

    swag_page = SwagPage(page)
    expect(swag_page.footer_text).to_be_visible()
    swag_page.open_menu.click(timeout=1000)
    swag_page.logout_button.click()
    print("Logout Successful")

    # context.close()
    # browser.close()




# @pytest.mark.skip(reason="This test fails")
# @pytest.mark.xfail(reason="This test fails")
@pytest.mark.regression
@pytest.mark.parametrize("username", ["standard_user",
                                               pytest.param("locked_out_user", marks=pytest.mark.xfail),
                                               pytest.param("standard_user", marks=pytest.mark.xfail)])
@pytest.mark.parametrize("password", ["secret_sauce",
                                               "secret_sauce",
                                               pytest.param("secret_test", marks=pytest.mark.xfail)])
def test_about_us_scrtion_verbiage2(set_up, username, password)-> None:
    page = set_up
    # browser = playwright.chromium.launch(headless=False, slow_mo=500)
    # context = browser.new_context()
    # page = browser.new_page()
    # page.goto('https://www.saucedemo.com/')
    # page.wait_for_load_state("networkidle")
    home_page = HomePage(page)
    home_page.username.fill(username)
    home_page.password.fill(utils.secret_config.PASSWORD)
    home_page.login_button.click(timeout=1000)
    expect(home_page.text_verify).to_be_visible()

    # swag_page = SwagPage(page)
    # expect(swag_page.footer_text).to_be_visible()
    # swag_page.open_menu.click(timeout=1000)
    # swag_page.logout_button.click()
    # print("Logout Successful2")

