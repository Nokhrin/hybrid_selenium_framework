from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class EmployeesDirectory:
    """Page class for testing of searching employee on 'Directory' page"""
    # locators
    a_href_directory_xpath = "//a[@href='/web/index.php/directory/viewDirectory']"
    textbox_employee_name_search_xpath = "//div[contains(@class,'oxd-autocomplete-text-input')]/input"
    div_employee_name_dropdown_xpath = "//div[@class='oxd-autocomplete-dropdown --position-bottom']"

    dropdown_div_job_title_xpath = "//label[text()='Job Title']/parent::div/parent::div//div[@class='oxd-select-text-input']"
    div_job_title_account_assistant_xpath = "//div[text()='Account Assistant']"

    dropdown_div_location_xpath = "//label[text()='Location']/parent::div/parent::div//div[@class='oxd-select-text-input']"

    button_search_xpath = "//button[@type='submit']"
    button_reset_xpath = "//button[@type='reset']"

    text_records_found_xpath = "//span[contains(.,'Records Found')]"

    # page actions
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver=driver, timeout=10.0, poll_frequency=0.1)

    def open_directory(self):
        self.wait.until(EC.visibility_of_element_located(
                (By.XPATH, self.a_href_directory_xpath)
            ), message='directory link is not visible'
        ).click()
        # wait until url change
        self.wait.until(EC.url_to_be(
            "https://opensource-demo.orangehrmlive.com/web/index.php/directory/viewDirectory"
            ), message='url had not changed'
        )

    def set_employee_name(self, employee_name):
        self.wait.until(EC.presence_of_element_located(
                (By.XPATH, self.textbox_employee_name_search_xpath)
            ), message='employee name can not be set'
        ).send_keys(employee_name)

    def pick_employee_name(self, employee_fullname):
        print(self.wait.until(EC.presence_of_element_located(
            (By.XPATH, self.div_employee_name_dropdown_xpath))
        ).get_attribute('value')
        )

        self.wait.until(EC.text_to_be_present_in_element(
                (By.XPATH, self.div_employee_name_dropdown_xpath),
                text_=employee_fullname
            ), message=f'{employee_fullname} is not presented'
        ).click()

    def search_employee_by_title(self, employee_title):
        """
        Dropdown is implemented as div.
        To pick an item do next:
        - click div when it's clickable
        - navigate a value based on it's text when it's visible
        - click a value when it's clickable
        """
        self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, self.dropdown_div_job_title_xpath)
            ), message='dropdown_div_job_title can\'t be clicked'
        ).click()

        self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, self.dropdown_div_job_title_xpath)
            ), message='job title can not be sent'
        ).send_keys(employee_title)
        
        self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, self.dropdown_div_job_title_xpath)
            ), message='dropdown_div_job_title can\'t be clicked'
        ).click()

    def pick_location_from_div_dropdown(self, employee_location):
        """
        Dropdown is implemented as div.
        To pick an item do next:
        - click div when it's clickable
        - navigate a value based on it's text when it's visible
        - click a value when it's clickable
        """
        self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, self.dropdown_div_location_xpath)
        ))

    def click_search_button(self):
        self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, self.button_search_xpath)
            ), message='search can not be clicked'
        ).click()

    def click_reset_button(self):
        self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, self.button_reset_xpath)
            ), message='reset can not be clicked'
        ).click()

    def get_records_found(self):
        records_str = self.wait.until(EC.presence_of_element_located(
                (By.XPATH, self.text_records_found_xpath)
            ), message='total can not be located'
        ).text
        if records_str != 'No Records Found':
            records_str = records_str.split(sep=' ')[0][1:-1]
        return records_str
