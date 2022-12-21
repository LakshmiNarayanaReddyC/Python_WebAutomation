from selenium.webdriver.common.by import By
from PageLocators.CommonMethods import BaseClass
from PageLocators.LoginScreen_Locators import *
from PageLocators.Dashboard_Locators import *


class Dashboard:

    def __init__(self, driver):
        self.driver = driver
        self.baseclass = BaseClass(self.driver)

    def click_menu_button(self):
        menu_button = self.baseclass.find_element(By.XPATH, menu_icon_xpath)
        menu_button.click()


    def click_about_link(self):
        about_button = self.baseclass.find_element(By.XPATH, about_link_xpath)
        about_button.click()

    def click_logout(self):
        logout_button = self.baseclass.find_element(By.XPATH,logout_btn_xpath)
        logout_button.click()
