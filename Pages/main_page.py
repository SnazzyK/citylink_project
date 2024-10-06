import time

from selenium.common import TimeoutException

from Pages.main_locators import LocatorsInSite
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
        try:
            search_field_button = self.find_element(LocatorsInSite.locator_button_authorize)
            if search_field_button.is_displayed():
                 search_field_button.click()
            else: print("Элемент невидим")
        except TimeoutException:
            print("Кнопка не доступна.")



    def authorization_confirmation(self):
        search_field_name = self.find_element(LocatorsInSite.locator_name_account)
        element_text = search_field_name.text
        assert element_text == "Валерий"

    def сonfirmation_of_authorization_error(self):
        search_error_name = self.find_element_visible(LocatorsInSite.error_massage,time=30)
        error_name_text = search_error_name.text
        assert error_name_text == 'Поле должно содержать не менее 6 символов'

    def сonfirmation_of_authorization_error_after(self):
        search_error_name = self.find_element_visible(LocatorsInSite.error_massage_after, time=30)
        error_name_text = search_error_name.text
        assert error_name_text == 'Неверный логин или пароль'



    def search_input_field(self,name):
        search_button_catalog = self.find_element(LocatorsInSite.locator_product_catalog)
        search_button_catalog.send_keys(name)
        search_button_catalog.send_keys(Keys.ENTER)

    def search_product_and_add_in_card(self):
        search_product_button = self.find_element(LocatorsInSite.locator_in_product)
        search_product_button.click()
        search_add_cart_button = self.find_element(LocatorsInSite.locator_add_cart)
        search_add_cart_button.click()
        search_text = self.find_element(LocatorsInSite.text_product)
        product_text = search_text.text
        assert product_text == "Товар добавлен в корзину"

    def delete_product(self):
        search_cart_button =self.find_element(LocatorsInSite.go_to_cart)
        search_cart_button.click()
        search_delete_button = self.find_element(LocatorsInSite.delete_product)
        search_delete_button.click()
        time.sleep(3)
        search_delete_text = self.find_element_visible(LocatorsInSite.text_delete)
        delete_text = search_delete_text.text
        assert delete_text == "В корзине нет товаров"





