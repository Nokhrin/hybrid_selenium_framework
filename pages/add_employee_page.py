from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class AddEmployee:
    """
    Page for adding the employee
    """
    # locators
    link_pim_xpath = "//a[@href='/web/index.php/pim/viewPimModule']//span"
    link_add_employee_xpath = "//li[@class='oxd-topbar-body-nav-tab']//a[text()='Add Employee']"
    button_add_employee_xpath = "//div[@class='orangehrm-header-container']//button"
    input_firstname_xpath = "//input[@name='firstName' and @placeholder='First Name']"
    input_middlename_xpath = "//input[@name='middleName' and @placeholder='Middle Name']"
    input_lastname_xpath = "//input[@name='lastName' and @placeholder='Last Name']"
    input_employee_id_xpath = "//label[text()='Employee Id']/ancestor::div[@class='oxd-input-group oxd-input-field-bottom-space']//input"
    button_save_xpath = "//div[@class='oxd-form-actions']//button[@type='submit']"

    checkbox_create_login_details_xpath = "//p[text()='Create Login Details']/following-sibling::*[1]//span"
    input_username_xpath = "//label[text()='Username']/parent::*/following-sibling::*/input"
    radio_status_enabled_xpath = "//input[@type='radio' and @value='1']/following-sibling::span"
    radio_status_disabled_xpath = "//input[@type='radio' and @value='2']/following-sibling::span"
    input_password_xpath = "//label[text()='Password']/parent::*/following-sibling::*/input"
    input_confirm_password_xpath = "//label[text()='Confirm Password']/parent::*/following-sibling::*/input"

    text_actual_short_name_xpath = "//div[@class='orangehrm-edit-employee-name']/h6"
    input_saved_employee_id_xpath = "//label[text()='Employee Id']/parent::*/parent::*//input"

    # action methods for locators
    def __init__(self, driver):
        """Initiate webdriver"""
        self.driver = driver
        self.wait = WebDriverWait(driver=self.driver, timeout=10, poll_frequency=0.5)

    def click_pim_link(self):
        self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, self.link_pim_xpath)
            ), message='pim link can\'t be clicked'
        ).click()

    def click_employee_link(self):
        self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, self.link_add_employee_xpath)
            ), message='add employee link can\'t be clicked'
        ).click()

    def click_add_button(self):
        self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, self.button_add_employee_xpath)
            ), message='add employee button can\'t be clicked'
        ).click()

    # add employee
    def write_first_name(self, firstname: str):
        self.wait.until(EC.visibility_of_element_located(
                (By.XPATH, self.input_firstname_xpath)
            ), message='firstname textbox can not be located'
        ).send_keys(firstname)

    def write_middle_name(self, middlename: str):
        self.wait.until(EC.visibility_of_element_located(
                (By.XPATH, self.input_middlename_xpath)
            ), message='middlename textbox can not be located'
        ).send_keys(middlename)

    def write_last_name(self, lastname: str):
        self.wait.until(EC.visibility_of_element_located(
                (By.XPATH, self.input_lastname_xpath)
            ), message='lastname textbox can not be located'
        ).send_keys(lastname)

    def get_employee_id(self):
        return self.wait.until(EC.visibility_of_element_located(
                (By.XPATH, self.input_employee_id_xpath)
            ), message='employee id inputbox can not be found'
        ).get_attribute('value')

    def set_employee_id(self, employee_id: str):
        input_employee_id = self.wait.until(EC.visibility_of_element_located(
                (By.XPATH, self.input_employee_id_xpath)
            ), message='employee id inputbox can not be found'
        )
        input_employee_id.clear()
        input_employee_id.send_keys(employee_id)

    def click_save_employee(self):
        self.wait.until(EC.visibility_of_element_located(
                (By.XPATH, self.button_save_xpath)
            ), message='save employee button can not be clicked'
        ).click()

    def click_login_details(self):
        self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, self.checkbox_create_login_details_xpath)
            ), message='login details can not be clicked'
        ).click()

    def fill_in_username(self, username):
        self.wait.until(EC.visibility_of_element_located(
                (By.XPATH, self.input_username_xpath)
            ), message='username textbox can not be located'
        ).send_keys(username)

    def click_disabled_button(self):
        self.wait.until(EC.visibility_of_element_located(
                (By.XPATH, self.radio_status_disabled_xpath)
            ), message='disabled button can not be clicked'
        ).click()

    def click_enabled_button(self):
        self.wait.until(EC.visibility_of_element_located(
                (By.XPATH, self.radio_status_enabled_xpath)
            ), message='enabled button can not be clicked'
        ).click()

    def fill_in_password(self, password):
        self.wait.until(EC.visibility_of_element_located(
                (By.XPATH, self.input_password_xpath)
            ), message='password textbox can not be located'
        ).send_keys(password)

    def fill_in_confirm_password(self, password):
        self.wait.until(EC.visibility_of_element_located(
                (By.XPATH, self.input_confirm_password_xpath)
            ), message='confirm password textbox can not be located'
        ).send_keys(password)

    def get_saved_employee_id(self):
        return self.wait.until(EC.visibility_of_element_located(
                (By.XPATH, self.input_saved_employee_id_xpath)
            ), message='employee id can not be found'
        ).get_attribute('value')

    def get_employee_short_name(self):
        try:
            return self.wait.until(EC.presence_of_element_located(
                    (By.XPATH, self.text_actual_short_name_xpath)
                ), message='short name can not be found'
            ).get_attribute('textContent')
        except TimeoutException:
            return 'timeout for short name'
