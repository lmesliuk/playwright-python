import re # Regular expression module for pattern matching
from playwright.sync_api import Page, expect

def test_home_has_title(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    expect(page).to_have_title(re.compile("OrangeHRM")) # Assert that the page title contains "OrangeHRM" using a regular expression
    
    
def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")
    page.get_by_role("link", name="Get started").click()
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()