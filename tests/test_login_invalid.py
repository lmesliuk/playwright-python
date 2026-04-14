from pages.login_page import LoginPage

def test_successful_login(page):
    login = LoginPage(page)
    login.open()
    login.login("Admin", "pepe123")
    assert login.get_error_message() == "Invalid credentials"
    
    