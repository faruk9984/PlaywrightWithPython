import re
from playwright.sync_api import Playwright, sync_playwright, expect
import pytest


@pytest.mark.smoke
# @pytest.mark.regression
def test_login_demo(login_set_up) -> None:
    page = login_set_up

    page.get_by_role("button", name="Open Menu").click()
    page.locator("[data-test=\"logout-sidebar-link\"]").click()
    print('Yay!')


@pytest.mark.smoke2
def test_login_demo_2(login_set_up) -> None:
    page = login_set_up
    print("Home page load Successfull")







@pytest.mark.smoke3
def test_login_demo_3(login_set_up2) -> None:
    page = login_set_up2
