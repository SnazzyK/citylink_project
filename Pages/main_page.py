import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from Pages.base_page import  BasePage
from conftest import browser


class LocatorsInSite:
    locator_authorize = (By.XPATH,'//span[@class="ekyeari0 e106ikdt0 css-1y9ljh1 e1gjr6xo0"]')
    locator_email_input = (By.XPATH,'//input[@name= "login"]')
    locator_pass_input = (By.XPATH,'//input[@name= "pass"]')
    locator_button_authorize = (By.XPATH,'//button[@class = "e4uhfkv0 css-1nvnwij e4mggex0"]')
    locator_name_account = (By.XPATH,"//span[@class= 'en3k2720 e106ikdt0 css-1y9ljh1 e1gjr6xo0']")

    locator_product_catalog = (By.XPATH,"//input[@type='search']")
    locator_search = (By.XPATH,"//button[@class='css-c064wa ebli37a0']")
    locator_in_product = (By.XPATH,"//div[@class='app-catalog-shrvo4 e1ekfd3u0']//a[@title='Смартфон INFINIX Note 30 8/256Gb,  X6833B,  голубой']")
    locator_add_cart = (By.XPATH,"//button[@class='e11w80q30 e4uhfkv0 app-catalog-zkoen2 e4mggex0']")
    text_product = (By.XPATH,"//span[@class='e1ys5m360 e106ikdt0 css-p2oaao e1gjr6xo0']")
    go_to_cart = (By.XPATH,"(//a[@href='/order/']//span[@class='css-1xdhyk6 e1hf2t4f0'])[1]")
    delete_product = (By.XPATH,"//*[@id='__next']/div/main/div[1]/div[2]/section/div[1]/div[2]/div/div/div[5]/div/div[4]/div/div/button")
    text_delete = (By.XPATH,"//span[@class='e1ys5m360 e106ikdt0 css-1spb733 e1gjr6xo0']")

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





