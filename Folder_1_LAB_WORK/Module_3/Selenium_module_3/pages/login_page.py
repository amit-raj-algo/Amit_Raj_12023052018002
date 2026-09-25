from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

    URL = "https://www.saucedemo.com/"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)

    def login(self, username, password):

        username_element = self.wait.until(
            EC.visibility_of_element_located(self.USERNAME)
        )

        password_element = self.wait.until(
            EC.visibility_of_element_located(self.PASSWORD)
        )

        username_element.clear()
        password_element.clear()

        username_element.send_keys(username)
        password_element.send_keys(password)

        self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        ).click()

    def get_error_message(self):

        return self.wait.until(
            EC.visibility_of_element_located(self.ERROR_MESSAGE)
        ).text