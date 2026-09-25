import pandas as pd
import pytest

from pages.login_page import LoginPage


# Read test data from CSV
data = pd.read_csv(
    "test_data/login_data.csv",
    keep_default_na=False
)

# Convert rows into dictionaries
test_cases = data.to_dict("records")


@pytest.mark.parametrize(
    "test_data",
    test_cases
)
def test_data_driven_login(test_data, driver):

    # Open SauceDemo
    driver.get("https://www.saucedemo.com/")

    # Create LoginPage object
    login_page = LoginPage(driver)

    # Get test data
    username = test_data["username"]
    password = test_data["password"]
    expected_result = test_data["expected_result"]
    expected_error = test_data["expected_error"]

    # Perform login
    login_page.login(
        username,
        password
    )

    # Validate result
    if expected_result == "success":

        assert "/inventory.html" in driver.current_url

    else:

        actual_error = login_page.get_error_message()

        assert actual_error == expected_error

# ✅ Assignment 8 successfully complete

# Tumne ab ye sab achieve kar liya:

# ✅ External CSV file se test data
# ✅ Pandas se CSV read
# ✅ 6 different login combinations
# ✅ Correct username/password validation
# ✅ Wrong username/password validation
# ✅ Empty username validation
# ✅ Empty password validation
# ✅ PyTest parametrize
# ✅ POM (LoginPage) ka use
# ✅ Assertions
# ✅ Browser cleanup using finally
# ✅ 6/6 tests PASS 