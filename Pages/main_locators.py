from selenium.webdriver.common.by import By



class LocatorsInSite:
    locator_authorize = (By.XPATH,'//span[@class="ekyeari0 e106ikdt0 css-1y9ljh1 e1gjr6xo0"]')
    locator_email_input = (By.XPATH,'//input[@name= "login"]')
    locator_pass_input = (By.XPATH,'//input[@name= "pass"]')
    locator_button_authorize = (By.XPATH,'//button[@class = "e4uhfkv0 css-1nvnwij e4mggex0"]')
    locator_name_account = (By.XPATH,"//span[@class= 'en3k2720 e106ikdt0 css-1y9ljh1 e1gjr6xo0']")

    locator_product_catalog = (By.XPATH,"//input[@type='search']")
    locator_search = (By.XPATH,"//button[@class='css-c064wa ebli37a0']")
    locator_in_product = (By.XPATH,"//div[@class='app-catalog-shrvo4 e1ekfd3u0']//a[@title='Смартфон INFINIX Note 30 8/256Gb,  X6833B,  голубой']")
    locator_add_cart = (By.XPATH,"//button[@data-meta-name='BasketDesktopButton']")
    text_product = (By.XPATH,"//span[@class='e1ys5m360 e106ikdt0 css-p2oaao e1gjr6xo0']")
    go_to_cart = (By.XPATH,"(//a[@href='/order/']//span[@class='css-1xdhyk6 e1hf2t4f0'])[1]")
    delete_product = (By.XPATH,"//div[@data-meta-name='DeleteAction']//button")
    text_delete = (By.XPATH,"//span[@class='e1ys5m360 e106ikdt0 css-1spb733 e1gjr6xo0']")
    error_massage = (By.XPATH,"//div[@class='css-12tloqr e15krpzo5']")