# log into admin area
from selenium import webdriver
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

    # page actions
    def load_page(self):
        wait = WebDriverWait(self.driver, timeout=5, poll_frequency=1)
        img_logo_element = wait.until(EC.presence_of_element_located((By.XPATH, self.img_logo_xpath)))

    def set_username(self, username):
        wait = WebDriverWait(self.driver, timeout=10, poll_frequency=1)
        textbox_username_element = wait.until(EC.visibility_of_element_located((By.XPATH, self.textbox_username_xpath)))
        textbox_username_element.clear()
        textbox_username_element.send_keys(username)

    def set_password(self, password):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def open_profile_menu(self):
        self.driver.find_element(By.XPATH, self.span_usermenu_xpath).click()

    def log_out(self):
        self.driver.find_element(By.XPATH, self.link_logout_linktext).click()
