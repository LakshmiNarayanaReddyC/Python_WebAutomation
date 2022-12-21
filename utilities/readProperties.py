import configparser
import os
from datetime import datetime



# CREATE AN OBJECT FOR CONFIGPARSER
config = configparser.RawConfigParser()
# LOADING THE 'CONFIG.INI' FILE
file_path = str(os.path.abspath("Configurations\config.ini"))
# config.read("'" + file_path +"'")
config.read(r"Configurations\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        print(config)
        url = config.get("common info", "baseurl")
        return url

    @staticmethod
    def getUserEmailL():
        usrname = config.get('common info', 'username')
        return usrname

    @staticmethod
    def getUserPasswd():
        pwd = config.get('common info', 'password')
        return pwd

