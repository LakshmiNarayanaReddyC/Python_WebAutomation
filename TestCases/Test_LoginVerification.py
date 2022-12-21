import time

import pytest
# from PageLocators.LoginScreen_Locators import LoginPage
from Screens.Login_Screen import *
# from PageLocators.Dashboard_Locators import DashBoardPage
from utilities.readProperties import ReadConfig
from .conftest import setUp
# from utilities.logger_settings import logger_info
from utilities import logger_settings


class Test_LoginScreen():
    base_url = ReadConfig.getApplicationURL()
    uname = ReadConfig.getUserEmailL()
    passwd = ReadConfig.getUserPasswd()
    driver = setUp('Chrome')
    log = logger_settings.get_logger()

    @pytest.fixture()
    def set_up(self):
        self.log.info("*************** Test_001_Login *****************")
        self.log.info("****Started Home page title test ****")
        self.log.info("Welcome web application")
        self.driver.get(self.base_url)
        act_title = self.driver.title
        if act_title == "Swag Labs":
            self.log.info("**** Home page title test passed ****")
            assert True
        else:
            self.log.info("**** Home page title test failed****")
            self.driver.save_screenshot(".\\Screenshots\\" + "HomepageTitle.png")
            assert False
        # yield "resource"
        # self.driver.quit()

    def test_Login(self, set_up):
        self.log.info("****Started Login Test****")
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.passwd)
        self.lp.click_submit_button()
        # self.lp.click_menu_button()
        self.driver.save_screenshot(".\\Screenshots\\" + "Login.png")

    def test_Dashboard(self):
        self.log.info("****Navigate to Dashboard Screen****")
        time.sleep(30)
        self.lp.click_menu_button()
        # self.db.menu_icon()
        # self.db.about_link()
        self.driver.save_screenshot(".\\Screenshots\\" + "Dashbaord.png")
