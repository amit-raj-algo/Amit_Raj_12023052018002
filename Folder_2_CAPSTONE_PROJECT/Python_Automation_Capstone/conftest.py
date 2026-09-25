import os

import pytest
from selenium import webdriver

from utils.config_reader import ConfigReader


@pytest.fixture
def driver():
    config = ConfigReader()

    browser = config.get_browser()
    url = config.get_application_url()

    if browser.lower() == "chrome":
        driver = webdriver.Chrome()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()
    driver.get(url)

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")

        if driver:
            screenshots_dir = os.path.join(
                os.path.dirname(os.path.abspath(__file__)),
                "screenshots"
            )

            os.makedirs(screenshots_dir, exist_ok=True)

            screenshot_path = os.path.join(
                screenshots_dir,
                f"{item.name}.png"
            )

            driver.save_screenshot(screenshot_path)

            print(f"\nScreenshot saved: {screenshot_path}")