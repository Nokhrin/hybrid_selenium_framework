import time
import random
import pytest
from utilities.custom_logger import LogGenerator
from utilities.read_properties import ReadConfig
from pages.login_page import LoginPage
from pages.add_employee_page import AddEmployee
from pages.employees_directory_page import EmployeesDirectory


class Test_004_SearchEmployee:
    logger = LogGenerator.generate_log()
    base_url = ReadConfig.get_app_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()

    firstname = ReadConfig.get_user_firstname()
    middlename = ReadConfig.get_user_middlename()
    lastname = ReadConfig.get_user_lastname()

    employee_username = ReadConfig.get_new_employee_username()
    employee_password = ReadConfig.get_new_employee_password()

    @pytest.mark.fresh
    def test_add_and_go_to_directory(self, setup):
        try:
            self.logger.info('*** Test_004_SearchEmployee ***')
            self.driver = setup
            self.driver.get(url=self.base_url)
            self.driver.maximize_window()

            self.login_page = LoginPage(driver=self.driver)
            self.logger.info('*** log into admin account ***')
            self.login_page.set_username(username=self.username)
            self.login_page.set_password(password=self.password)
            self.login_page.click_login_button()

            # add new employee
            self.add_employee_page = AddEmployee(driver=self.driver)
            self.logger.info('*** go to PIM page ***')
            self.add_employee_page.click_pim_link()
            self.logger.info('*** go to Add Employee page ***')
            self.add_employee_page.click_add_button()
            self.logger.info('fill user data')
            self.add_employee_page.write_first_name(self.firstname)
            self.add_employee_page.write_middle_name(self.middlename)
            self.add_employee_page.write_last_name(self.lastname)
            self.add_employee_page.click_login_details()
            self.add_employee_page.fill_in_username(self.employee_username + str(random.randint(1, 999)))
            self.add_employee_page.fill_in_password(self.employee_password)
            self.add_employee_page.fill_in_confirm_password(self.employee_password)
            self.add_employee_page.click_save_employee()

            # test IDEA - check search/reset functionality:
            # - go to directory page
            # - get total of records
            # - filter by location (title/name/etc)
            # - get new total of records
            # - make sure the total is different
            # - reset search
            # - make sure the total is the same as initial

            self.logger.info('!!!!!!!!!!!!!!!!!!!!!')
            self.logger.info('before switching to directory')
            self.logger.info(f'current url: {self.driver.current_url}')
            self.logger.info(f'current title: {self.driver.title}')

            # go to directory page
            self.directory_page = EmployeesDirectory(driver=self.driver)
            self.logger.info('!!!!!!!!!!!!!!!!!!!!!')
            self.logger.info(f'switch to directory')
            self.directory_page.open_directory()

            self.logger.info(f'here is the implicit wait for url to change')
            self.logger.info(f'current url: {self.driver.current_url}')
            self.logger.info(f'current title: {self.driver.title}')
            self.logger.info(f'total records found: {self.directory_page.get_records_found()}')

            self.directory_page.search_employee_by_title('a')
            time.sleep(5)
            self.directory_page.click_search_button()
            time.sleep(5)
            initial_total = self.directory_page.get_records_found()
            self.logger.info(f'records found after search: {self.directory_page.get_records_found()}')

            self.directory_page.click_reset_button()
            time.sleep(5)
            self.logger.info(f'records found after reset: {self.directory_page.get_records_found()}')

            final_total = self.directory_page.get_records_found()

            assert initial_total == final_total

        finally:
            self.driver.quit()
            self.logger.info('*** quit webdriver ***')
            self.logger.info('*** Test_003_AddEmployee FINISHED ***')
