import time
import pytest
from Screens.Login_Screen import *
from utilities.readProperties import ReadConfig
from .conftest import setUp
from utilities import logger_settings
from Screens.Dashbaord_Screen import *



# from utilities.logger_settings import logger_info


class Test_DashBoardScreen():
    base_url = ReadConfig.getApplicationURL()
    uname = ReadConfig.getUserEmailL()
    passwd = ReadConfig.getUserPasswd()
    driver = setUp('Chrome')
    log = logger_settings.get_logger()

    def test_Login(self):
        self.log.info("*************** Test_001_Dashboard *****************")
        self.driver.get(self.base_url)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.passwd)
        self.lp.click_submit_button()
        time.sleep(20)
        # self.lp.click_menu_button()
        self.driver.save_screenshot(".\\Screenshots\\" + "Login.png")

    def test_Dashboard(self):
        self.log.info("*************** Test_002_Dashboard *****************")
        self.driver.implicitly_wait(10)
        self.db = (self.driver)
        self.db.click_menu_button()
        self.db.c()
        self.driver.save_screenshot(".\\Screenshots\\" + "Dashbaord.png")

    def test_logout(self):
        self.log.info("*************** Test_003_Dashboard *****************")
        self.db = Dashboard(self.driver)
        self.db.click_logout()
        self.driver.save_screenshot(".\\Screenshots\\" + "Logout.png")
