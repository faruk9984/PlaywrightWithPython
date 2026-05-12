class SwagPage:
    def __init__(self,page):
        self.open_menu=page.get_by_role("button", name="Open Menu")
        self.logout_button=page.locator("[data-test=\"logout-sidebar-link\"]")
        self.footer_text=page.locator("[data-test=\"footer-copy\"]")