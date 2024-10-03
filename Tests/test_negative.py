from Pages.main_page import AuthorizeInSite
from conftest import browser

def test_negative_authorize(browser):
    citylinkpage = AuthorizeInSite(browser)
    citylinkpage.open()
    citylinkpage.authorizebutton("mihailtestov1ch8@gmail.com", ".")
    citylinkpage.сonfirmation_of_authorization_error()
