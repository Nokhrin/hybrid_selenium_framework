# read data from ini file
import configparser


config = configparser.RawConfigParser()
config.read('configurations/config.ini')


class ReadConfig():
    @staticmethod  # to call method without creating the object
    def get_app_url():
        url = config.get('common data', 'base_url')
        return url

    @staticmethod
    def get_username():
        username = config.get('common data', 'username')
        return username

    @staticmethod
    def get_password():
        password = config.get('common data', 'password')
        return password

    @staticmethod
    def get_expected_url():
        password = config.get('common data', 'expected_url')
        return password

    @staticmethod
    def get_user_firstname():
        return config.get('new employee data', 'firstname')

    @staticmethod
    def get_user_middlename():
        return config.get('new employee data', 'middlename')

    @staticmethod
    def get_user_lastname():
        return config.get('new employee data', 'lastname')

    @staticmethod
    def get_new_employee_username():
        return config.get('new employee data', 'username')

    @staticmethod
    def get_new_employee_password():
        return config.get('new employee data', 'password')

    @staticmethod
    def get_expected_employee_short_name():
        return config.get('new employee data', 'short_name')

    @staticmethod
    def get_expected_employee_url():
        return config.get('new employee data', 'expected_employee_url')

    @staticmethod
    def get_excel_file():
        xl_file = config.get('test data', 'xl_for_ddt')
        return xl_file
