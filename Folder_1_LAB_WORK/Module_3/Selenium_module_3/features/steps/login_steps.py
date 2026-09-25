import os
import pandas as pd

from behave import given, when, then

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


@given("I open the SauceDemo login page")
def step_open_login_page(context):

    context.login_page = LoginPage(context.driver)

    context.login_page.open()


@when("I execute all login test cases from the CSV file")
def step_execute_login_tests(context):

    csv_path = os.path.join(
        "test_data",
        "login_data.csv"
    )

    test_data = pd.read_csv(
        csv_path,
        keep_default_na=False
    )

    context.results = []

    for _, row in test_data.iterrows():

        test_case = row["test_case"]
        username = row["username"]
        password = row["password"]
        expected_result = row["expected_result"]
        expected_error = row["expected_error"]

        print(f"\nRunning {test_case}")

        # Open login page before every test case
        context.login_page.open()

        # Perform login
        context.login_page.login(
            username,
            password
        )

        if expected_result == "success":

            dashboard_page = DashboardPage(
                context.driver
            )

            current_url = context.driver.current_url

            inventory_displayed = (
                dashboard_page.is_inventory_displayed()
            )

            page_title = (
                dashboard_page.get_page_title()
            )

            passed = (
                "/inventory.html" in current_url
                and inventory_displayed
                and page_title == "Products"
            )

            actual_result = (
                f"URL={current_url}, "
                f"Title={page_title}"
            )

        else:

            actual_error = (
                context.login_page.get_error_message()
            )

            passed = actual_error == expected_error

            actual_result = actual_error

        context.results.append(
            {
                "test_case": test_case,
                "passed": passed,
                "actual": actual_result,
                "expected": (
                    "Success"
                    if expected_result == "success"
                    else expected_error
                )
            }
        )

        print(
            f"{test_case}: "
            f"{'PASSED' if passed else 'FAILED'}"
        )


@then("all login test cases should pass")
def step_validate_all_tests(context):

    failed_tests = [
        result
        for result in context.results
        if not result["passed"]
    ]

    for result in context.results:

        print(
            f"\n{result['test_case']}: "
            f"{'PASSED' if result['passed'] else 'FAILED'}"
        )

        if not result["passed"]:

            print(
                f"Expected: {result['expected']}"
            )

            print(
                f"Actual: {result['actual']}"
            )

    assert not failed_tests, (
        f"{len(failed_tests)} "
        f"login test case(s) failed."
    )

# @then('the login result should be "{result}"')
# def step_verify_login_result(context, result):

#     if result == "success":

#         assert "/inventory.html" in \
#                context.driver.current_url

#     else:

#         assert context.login_page.get_error_message()