from selenium.webdriver.common.by import By

class Page_index():
    def __init__(self, driver):
        self.driver = driver
        self.searchBox = (By.ID, "twotabsearchtextbox")
        self.buttonSearch = (By.ID, "nav-search-submit-button")

    def search_item(self, item):
        search_input = self.driver.find_element(*self.searchBox)
        search_input.send_keys(item)
        self.driver.find_element(*self.buttonSearch).click()

