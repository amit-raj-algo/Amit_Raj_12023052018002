from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


def test_valid_login(driver):

    # Open SauceDemo
    driver.get("https://www.saucedemo.com/")

    # Create LoginPage object
    login_page = LoginPage(driver)

    # Perform login
    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    # Create DashboardPage object
    dashboard_page = DashboardPage(driver)

    # Assertions
    assert "/inventory.html" in driver.current_url

    assert dashboard_page.is_inventory_displayed()

    assert dashboard_page.get_page_title() == "Products"


# Selenium_Module_2
# │
# ├── pages
# │   ├── __init__.py
# │   ├── login_page.py          ✅
# │   └── dashboard_page.py      ✅
# │
# ├── tests
# │   ├── __init__.py            ✅
# │   └── test_login.py          ✅
# │
# ├── pytest.ini                 ✅
# │
# └── venv                       ✅

# Assignment 7

# LoginPage use ho raha hai ✅
# DashboardPage use ho raha hai ✅
# Locators page classes mein hain ✅
# UI methods page classes mein hain ✅
# Assertions test file mein hain ✅
# Login successful hai ✅
# /inventory.html assertion pass hui ✅
# Inventory assertion pass hui ✅
# "Products" title assertion pass hui ✅


# Tumne Assignment 9 mein kya-kya complete kiya
# Requirement	Status
# PyTest integration	✅
# PyTest fixtures	✅
# Chrome initialization	✅
# Browser cleanup	✅
# Data-driven tests	✅
# 6 CSV test cases	✅
# POM integration	✅
# Assertions	✅
# HTML report	✅
# Failed-test screenshot	✅ Tested
# Screenshot folder	✅
# Complete test suite	✅ 7/7 PASS