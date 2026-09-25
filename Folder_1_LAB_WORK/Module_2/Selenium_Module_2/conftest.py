import os
import base64

import pytest
import pytest_html
from selenium import webdriver


@pytest.fixture
def driver():

    # Start Chrome
    driver = webdriver.Chrome()

    # Open browser maximized
    driver.maximize_window()

    yield driver

    # Close browser
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    # Run the actual test
    outcome = yield

    # Get test report
    report = outcome.get_result()

    # Only capture screenshot when actual test fails
    if report.when == "call" and report.failed:

        # Get driver from fixture
        driver = item.funcargs.get("driver")

        if driver:

            # Create screenshots folder
            os.makedirs("screenshots", exist_ok=True)

            # Screenshot filename
            screenshot_name = f"{item.name}.png"

            screenshot_path = os.path.join(
                "screenshots",
                screenshot_name
            )

            # Save screenshot
            driver.save_screenshot(screenshot_path)

            # Read screenshot
            with open(screenshot_path, "rb") as image_file:
                screenshot_data = image_file.read()

            # Convert bytes to Base64 string
            screenshot_base64 = base64.b64encode(
                screenshot_data
            ).decode("utf-8")

            # Attach screenshot to HTML report
            extras = getattr(report, "extras", [])

            extras.append(
                pytest_html.extras.image(
                    screenshot_base64,
                    mime_type="image/png",
                    name="Failure Screenshot"
                )
            )

            report.extras = extras

            print(
                f"\nScreenshot saved: {screenshot_path}"
            )
    

# Assignment 9 goal 
# Test starts
#    ↓
# conftest.py fixture
#    ↓
# Chrome open
#    ↓
# Test executes
#    ↓
# PASS → Chrome close
# FAIL → Screenshot save → Chrome close
#    ↓
# HTML report