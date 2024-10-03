from Pages.main_page import AuthorizeInSite
from conftest import browser

def test_negative_authorize(browser):
    citylinkpage = AuthorizeInSite(browser)
    citylinkpage.open()
    citylinkpage.authorizebutton("name@gmail.com", "123456")
    citylinkpage.сonfirmation_of_authorization_error_after()
