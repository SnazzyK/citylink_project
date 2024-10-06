import os
from Pages.main_page import AuthorizeInSite
from conftest import browser

def test_authorize(browser):

    citylinkpage = AuthorizeInSite(browser)
    citylinkpage.open()
    citylinkpage.authorizebutton("mihailtestov1ch8@gmail.com","1234554321")
    citylinkpage.authorization_confirmation()
    citylinkpage.search_input_field("Смартфон")
    citylinkpage.search_product_and_add_in_card()
    citylinkpage.delete_product()
















