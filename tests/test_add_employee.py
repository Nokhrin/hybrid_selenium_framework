import random
import string
from utilities.custom_logger import LogGenerator
from utilities.read_properties import ReadConfig
from pages.login_page import LoginPage
from pages.add_employee_page import AddEmployee
import time


class Test_003_AddEmployee:
    logger = LogGenerator.generate_log()
    base_url = ReadConfig.get_app_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()

    firstname = ReadConfig.get_user_firstname()
    middlename = ReadConfig.get_user_middlename()
    lastname = ReadConfig.get_user_lastname()

    employee_username = ReadConfig.get_new_employee_username()
    employee_password = ReadConfig.get_new_employee_password()
    expected_employee_url = ReadConfig.get_expected_employee_url()
    expected_employee_short_name = ReadConfig.get_expected_employee_short_name()

    def test_add_employee(self, setup):
        try:
            self.logger.info('*** Test_003_AddEmployee ***')
            self.driver = setup
            self.driver.get(url=self.base_url)
            self.driver.maximize_window()

            self.login_page = LoginPage(driver=self.driver)
            self.logger.info('*** log into admin account ***')
            self.login_page.set_username(username=self.username)
            self.login_page.set_password(password=self.password)
            self.login_page.click_login_button()

            self.add_employee = AddEmployee(driver=self.driver)
            self.logger.info('*** go to PIM page ***')
            self.add_employee.click_pim_link()

            self.logger.info('*** go to Add Employee page ***')
            self.add_employee.click_add_button()

            self.logger.info(f'current url: {self.driver.current_url}')
            self.logger.info(f'current title: {self.driver.title}')

            # fill employee data
            self.logger.info('fill user data')
            self.add_employee.write_first_name(self.firstname)
            self.add_employee.write_middle_name(self.middlename)
            self.add_employee.write_last_name(self.lastname)

            # time.sleep(5)
            # self.expected_employee_id = str(random.randint(1, 9999999999))
            # self.logger.info(f'set random employee id: {self.expected_employee_id}')
            # self.add_employee.set_employee_id(self.expected_employee_id)

            self.expected_employee_id = self.add_employee.get_employee_id()

            self.add_employee.click_login_details()

            self.logger.info(f'try to use username: {self.employee_username + self.expected_employee_id}')
            self.add_employee.fill_in_username(self.employee_username + self.expected_employee_id)
            self.add_employee.click_disabled_button()
            self.add_employee.click_enabled_button()

            self.logger.info(f'try to use password: {self.employee_password}')
            self.add_employee.fill_in_password(self.employee_password)
            self.add_employee.fill_in_confirm_password(self.employee_password)

            self.add_employee.click_save_employee()
            self.logger.info(f'data for employee # {self.expected_employee_id} has been saved')

            # verification of employee created
            # IDEA - if all 3 checks are passed, employee account was created correctly
            # - check url - we expect page with account info
            # - check employee id - should match with one generated on adding
            # - check employee short name - should match 'firstname' + 'lastname' provided on adding

            self.logger.info('***** verify data for created employee *****')
            time.sleep(10)  # TODO - figure out how to wait correctly

            # get employee id
            self.logger.info('*** verify employee id ***')
            self.logger.info(f'expected: {self.expected_employee_id}')
            self.actual_employee_id = self.add_employee.get_saved_employee_id()
            self.logger.info(f'actual: {self.actual_employee_id}')

            # get employee short name
            self.logger.info('*** verify short name ***')
            self.logger.info(f'expected short name: {self.expected_employee_short_name}')
            self.actual_employee_short_name = self.add_employee.get_employee_short_name()
            self.logger.info(f'actual short name: {self.actual_employee_short_name}')

            # get url - after employee id and short name - to guaranty the load of the employee details page
            self.current_url = self.driver.current_url
            self.current_url = self.current_url[:self.current_url.rfind('/') + 1]
            self.logger.info(f'current_url: {self.current_url}')

            # check all 3 conditions
            if self.current_url == self.expected_employee_url and \
                    self.expected_employee_id == self.actual_employee_id and \
                    self.expected_employee_short_name == self.actual_employee_short_name:
                assert True
            else:
                if self.current_url != self.expected_employee_url:
                    self.logger.warning(f'{self.current_url} not equal {self.expected_employee_url}')
                if self.expected_employee_id != self.actual_employee_id:
                    self.logger.warning(f'{self.expected_employee_id} not equal {self.actual_employee_id}')
                if self.expected_employee_short_name != self.actual_employee_short_name:
                    self.logger.warning(f'{self.expected_employee_short_name} not equal {self.actual_employee_short_name}')
                assert False, 'see log file for warnings'

        finally:
            self.driver.quit()
            self.logger.info('*** quit webdriver ***')
            self.logger.info('*** Test_003_AddEmployee FINISHED ***')
