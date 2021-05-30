from typing import Tuple

from tests.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class TodoPage(BasePage):
    url_path = "todos/"
    ADD_TODO_LOCATOR = (By.ID, 'new-todo')
    LIST_ITEM_BASE_LOCATOR = "#todo-list li:nth-child({})"

    def __init__(self, driver):
        super().__init__(driver)

    def add_todo(self, text: str):
        return self._type(self.ADD_TODO_LOCATOR, f"{text}\n")

    def get_list_item_text(self, index: str) -> str:
        return self._find(self.get_list_item_locator(index)).text

    def get_list_item_locator(self, index: str) -> Tuple:
        return TodoPage.build_locator_by_css(self.LIST_ITEM_BASE_LOCATOR, index)
