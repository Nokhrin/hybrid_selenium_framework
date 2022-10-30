# setup fixture
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def setup():
    driver_path = '/home/nohal/practicing/auto_testing/selenium_projects/drivers/chromedriver'
    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service)
    return driver
