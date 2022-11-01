# utility for logging testcases
import logging
import logging.config

#
# class LogGenerator:
#     # @staticmethod
#     def generate_log():
#         # logging.basicConfig(filename='./automation.log',
#         #                     filemode='w',
#         #                     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#         #                     datefmt='%d-%b-%y %H:%M:%S',
#         #                     )
#         # logging.basicConfig(filename='automation.log')
#         # logging.config.fileConfig('configurations/logging.conf')
#         logger = logging.getLogger('Test Logger')
#         logger.setLevel(logging.DEBUG)
#
#         # logs for writing to file
#         file_h = logging.FileHandler(filename='automation.log')
#         file_h.setLevel(logging.DEBUG)
#
#         # logs for writing to console
#         cons_h = logging.StreamHandler()
#         cons_h.setLevel(logging.ERROR)
#
#         # define formatting
#         formatter = logging.Formatter(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#         file_h.setFormatter(formatter)
#         cons_h.setFormatter(formatter)
#
#         # attach handlers to the logger
#         logger.addHandler(file_h)
#         logger.addHandler(cons_h)
#
#         return logger


def generate_log():
    logging.basicConfig(filename='./automation.log',
                        filemode='w',
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        datefmt='%d-%b-%y %H:%M:%S',
                        )

    logger = logging.getLogger('Test Logger')
    logger.setLevel(logging.DEBUG)

    # logs for writing to file
    file_h = logging.FileHandler(filename='logs/automation.log', mode='w')
    file_h.setLevel(logging.DEBUG)

    # logs for writing to console
    cons_h = logging.StreamHandler()
    cons_h.setLevel(logging.ERROR)

    # define formatting
    formatter = logging.Formatter(
            '%(asctime)s :: %(name)s :: %(levelname)-8s :: %(message)s',
            datefmt='%d-%b-%y %H:%M:%S'
            )
    file_h.setFormatter(formatter)
    cons_h.setFormatter(formatter)

    # attach handlers to the logger
    logger.addHandler(file_h)
    logger.addHandler(cons_h)

    return logger
