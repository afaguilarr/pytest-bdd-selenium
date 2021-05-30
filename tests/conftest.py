from typing import Dict

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager


# Gets the headless command line argument
# execute 'pytest --headless headless' to run headless
def pytest_addoption(parser):
    parser.addoption("--headless", action="store", default="")


@pytest.fixture(scope="function")
def web_driver(pytestconfig) -> WebDriver:
    chrome_options = Options()
    if pytestconfig.getoption("headless"):
        chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    yield driver
    driver.close()
    driver.quit()


@pytest.fixture(scope="function")
def steps_context() -> Dict:
    return {
        "request": None
    }
