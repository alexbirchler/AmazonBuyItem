from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Page_cart():
    def __init__(self, driver):
        self.driver = driver
        self.articleInCart = (By.CLASS_NAME, 'sc-product-title')
        self.buttonCart = (By.XPATH, '//*[@id="attach-sidesheet-view-cart-button"]')

    def check_article_in_cart(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((self.buttonCart))).click()
        cart_article_to_check = self.driver.find_element(*self.articleInCart).text
        return cart_article_to_check