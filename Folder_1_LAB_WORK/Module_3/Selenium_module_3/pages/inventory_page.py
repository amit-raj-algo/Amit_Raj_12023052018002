from selenium.webdriver.common.by import By


class InventoryPage:

    TITLE = (By.CLASS_NAME, "title")
    INVENTORY_CONTAINER = (By.ID, "inventory_container")

    def __init__(self, driver):
        self.driver = driver

    def get_page_title(self):
        return self.driver.find_element(
            *self.TITLE
        ).text

    def is_inventory_displayed(self):
        return self.driver.find_element(
            *self.INVENTORY_CONTAINER
        ).is_displayed()