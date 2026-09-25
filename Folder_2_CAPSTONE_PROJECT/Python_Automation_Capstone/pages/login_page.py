from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    EMAIL_FIELD = (By.ID, "input-email")
    PASSWORD_FIELD = (By.ID, "input-password")
    LOGIN_BUTTON = (By.XPATH, "//input[@value='Login']")

    MY_ACCOUNT_LINK = (
        By.XPATH,
        "//a[contains(normalize-space(), 'My Account')]"
    )

    def __init__(self, driver):
        self.driver = driver

    def open_login_page(self):
        self.driver.get(
            "https://tutorialsninja.com/demo/index.php?route=account/login"
        )

    def enter_email(self, email):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.EMAIL_FIELD)
        ).send_keys(email)

    def enter_password(self, password):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.PASSWORD_FIELD)
        ).send_keys(password)

    def click_login(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        ).click()

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()

    def is_logged_in(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.url_contains("route=account/account")
            )
            return True
        except:
            return False