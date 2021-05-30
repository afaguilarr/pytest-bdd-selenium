from typing import Dict

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def web_driver() -> WebDriver:
    driver = webdriver.Chrome(ChromeDriverManager().install())
    yield driver
    driver.close()
    driver.quit()


@pytest.fixture(scope="function")
def steps_context() -> Dict:
    return {
        "request": None
    }
