import unittest

from selenium import webdriver

from pages.login_page import LoginPage
from utils.config_reader import ConfigReader
from utils.csv_reader import CSVReader


class TestLogin(unittest.TestCase):

    def setUp(self):
        print("\n========================================")
        print("       UNITTEST LOGIN AUTOMATION")
        print("========================================")

        print("[1] Loading configuration...")
        config = ConfigReader()
        print("[PASS] Configuration loaded")

        print("[2] Launching Chrome browser...")
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(config.get_application_url())
        print("[PASS] Application opened")

    def test_valid_login(self):
        print("[3] Reading login data from CSV...")
        test_data = CSVReader.read_test_data()[0]
        print("[PASS] CSV data loaded")

        print("[4] Performing login...")
        login_page = LoginPage(self.driver)

        login_page.open_login_page()

        login_page.login(
            test_data["email"],
            test_data["password"]
        )

        print("[5] Verifying login...")
        self.assertTrue(login_page.is_logged_in())
        print("[PASS] Login successful")

        print("========================================")
        print("       UNITTEST LOGIN TEST PASSED")
        print("========================================")

    def tearDown(self):
        print("[6] Closing browser...")
        self.driver.quit()
        print("[PASS] Browser closed")


if __name__ == "__main__":
    unittest.main()