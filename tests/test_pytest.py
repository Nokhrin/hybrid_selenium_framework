# test login into admin area
import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from pages.login_page import LoginPage
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogGenerator


# test var
# logger object
# logger = LogGenerator.generate_log()


# test methods
def test_logging():
    """Homepage should be like OrangeHRM"""
    print('logger should be here')
    logger = LogGenerator.generate_log()
    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warn message')
    logger.error('error message')
    logger.critical('critical message')
