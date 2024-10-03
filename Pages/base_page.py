from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import browser


class BasePage():

    def __init__(self, driver):
        self.driver = driver
        self.main_url = "https://www.citilink.ru"


    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator),
                                                          message=f"Can't find element by locator {locator}")
    def find_element_visible(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator),
                                                          message=f"Can't find element by locator {locator}")

    def open(self):
        return self.driver.get(self.main_url)



