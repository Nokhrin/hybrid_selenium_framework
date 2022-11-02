# test login into admin area
from utilities import XLUtils
from pages.login_page import LoginPage
from utilities.read_properties import ReadConfig
from utilities.custom_logger import generate_log
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))


class Test_002_DDT_Login:
    """Testcase for testing login page"""
    # test variables
    base_url = ReadConfig.get_app_url()
    path = ReadConfig.get_excel_file()
    expected_url = ReadConfig.get_expected_url()

    # logger object
    logger = generate_log()

    # test methods
    def test_login(self, setup):
        self.logger.info('*** Test_002_DDT_Login ***')
        self.logger.info('*** Verify login DDT test ***')
        self.driver = setup
        self.driver.get(self.base_url)

        self.login_page_obj = LoginPage(self.driver)

        # get data from excel file for DDT
        self.rows = XLUtils.getRowCount(file=self.path, sheetName='Sheet1')

        status_list = []

        for r in range(2, self.rows + 1):  # first row is the header
            self.logger.info('*** Read data from xl ***')
            self.username = XLUtils.readData(file=self.path,
                                             sheetName='Sheet1',
                                             rownum=r,
                                             columnno=1)
            self.password = XLUtils.readData(file=self.path,
                                             sheetName='Sheet1',
                                             rownum=r,
                                             columnno=2)
            self.expected = XLUtils.readData(file=self.path,
                                             sheetName='Sheet1',
                                             rownum=r,
                                             columnno=3)

            # log into admin account
            self.login_page_obj.set_username(self.username)
            self.login_page_obj.set_password(self.password)
            self.login_page_obj.click_login_button()

            # check the current url
            actual_url = self.driver.current_url

            if actual_url == self.expected_url:
                if self.expected == 'Pass':
                    self.logger.info('*** Passed ***')
                    # log out from account
                    self.login_page_obj.open_profile_menu()
                    self.login_page_obj.log_out()
                    status_list.append('Pass')
                elif self.expected == 'Fail':
                    self.logger.info('*** Failed ***')
                    # log out from account
                    self.login_page_obj.open_profile_menu()
                    self.login_page_obj.log_out()
                    status_list.append('Fail')

            elif actual_url != self.expected_url:
                if self.expected == 'Pass':
                    self.logger.info('*** Failed ***')
                    status_list.append('Fail')
                elif self.expected == 'Fail':
                    self.logger.info('*** Passed ***')
                    status_list.append('Pass')

        self.logger.info('*** Quit the browser ***')
        self.driver.quit()

        if 'Fail' not in status_list:
            self.logger.info('*** Login test passed ***')
            assert True
        else:
            self.logger.info('*** Login test failed ***')
            assert False

        self.logger.info('**** End of DDT for Login ****')
        self.logger.info('*** Completed Test_002_DDT_Login ***')
