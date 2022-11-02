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
    def get_excel_file():
        xl_file = config.get('test data', 'xl_for_ddt')
        return xl_file
