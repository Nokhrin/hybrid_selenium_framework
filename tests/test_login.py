# test login into admin area

import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogGenerator


class Test_001_Login:
    """Testcase for testing login page"""
    # test variables
    base_url = ReadConfig.get_app_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()

    # logger object
    logger = LogGenerator.get_logger()

    # test methods
    @pytest.mark.fresh
    def test_homepage_title(self, setup):
        """Homepage should be like OrangeHRM"""
        self.logger.info('************Test_001_Login************')
        self.logger.info('************Verify homepage title************')
        self.driver = setup
        self.driver.get(self.base_url)
        actual_title = self.driver.title
        if actual_title == 'OrangeHRM':
            self.driver.quit()
            self.logger.info('************Homepage title test passed************')
            assert True
        else:
            self.driver.save_screenshot('screenshots/test_homepage.png')
            self.driver.quit()
            self.logger.info('************Homepage title test failed************')
            assert False

    # @pytest.mark.xfail
    def test_homepage_title_failed(self, setup):
        """Homepage should not be like not OrangeHRM"""
        self.logger.info('************Test_001_Login************')
        self.logger.info('************Verify homepage title************')
        self.driver = setup
        self.driver.get(self.base_url)
        # wait for page to load
        self.page = LoginPage(self.driver)
        self.page.load_page()
        actual_title = self.driver.title
        if actual_title == 'not-OrangeHRM':
            self.driver.quit()
            self.logger.info('************Homepage title test passed************')
            assert True
        else:
            self.driver.save_screenshot('screenshots/test_homepage.png')
            self.driver.quit()
            self.logger.info('************Homepage title test failed************')
            assert False

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.login_page_obj = LoginPage(self.driver)
        # log into admin account
        self.login_page_obj.set_username(self.username)
        self.login_page_obj.set_password(self.password)
        self.login_page_obj.click_login_button()
        # check the current url
        expected_url = 'https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList'
        actual_url = self.driver.current_url
        if actual_url == expected_url:
            self.driver.quit()
            assert True
        else:
            self.driver.save_screenshots('../screenshots/test_login.png')
            self.driver.quit()
            assert False
