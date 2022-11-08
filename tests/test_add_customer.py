from utilities.custom_logger import LogGenerator
from utilities.read_properties import ReadConfig
from pages.login_page import LoginPage
from pages.add_customer_page import AddCustomer


class Test_003_AddCustomer:
    logger = LogGenerator.generate_log()
    base_url = ReadConfig.get_app_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()

    def test_add_customer(self, setup):
        try:
            self.logger.info('*** Test_003_AddCustomer ***')
            self.driver = setup
            self.driver.get(url=self.base_url)
            self.driver.maximize_window()

            self.login_page = LoginPage(driver=self.driver)
            self.logger.info('*** log into admin account ***')
            self.login_page.set_username(username=self.username)
            self.login_page.set_password(password=self.password)
            self.login_page.click_login_button()

            self.add_customer_page = AddCustomer(driver=self.driver)
            self.logger.info('*** go to PIM page')
            self.add_customer_page.click_pim_link()

            self.logger.info('*** go to Add Customer page')
            self.add_customer_page.click_add_button()

            self.logger.info(f'current url: {self.driver.current_url}')
            self.logger.info(f'current title: {self.driver.title}')
        finally:
            self.driver.quit()
            self.logger.info('*** quit webdriver ***')
        self.logger.info('*** Test_003_AddCustomer FINISHED ***')
