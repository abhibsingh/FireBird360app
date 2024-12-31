import json
import pytest
from appium import webdriver
import os
from config.env_config import get_config

@pytest.fixture(scope="session")
def capabilities():
    config = get_config()
    with open(os.path.join('config', 'capabilities.json')) as cap_file:
        caps = json.load(cap_file)
        caps["app"] = config["APK_PATH"]
        return caps

@pytest.fixture(scope="session")
def driver(capabilities):
    driver = webdriver.Remote("http://localhost:4723/wd/hub", capabilities)
    yield driver
    driver.quit() 