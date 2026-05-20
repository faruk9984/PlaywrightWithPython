# from playwright.sync_api import sync_playwright
# import time
#
# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     # Set basic auth credentials if required by staging environment
#     context = browser.new_context(
#         http_credentials={"username": "toffee", "password": "Toffee@1234"}
#     )
#     page = context.new_page()
#
#     print("Navigating to https://stage.toffeelive.com/en...")
#     page.goto("https://stage.toffeelive.com/en")
#     page.wait_for_load_state("networkidle")
#     time.sleep(2)
#
#     # Click Sign In button (try different variations)
#     print("Clicking Sign In button...")
#     try:
#         # Try different button text variations
#         page.locator("button:has-text('Sign In'), button:has-text('Sign in'), a:has-text('Sign In'), a:has-text('Sign in')").first.click()
#     except:
#         print("Sign In button not found with text, trying CSS selectors...")
#         page.locator("button[class*='sign'], a[class*='sign']").first.click()
#     page.wait_for_load_state("networkidle")
#     time.sleep(2)
#
#
#     # Provide phone number and click continue (try different selectors)
#     print("Entering phone number: 01961931605...")
#     try:
#         # Try all text inputs first
#         phone_input = page.locator("input[type='text']").first
#         phone_input.fill("01961931605")
#     except Exception as e:
#         print(f"Error finding phone input: {e}")
#         # Try other input types
#         phone_input = page.locator("input").first
#         phone_input.fill("01961931605")
#
#     time.sleep(1)
#
#     print("Clicking Continue button...")
#     try:
#         page.locator("button:has-text('Continue'), button:has-text('continue')").first.click()
#     except:
#         page.locator("button[type='submit']").first.click()
#     page.wait_for_load_state("networkidle")
#     time.sleep(2)
#
#     # Provide OTP
#     print("Entering OTP: 123456...")
#     try:
#         # Try different OTP input selectors
#         otp_input = page.locator("input[type='text'], input[inputmode='numeric']").first
#         otp_input.fill("123456")
#     except Exception as e:
#         print(f"Error finding OTP input: {e}")
#         otp_input = page.locator("input").first
#         otp_input.fill("123456")
#
#     time.sleep(1)
#
#     # Wait for 3 seconds
#     print("Waiting 3 seconds...")
#     time.sleep(3)
#
#     print("Test completed!")
#
#     context.close()
#     browser.close()
#
