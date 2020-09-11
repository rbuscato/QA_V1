import pytest
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# in order to run from command line :
# (https://docs.pytest.org/en/latest/example/simple.html)
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )
@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="/Users/richardbuscato/chromedriver")
    elif browser_name == "firefox":
        # do firefox stuff ... gecko driver
        driver = webdriver.Firefox(executable_path="FIXME")
    elif browser_name == "IE":
        print("IE driver")
        # do IE stuff ... gecko driver

    driver.get("https://www.google.com/")
    driver.maximize_window()

    request.cls.driver = driver # make this driver available to
                                # class using this fixture.
    #     so we don't need   'return driver'
    yield
    driver.close()

