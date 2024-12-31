import json
import pytest
from appium import webdriver
import os

@pytest.fixture(scope="session")
def capabilities():
    with open(os.path.join('config', 'capabilities.json')) as cap_file:
        return json.load(cap_file)

@pytest.fixture(scope="session")
def driver(capabilities):
    driver = webdriver.Remote("http://localhost:4723/wd/hub", capabilities)
    yield driver
    driver.quit() 