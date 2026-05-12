from playwright.sync_api import Playwright, sync_playwright, expect
from pom.home_page_element import HomePage
from pom.swag_element import SwagPage


def about_us_scrtion_verbiage(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    page=browser.new_page()
    page.goto('https://www.saucedemo.com/')
    page.wait_for_load_state("networkidle")
    home_page=HomePage(page)
    home_page.username.fill("standard_user")
    home_page.password.fill("secret_sauce",)
    home_page.login_button.click(timeout=1000)
    expect(home_page.text_verify).to_be_visible()

    swag_page = SwagPage(page)
    expect(swag_page.footer_text).to_be_visible()
    swag_page.open_menu.click(timeout=1000)
    swag_page.logout_button.click()
    print("Logout Successful")



with sync_playwright() as playwright:
    about_us_scrtion_verbiage(playwright)