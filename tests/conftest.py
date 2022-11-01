# setup fixture
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver_path = '/home/nohal/practicing/auto_testing/selenium_projects/drivers/chromedriver'
        service = Service(executable_path=driver_path)
        driver = webdriver.Chrome(service=service)
    else:
        driver_path = '/home/nohal/practicing/auto_testing/selenium_projects/drivers/geckodriver'
        service = Service(executable_path=driver_path)
        driver = webdriver.Firefox(service=service)
    return driver


def pytest_addoption(parser):
    """Get value from CLI"""
    parser.addoption('--browser')


@pytest.fixture()
def browser(request):
    return request.config.getoption('--browser')


# ==> Pytest HTML Report
def pytest_configure(config):
    """Hook for Adding Environment"""
    config._metadata['Project Name'] = 'Orange'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Aleksandr Nokhrin'


def pytest_metadata(metadata):
    """Hook to modify Env info in report"""
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Plugins', None)
