"""
workflow for any utilities needed for tests

Author:

"""
import os
import datetime
import json
import inspect
import logging


def utils_class(cls):
    """
    decoartor method for running class methods when class obj created

    Returns:
        cls[class obj]: return the class itself
    """
    # cls.parseconfigjson()
    cls.create_logfolder()
    cls.getlogger()

    return cls
@utils_class
class Utils:
    """
    workflow class for generic methods and utilities
    """

    @classmethod
    def create_logfolder(cls, test_name="test", initialize=False):
        """
        method to create log folders/files with timestamps and test name

        Args:
            test_name (str): name of the test running from process
        """
        cls.folder_created = getattr(cls, "folder_created", False)
        current_dir = os.getcwd() + os.path.sep + "results" + os.path.sep
        try:
            if not cls.folder_created:
                log_path = current_dir + datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
                cls.test_args["log_path"] = log_path
                os.makedirs(log_path)
                cls.folder_created = True
                with open("{}/debuglog.log".format(log_path), 'w'):
                    pass
        except FileExistsError:
            log_path = current_dir + datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S.%f')
            cls.test_args["log_path"] = log_path
            os.makedirs(log_path)
            cls.folder_created = True
            with open("{}/debuglog.log".format(log_path), 'w'):
                pass
        if initialize:
            cls.test_args["files_dict"] = {"weblog":"weblog.log", "archive":"archive.har"}
            for key, value in cls.test_args["files_dict"].items():
                with open("{}/{}_{}".format(cls.test_args["log_path"], test_name, value), 'w'):
                    pass
                cls.test_args["files_dict"][key] = "{}_{}".format(test_name, value)

    @classmethod
    def getlogger(cls):
        """
        logger helper for python
        Returns:
            logger(obj): logger value
        """
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)
        filehandler = logging.FileHandler(cls.test_args["log_path"] + "/debuglog.log")
        formatter = logging.Formatter("%(asctime)s :%(module)s.%(funcName)s :%(levelname)s :%(message)s")
        filehandler.setFormatter(formatter)

        logger.addHandler(filehandler)

        logger.setLevel(logging.DEBUG)
        cls.logger = getattr(cls, "logger", logger)
        cls.logger.info("=============================START===================================")
        cls.logger.debug("Created log folder at {}".format(cls.test_args["log_path"]))
        cls.logger.debug("Log folder contains {}".format(os.listdir(cls.test_args["log_path"])))
        cls.logger.debug("Config Json {}".format(cls.test_args))
    #
    # @classmethod
    # def parseconfigjson(cls):
    #     """
    #     method to parse config.json files from tests
    #     """
    #     current_dir = os.getcwd()
    #     with open(current_dir + "/tests/config.json") as jsonfile:
    #         cls.test_args = json.load(jsonfile)
