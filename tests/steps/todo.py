import json

import pytest
from pytest_bdd import given, when, then, parsers
from selenium.webdriver.chrome.webdriver import WebDriver

from tests.page_objects.todo_page import TodoPage


@pytest.fixture(scope="function")
def todo_page(web_driver: WebDriver) -> TodoPage:
    return TodoPage(web_driver)


@given('I am on the todo page', target_fixture='todo_page')
def i_am_on_the_todo_page(todo_page: TodoPage):
    return todo_page.open()


@when(parsers.parse('I type the todo {todo_text}'))
@when('I type the todo <todo_text>')
def i_type_the_todo(todo_text: str, todo_page: TodoPage):
    todo_page.add_todo(todo_text)


@then(parsers.parse("todo list item {index} has text {todo_text}"))
@then("todo list item <index> has text <todo_text>")
def todo_list_item_has_text(index: str, todo_text: str, todo_page: TodoPage):
    assert todo_page.get_list_item_text(index), todo_text


@when(parsers.parse("I type the todos '{todo_list}'"))
def i_type_the_todo(todo_list: str, todo_page: TodoPage):
    for todo_text in json.loads(todo_list):
        todo_page.add_todo(todo_text)


@then(parsers.parse("todo list items '{index_list}' have the texts '{todo_list}'"))
def todo_list_item_has_text(index_list: str, todo_list: str, todo_page: TodoPage):
    for index, todo_text in zip(json.loads(index_list), json.loads(todo_list)):
        assert todo_page.get_list_item_text(index), todo_text
