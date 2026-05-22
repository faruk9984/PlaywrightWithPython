import pytest
from playwright.sync_api import Playwright, sync_playwright, Expect
from pom.contact_us_page import ContactUsPage
# from test1 import playwright

@pytest.mark.unitT2
def test_submit_form(go_to_new_collection_page) -> None:
    page = go_to_new_collection_page
    # browser = playwright.chromium.launch(headless=False, slow_mo=500)
    # page = browser.new_page()
    contact_us=ContactUsPage(page)
    # contact_us.navigate_to_contact_us()
    contact_us.fill_contact_form("Faruk", "QA", "QA23@gmail.com", "Hello11111" )
