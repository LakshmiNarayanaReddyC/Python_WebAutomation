# from selenium.webdriver.common.by import By
# from PageLocators.CommonMethods import BaseClass

menu_icon = "//button[@id='react-burger-menu-btn']"
about_link_xpath = "//a[@id='about_sidebar_link']"
logout_btn_xpath = "//a[text()='Logout']"
menu_icon_xpath = "//button[@id='react-burger-menu-btn']"
#
# class DashBoardPage:
#     menu_icon = "//button[@id='react-burger-menu-btn']"
#     about_link = "//a[@id='about_sidebar_link']"
#     logout_btn = "//a[text()='Logout']"
#
#     def __init__(self, driver):
#         self.driver = driver
#         self.baseclass = BaseClass(self.driver)
#
#     def click_menu_button(self):
#         menu_button = self.baseclass.find_element(By.XPATH, self.menu_icon)
#         menu_button.click()
#
#     def click_about_link(self):
#         about_button = self.baseclass.find_element(By.XPATH, self.about_link)
#         about_button.click()
#
#     def click_logout(self):
#         logout_button = self.baseclass.find_element(By.XPATH, self.logout_btn)
#         logout_button.click()
