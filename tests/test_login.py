from pages.login_page import LoginPage

def test_successful_login(page):
    login = LoginPage(page)
    login.open()
    login.login("Admin", "admin123")
    assert login.is_dashboard_displayed()
    
    