class HomePage:


    def __init__(self, page):
        self.username=page.locator("[data-test=\"username\"]")
        self.password=page.locator("[data-test=\"password\"]")
        self.login_button=page.locator("[data-test=\"login-button\"]")
        self.text_verify=page.locator(".app_logo")





