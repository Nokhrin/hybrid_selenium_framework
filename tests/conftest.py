# setup fixture
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service as CS
from selenium.webdriver.firefox.service import Service as FS
from selenium.webdriver.edge.service import Service as ES


@pytest.fixture()
def setup(browser):
    if browser == 'edge':
        driver_path = '/home/nohal/practicing/auto_testing/selenium_projects/drivers/msedgedriver'
        service = ES(executable_path=driver_path)
        driver = webdriver.Edge(service=service)
    elif browser == 'firefox':
        driver_path = '/home/nohal/practicing/auto_testing/selenium_projects/drivers/geckodriver'
        service = FS(executable_path=driver_path)
        driver = webdriver.Firefox(service=service)
    else:
        # chrome by default
        driver_path = '/home/nohal/practicing/auto_testing/selenium_projects/drivers/chromedriver'
        service = CS(executable_path=driver_path)
        driver = webdriver.Chrome(service=service)
    return driver


def pytest_addoption(parser):
    """Get value from CLI"""
    parser.addoption('--browser')


@pytest.fixture()
def browser(request):
    if request.config.getoption('--browser'):
        return request.config.getoption('--browser').lower()


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
