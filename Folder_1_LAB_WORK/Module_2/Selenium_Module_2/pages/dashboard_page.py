from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage:

    # Locators
    TITLE = (By.CLASS_NAME, "title")
    INVENTORY_CONTAINER = (By.ID, "inventory_container")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # UI Methods

    def get_page_title(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.TITLE)
        ).text

    def is_inventory_displayed(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.INVENTORY_CONTAINER
            )
        ).is_displayed()