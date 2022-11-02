# log into admin area
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    img_logo_xpath = "//img[ancestor::div[@class='orangehrm-login-logo']]"
    textbox_username_xpath = "//input[@name='username']"
    textbox_password_xpath = "//input[@name='password']"
    button_login_xpath = "//button[contains(@class, 'login-button')]"
    span_usermenu_xpath = "//span[contains(@class, 'userdropdown')]"
    link_logout_linktext = "//a[text()='Logout']"

    # page constructor
    def __init__(self, driver):
        """Take driver from the testcase"""
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout=10, poll_frequency=1)

    # page actions
    def load_page(self):
        self.wait.until(EC.presence_of_element_located(
                            (By.XPATH, self.img_logo_xpath)
                            )
                        )

    def set_username(self, username):
        textbox_username_element = self.wait.until(
                EC.visibility_of_element_located(
                        (By.XPATH, self.textbox_username_xpath)
                    ), message='username textbox is not visible'
                )
        textbox_username_element.clear()
        textbox_username_element.send_keys(username)

    def set_password(self, password):
        textbox_password = self.wait.until(
                EC.visibility_of_element_located(
                        (By.XPATH, self.textbox_password_xpath)
                    ), message='password textbox is not visible'
                )
        textbox_password.clear()
        textbox_password.send_keys(password)

    def click_login_button(self):
        login_button = self.wait.until(
                EC.element_to_be_clickable(
                        (By.XPATH, self.button_login_xpath)
                    ), message='login button is not clickable'
                )
        login_button.click()

    def open_profile_menu(self):
        profile_link = self.wait.until(
                EC.element_to_be_clickable(
                        (By.XPATH, self.span_usermenu_xpath)
                    ), message="profile link is not clickable"
                )
        profile_link.click()

    def log_out(self):
        logout_link = self.wait.until(
                EC.visibility_of_element_located(
                        (By.XPATH, self.link_logout_linktext)
                    ), message="logout link is not located"
                )
        logout_link.click()
