import time
from main_locators import LocatorsInSite
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from Pages.base_page import  BasePage
from conftest import browser


class AuthorizeInSite(BasePage):

    def authorizebutton(self,email,password):
        search_login_to_account = self.find_element(LocatorsInSite.locator_authorize)
        search_login_to_account.click()
        search_field_email = self.find_element(LocatorsInSite.locator_email_input)
        search_field_email.send_keys(email)
        search_field_pass = self.find_element(LocatorsInSite.locator_pass_input)
        search_field_pass.send_keys(password)
        search_field_button = self.find_element(LocatorsInSite.locator_button_authorize)
        search_field_button.click()
        search_field_name = self.find_element(LocatorsInSite.locator_name_account)
        element_text = search_field_name.text
        assert element_text == "Валерий"

    def cart(self,name):
        search_button_catalog = self.find_element(LocatorsInSite.locator_product_catalog)
        search_button_catalog.send_keys(name)
        search_button_catalog.send_keys(Keys.ENTER)
        search_product_button = self.find_element(LocatorsInSite.locator_in_product)
        search_product_button.click()
        search_product_button = self.find_element(LocatorsInSite.locator_add_cart)
        search_product_button.click()
        search_text = self.find_element(LocatorsInSite.text_product)
        product_text = search_text.text
        assert product_text == "Товар добавлен в корзину"
        search_cart_button =self.find_element(LocatorsInSite.go_to_cart)
        search_cart_button.click()
        search_delete_button = self.find_element(LocatorsInSite.delete_product)
        search_delete_button.click()
        time.sleep(3)
        search_delete_text = self.find_element_visible(LocatorsInSite.text_delete)
        delete_text = search_delete_text.text
        assert delete_text == "В корзине нет товаров"





