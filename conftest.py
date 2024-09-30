import datetime
import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    chrome_options = Options()
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument("--incognito")
    browser = webdriver.Chrome(options=chrome_options)
    browser.maximize_window()
    browser.set_page_load_timeout(60)
    yield browser
    print("\nquit browser..")
    browser.save_screenshot("screenshot.png")
    browser.quit()


