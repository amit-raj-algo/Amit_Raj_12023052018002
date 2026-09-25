from pages.login_page import LoginPage
from utils.csv_reader import CSVReader


def test_valid_login(driver):
    print("\n========================================")
    print("        LOGIN AUTOMATION TEST")
    print("========================================")

    print("[1] Reading login data from CSV...")
    test_data = CSVReader.read_test_data()[0]
    print("[PASS] CSV test data loaded successfully")

    print("[2] Opening Login Page...")
    login_page = LoginPage(driver)
    login_page.open_login_page()
    print("[PASS] Login page opened")

    print("[3] Entering email and password...")
    login_page.login(
        test_data["email"],
        test_data["password"]
    )
    print("[PASS] Login credentials submitted")

    print("[4] Verifying login...")
    assert login_page.is_logged_in()
    print("[PASS] Login successful")

    print("========================================")
    print("        LOGIN TEST PASSED")
    print("========================================\n")