textbox_username_id = "user-name"
textbox_password_id = "password"
submit_button_id = "login-button"
menu_icon_xpath = "//button[@id='react-burger-menu-btn']"

#
# class LoginPage:
#
#     def __init__(self, driver):
#         self.driver = driver
#         self.baseclass = BaseClass(self.driver)
#
#     def setUsername(self, username):
#         self.baseclass.find_element(By.ID, self.textbox_username).click()
#         self.baseclass.find_element(By.ID, self.textbox_username).clear()
#         self.baseclass.find_element(By.ID, self.textbox_username).send_keys(username)
#
#     def setPassword(self, password):
#         self.baseclass.find_element(By.ID, self.textbox_password).click()
#         self.baseclass.find_element(By.ID, self.textbox_password).clear()
#         self.baseclass.find_element(By.ID, self.textbox_password).send_keys(password)
#
#     def click_submit_button(self):
#         submit_button = self.baseclass.find_element(By.ID, self.submit_button)
#         submit_button.click()
