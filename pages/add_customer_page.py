from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class AddCustomer:
    """
    Page for adding the customer
    """
    # locators
    link_pim_xpath = "//a[@href='/web/index.php/pim/viewPimModule']//span"
    link_add_employee_xpath = "//li[@class='oxd-topbar-body-nav-tab']//a[text()='Add Employee']"
    button_add_employee_xpath = "//div[@class='orangehrm-header-container']//button"

    # action methods for locators
    def __init__(self, driver):
        """Initiate webdriver"""
        self.driver = driver
        self.wait = WebDriverWait(driver=self.driver, timeout=3, poll_frequency=1)

    def click_pim_link(self):
        self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, self.link_pim_xpath)
            ), message='pim link can\'t be clicked'
        ).click()

    def click_employee_link(self):
        self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, self.link_add_employee_xpath)
            ), message='add employee link can\'t be clicked'
        )

    def click_add_button(self):
        self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, self.button_add_employee_xpath)
            ), message='add employee button can\'t be clicked'
        )
