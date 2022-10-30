# utility for logging testcases

import logging


class LogGenerator(object):
    """docstring for LogGenerator."""

    @staticmethod
    def get_logger():
        logging.basicConfig(filename='logs/automation.log',
                            filemode='w',
                            format='%(name)s - %(levelname)s - %(message)s'
                            )
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
