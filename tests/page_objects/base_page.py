from typing import Tuple

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):

    base_url = 'http://testdouble.github.io/'
    url_path = None

    def __init__(self, driver: webdriver):
        self.driver = driver

    def get_url(self, params: str = "") -> str:
        return f"{self.base_url}{self.url_path}{params}"

    def open(self, params: str = "") -> 'BasePage':
        self.driver.get(self.get_url(params))
        return self

    def _find(self, locator, timeout: int = 5) -> WebElement:
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException:
            raise TimeoutException(f"Couldn't find the locator {locator}")

    def _is_element_present(self, locator, timeout: int = 5):
        try:
            self._find(locator, timeout)
        except TimeoutException:
            return False
        return True

    def _find_all(self, locator):
        try:
            return WebDriverWait(self.driver, 5).until(
                EC.presence_of_all_elements_located(locator)
            )
        except TimeoutException:
            raise TimeoutException(f"Couldn't find the locator {locator}")

    def _type(self, locator, text):
        text_area = self._find(locator)
        text_area.clear()
        text_area.send_keys(text)
        return self

    def _click(self, locator):
        element = self._find(locator)
        element.click()
        return self

    @staticmethod
    def build_locator_by_css(css_selector: str, params: str = "") -> Tuple:
        if params:
            css_selector = css_selector.format(params)
        return By.CSS_SELECTOR, css_selector
