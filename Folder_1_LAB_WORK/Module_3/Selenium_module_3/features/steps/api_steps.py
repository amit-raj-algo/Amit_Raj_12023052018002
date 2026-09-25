from behave import given, when, then
import pandas as pd

from api.api_client import APIClient


@given("the API client is initialized")
def step_initialize_api(context):
    context.api_client = APIClient()

    context.test_data = pd.read_csv(
        "test_data/api_data.csv"
    )


@when('I request post data using test case "{test_case}"')
def step_request_post(context, test_case):

    row = context.test_data[
        context.test_data["test_case"] == test_case
    ].iloc[0]

    post_id = int(row["post_id"])

    context.expected_status = int(
        row["expected_status"]
    )

    context.response = context.api_client.get_post(
        post_id
    )


@then("the API response status should be 200")
def step_verify_status(context):

    assert context.response.status_code == \
           context.expected_status