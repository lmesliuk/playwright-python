from pages.login_page import LoginPage
from playwright.sync_api import expect

def test_invalid_login(page):
    login = LoginPage(page)
    login.open()
    login.login("Admin", "pepe123")
    expect(page.get_by_text("Invalid credentials")).to_be_visible()
    #page.screenshot(path="shot.png", full_page=True)
    assert login.get_error_message() == "Invalid credentials"
    
    