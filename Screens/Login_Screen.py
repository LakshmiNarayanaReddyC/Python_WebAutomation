from selenium.webdriver.common.by import By
from PageLocators.CommonMethods import BaseClass
from PageLocators.LoginScreen_Locators import *


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.baseclass = BaseClass(self.driver)

    def setUsername(self, username):
        self.baseclass.find_element(By.ID, textbox_username_id).click()
        self.baseclass.find_element(By.ID, textbox_username_id).clear()
        self.baseclass.find_element(By.ID, textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.baseclass.find_element(By.ID, textbox_password_id).click()
        self.baseclass.find_element(By.ID, textbox_password_id).clear()
        self.baseclass.find_element(By.ID, textbox_password_id).send_keys(password)

    def click_submit_button(self):
        submit_button = self.baseclass.find_element(By.ID, submit_button_id)
        submit_button.click()

    def click_menu_button(self):
        menu_button = self.baseclass.find_element(By.XPATH, menu_icon_xpath)
        menu_button.click()
