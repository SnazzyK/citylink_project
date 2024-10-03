from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import browser


class BasePage():

    def __init__(self, driver,main_url=None):
        self.driver = driver


    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator),
                                                          message=f"Can't find element by locator {locator}")
    def find_element_visible(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator),
                                                          message=f"Can't find element by locator {locator}")

    def open(self,main_url):
        self.main_url = "https://www.citilink.ru"
        return self.main_url



