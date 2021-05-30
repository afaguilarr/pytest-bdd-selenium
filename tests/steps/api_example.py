from pytest_bdd import given, when, then
from requests import get


@when('the user makes an example API call')
def the_user_makes_an_example_api_call(steps_context):
    steps_context["request"] = get("https://jsonplaceholder.typicode.com/todos/1")


@then("the API responds successfully")
def the_api_response_successfully(steps_context):
    assert steps_context["request"].status_code == 200


@then('the response body contains the expected data')
def the_response_body_contains_the_expected_data(steps_context):
    body = steps_context["request"].json()
    assert body["userId"] == 1
    assert body["id"] == 1
    assert body["title"] == "delectus aut autem", "Error message"
    assert body["completed"] is False
