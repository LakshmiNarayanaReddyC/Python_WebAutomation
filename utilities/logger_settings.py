# import sys
# import logging
# from logging.config import dictConfig
#
#
# logging_config = dict(
#     version=1,
#     formatters={
#         'verbose': {
#             'format': ("[%(asctime)s] %(levelname)s "
#                        "[%(name)s:%(lineno)s] %(message)s"),
#             'datefmt': "%d/%b/%Y %H:%M:%S",
#
#         },
#         'simple': {
#             'format': '%(levelname)s %(message)s',
#         },
#     },
#     handlers={
#         'logger-info': {'class': 'logging.handlers.RotatingFileHandler',
#                        'formatter': 'verbose',
#                        'level': logging.DEBUG,
#                        'filename': '.\\LogFolder\\automation.log',
#                        'maxBytes': 52428800,
#                        'backupCount': 7},
#         'batch-process-logger': {'class': 'logging.handlers.RotatingFileHandler',
#                                  'formatter': 'verbose',
#                                  'level': logging.DEBUG,
#                                  'filename': '.\\LogFolder\\automation.log',
#                                  'maxBytes': 52428800,
#                                  'backupCount': 7},
#         'console': {
#             'class': 'logging.StreamHandler',
#             'level': 'DEBUG',
#             'formatter': 'simple',
#             'stream': sys.stdout,
#         },
#     },
#     loggers={
#         'logger_info': {
#             'handlers': ['logger-info', 'console'],
#             'level': logging.DEBUG
#         },
#         'batch_process_logger': {
#             'handlers': ['batch-process-logger', 'console'],
#             'level': logging.DEBUG
#         }
#     }
# )
#
# dictConfig(logging_config)
#
# logger_info = logging.getLogger('logger_info')
# batch_process_logger = logging.getLogger('batch_process_logger')


import inspect
import logging
from pathlib import Path

from utilities import file_utils


def get_logger(log_level=logging.INFO):
    root_path = str(Path(__file__).parent.parent)
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)
    file_utils.create_folder(root_path + '/logs/')
    file_handler = logging.FileHandler(root_path + '/logs/' + 'logfile.log')
    formatter = logging.Formatter("%(asctime)s : %(levelname)s :%(name)s :%(message)s")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.setLevel(log_level)
    return logger
