from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class EmployeeDetails:
    """
    Page with personal information of the account
    """
    # locators
    input_firstname_xpath = ""
    input_middlename_xpath = ""
    input_lastname_xpath = ""
    input_employee_id_xpath = ""

    # actions
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver=driver, timeout=5, poll_frequency=1)

    def get_firstname(self):
        pass

    def get_middlename(self):
        pass

    def get_lastname(self):
        pass

    def get_employee_id(self):
        pass
