from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Page_results():
    def __init__(self, driver):
        self.driver = driver
        self.articleTitle = (By.XPATH, '//*[@id="search"]/span/div/h1/div/div[1]/div/div/span[3]')
        self.productFromlist = (By.CLASS_NAME, 's-product-image-container')
        self.productName = (By.XPATH, '//*[@id="productTitle"]')
        self.addToCartButton = (By.NAME, 'submit.add-to-cart')

    def check_title(self):
        title = self.driver.find_element(*self.articleTitle).text
        return title

    def click_product_from_list(self):
        self.driver.find_element(*self.productFromlist).click()

    def product_title(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((self.productName)))
        product_name = self.driver.find_element(*self.productName).text
        return product_name

    def add_article_to_cart(self):
        self.driver.find_element(*self.addToCartButton).click()

