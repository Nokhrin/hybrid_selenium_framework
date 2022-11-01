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
