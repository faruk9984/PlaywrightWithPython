
class ContactUsPage:
    def __init__(self,page):
        self.page=page

    # def navigate_to_contact_us(self):
    #     self.page.goto("https://www.automationtesting.co.uk/contactForm.html")
    #     self.page.wait_for_load_state("networkidle")

    def fill_contact_form(self, Fname, Lname, email, message):
        self.page.get_by_role("textbox", name="First Name").fill(Fname)
        self.page.get_by_role("textbox", name="Last Name").fill(Lname)
        self.page.get_by_role("textbox", name="Email Address").fill(email)
        self.page.get_by_role("textbox", name="Comments").fill(message)
        self.page.locator("input[type='submit']").click()
