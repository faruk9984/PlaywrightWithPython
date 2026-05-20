import re
from playwright.sync_api import Playwright, sync_playwright, expect
import pytest


@pytest.mark.smoke
# @pytest.mark.regression
def test_login_demo(set_up) -> None:
    page = set_up
    page.goto("https://www.saucedemo.com/")
    page.wait_for_load_state("networkidle")
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").fill("secret_sauce", timeout=2000)
    expect(page.locator('[data-test="login-button"]')).to_have_value("Login", timeout=2000)
    page.locator("[data-test=\"login-button\"]").click(timeout=3000)
    expect(page.locator(".app_logo")).to_have_text("Swag Labs")

    

    page.wait_for_selector("[data-test='footer-copy']")
    expect(page.locator("[data-test='footer-copy']")).to_be_visible()
    expect(page.locator("[data-test='footer-copy']")).to_contain_text("© 2026 Sauce Labs. All Rights Reserved. Terms of Service | Privacy Policy")
    print("Footer text is correct and visible.")

    # all_links= page.get_by_role("link").all()
    # for link in all_links:
    #     if "$29" in link.text_content():
    #         assert 'SOCKS' not in link.text_content().lower() and "notepad" not in link.text_content().lower()

    # product = page.get_by_text("$29").first.locator("xpath=../../..").get_by_text("Sauce Labs Backpack").text_content()
    # product = page.get_by_text("$29").first.locator("xpath=../..//a").text_content()
    # assert product != "Socks"

    # page.locator("xpath=//*[contains(@class, 'inventory_item_img')]").nth(1)

    # page.wait_for_load_state("networkidle")
    # page.pause()
    # page.wait_for_load_state()


    page.get_by_role("button", name="Open Menu").click()
    page.locator("[data-test=\"logout-sidebar-link\"]").click()
    print('Yay!')


# with sync_playwright() as playwright:
#     run(playwright)
