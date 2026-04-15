from playwright.sync_api import expect
import logging

logger = logging.getLogger(__name__) # Set up a logger for this module

class LoginPage:
    URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    def __init__(self, page):
        self.page = page

    def open(self):
        logger.info("Opening login")
        self.page.goto(self.URL)

    def login(self, username, password):
        logger.info(f"Logging in with username: {username}")
        self.page.get_by_placeholder("Username").fill(username)
        self.page.get_by_placeholder("Password").fill(password)
        self.page.get_by_role("button", name="Login").click()

    def is_dashboard_displayed(self):
        logger.info("Checking if dashboard is displayed")
        expect(self.page.get_by_role("heading", name="Dashboard")).to_be_visible()
        return True

    def get_error_message(self):
        msg = self.page.locator(".oxd-alert-content-text").inner_text()
        logger.info(f"Error message displayed: {msg}")
        return msg