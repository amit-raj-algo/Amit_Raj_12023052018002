from selenium.webdriver.common.by import By


class ProductPage:

    # Locators
    SEARCH_FIELD = (By.NAME, "search")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "#search button")

    def __init__(self, driver):
        self.driver = driver

    def enter_search_text(self, product):
        self.driver.find_element(*self.SEARCH_FIELD).send_keys(product)

    def click_search(self):
        self.driver.find_element(*self.SEARCH_BUTTON).click()

    def search_product(self, product):
        self.enter_search_text(product)
        self.click_search()