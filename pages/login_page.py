from playwright.sync_api import expect

class LoginPage:
    URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto(self.URL)

    def login(self, username, password):
        self.page.get_by_placeholder("Username").fill(username)
        self.page.get_by_placeholder("Password").fill(password)
        self.page.get_by_role("button", name="Login").click()

    #def is_dashboard_displayed(self):
    #    return self.page.get_by_role("heading", name="Dashboard").is_visible()

    #def is_dashboard_displayed(self):
     #   self.page.get_by_role("heading", name="Dashboard").wait_for()
    #    return self.page.get_by_role("heading", name="Dashboard").is_visible()

    def is_dashboard_displayed(self):
        expect(self.page.get_by_role("heading", name="Dashboard")).to_be_visible()
        return True

    def get_error_message(self):
        return self.page.locator(".oxd-alert-content-text").inner_text()