from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage:

    INVENTORY_CONTAINER = (
        By.ID,
        "inventory_container"
    )

    TITLE = (
        By.CSS_SELECTOR,
        ".title"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def is_inventory_displayed(self):

        return self.wait.until(
            EC.visibility_of_element_located(
                self.INVENTORY_CONTAINER
            )
        ).is_displayed()

    def get_page_title(self):

        return self.wait.until(
            EC.visibility_of_element_located(
                self.TITLE
            )
        ).text