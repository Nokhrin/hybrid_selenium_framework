from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class EmployeesDirectory:
    """Page class for testing of searching employee on 'Directory' page"""
    # locators
    a_href_directory_xpath = "//a[@href='/web/index.php/directory/viewDirectory']"

    # page actions
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver=driver, timeout=10.0, poll_frequency=0.1)

    def open_directory(self):
        self.wait.until(EC.visibility_of_element_located(
                (By.XPATH, self.a_href_directory_xpath)
            ), message='directory link is not visible'
        ).click()
