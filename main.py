from selenium import webdriver
import unittest
from pages.pageIndex import *
from pages.pageResults import *
from pages.pagesCart import *

class AmazonSearch(unittest.TestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--incognito')
        self.driver = webdriver.Chrome('chromedriver/chromedriver.exe', options=chrome_options)
        self.driver.get('https://www.amazon.es/')
        self.driver.maximize_window()

        # Check the cookies option
        accept_Cookies_Button = self.driver.find_element(by=By.NAME, value="accept")
        if accept_Cookies_Button.size['width'] != 0:
            accept_Cookies_Button.click()

    def test_view_item_page(self):
        item = "macbook air"
        pages_index = Page_index(self.driver)
        pages_results = Page_results(self.driver)
        pages_cart = Page_cart(self.driver)
        pages_index.search_item(item)
        title = pages_results.check_title()
        self.assertIn(item, title)
        pages_results.click_product_from_list()
        product_title = pages_results.product_title()
        pages_results.add_article_to_cart()
        cart_article_to_check = pages_cart.check_article_in_cart()

        self.assertIn(product_title, cart_article_to_check)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()