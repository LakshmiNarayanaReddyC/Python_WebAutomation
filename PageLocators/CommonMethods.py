from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchAttributeException, NoAlertPresentException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import datetime
import log4python
# from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select


class BaseClass:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locatortype, elementID):
        try:
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((locatortype, elementID)))
            screen_element = self.driver.find_element(locatortype, elementID)
            return screen_element
        except WebDriverException as WDE:
            if WDE.msg == "NoSuchElementError":
                raise NoSuchAttributeException(WDE.msg, WDE.stacktrace)
            else:
                raise WDE

    def find_elements(self, locatortype, elementID):
        try:
            WebDriverWait(self.driver, 30).until(EC.presence_of_all_elements_located((locatortype, elementID)))
            screen_element = self.driver.find_elements(locatortype, elementID)
            return screen_element
        except WebDriverException as WDE:
            if WDE.msg == "NoSuchElementError":
                raise NoSuchAttributeException(WDE.msg, WDE.stacktrace)
            else:
                raise WDE

    def getAttribute_Value(self, locatortype, locator, getvalue):
        try:
            WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((locatortype, locator)))
            value = self.driver.find_element(locatortype, locator).get_attribute(getvalue)
            return value
        except WebDriverException as WDE:
            if WDE.msg == "NoSuchElementError":
                raise NoSuchAttributeException(WDE.msg, WDE.stacktrace)
            else:
                raise WDE

    def enter_text(self, locatortype, locator, text):
        try:
            WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((locatortype, locator)))
            textbox = self.driver.find_element(locatortype, locator)
            textbox.click()
            textbox.clear()
            textbox.sendkeys(text)
        except WebDriverException as WDE:
            if WDE.msg == "NoSuchElementError":
                raise NoSuchAttributeException(WDE.msg, WDE.stacktrace)
            else:
                raise WDE

    def DragAndDrop(self, locatortype, source, dest):
        try:
            WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((locatortype, source)))
            source = self.driver.find_element(locatortype, source)
            target = self.driver.find_element(locatortype, dest)
            act_chains = ActionChains(self.driver)
            # act_chains.drag_and_drop(source,target).perform()
            act_chains.click_and_hold(source).move_to_element(target).release().perform()
        except WebDriverException as WDE:
            if WDE.msg == "NoSuchElementError":
                raise NoSuchAttributeException(WDE.msg, WDE.stacktrace)
            else:
                raise WDE

    def select_dropdown_text(self, locatortype, element, text):
        try:
            WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((locatortype, element)))
            select_dropdown_visible_text = Select(self.driver.find_element(locatortype, element))
            select_dropdown_visible_text.select_by_visible_text(text)
        except WebDriverException as WDE:
            if WDE.msg == "NoSuchElementError":
                raise NoSuchAttributeException(WDE.msg, WDE.stacktrace)
            else:
                raise WDE

    def select_dropdown_index(self, locatortype, element, index):
        try:
            WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((locatortype, element)))
            select_dropdown_index = Select(self.driver.find_element(locatortype, element))
            select_dropdown_index.select_by_index(index)
        except WebDriverException as WDE:
            if WDE.msg == "NoSuchElementError":
                raise NoSuchAttributeException(WDE.msg, WDE.stacktrace)
            else:
                raise WDE

    def select_dropdown_value(self, locatortype, element, value):
        try:
            WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((locatortype, element)))
            select_dropdown_value = Select(self.driver.find_element(locatortype, element))
            select_dropdown_value.select_by_value(value)
        except WebDriverException as WDE:
            if WDE.msg == "NoSuchElementError":
                raise NoSuchAttributeException(WDE.msg, WDE.stacktrace)
            else:
                raise WDE

    def get_text(self, locatortype, locator):
        try:
            WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((locatortype, locator)))
            get_text = self.driver.find_element(locatortype, locator)
            get_text.text()
        except WebDriverException as WDE:
            if WDE.msg == "NoSuchElementError":
                raise NoSuchAttributeException(WDE.msg, WDE.stacktrace)
            else:
                raise WDE

    def switch_to_frame(self, locatortype, elementXpath):
        try:
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((locatortype, elementXpath)))
            switch_frame = self.driver.switch_to_frame(locatortype, elementXpath)
            return switch_frame
        except WebDriverException as WDE:
            if WDE.msg == "NoSuchElementError":
                raise NoSuchAttributeException(WDE.msg, WDE.stacktrace)
            else:
                raise WDE

    def switch_to_default_content(self):
        try:
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(()))
            switch_default = self.driver.switch_to_default_content()
            return switch_default
        except WebDriverException as WDE:
            if WDE.msg == "NoSuchElementError":
                raise NoSuchAttributeException(WDE.msg, WDE.stacktrace)
            else:
                raise WDE

    def alert_accept(self):
        """
        Accept the alert
        Args:
            None

        Returns:
            perform alert accept
        """
        try:
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(()))
            alert = self.driver.switch_to.alert
            alert.accept()
        except WebDriverException as WDE:
            if WDE.msg == "NoSuchElementError":
                raise NoSuchAttributeException(WDE.msg, WDE.stacktrace)
            else:
                raise WDE

    def alert_dismiss(self):
        """
        Dimiss the alert
        Args:
            None

        Returns:
            perform dismiss the alert
        """
        try:
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(()))
            alert = self.driver.switch_to.alert
            alert.dismiss()
        except WebDriverException as WDE:
            if WDE.msg == "NoSuchElementError":
                raise NoSuchAttributeException(WDE.msg, WDE.stacktrace)
            else:
                raise WDE

    def alert_send_keys(self, texttoEnter):
        """
        Enter text to the alert
        Args:
            texttoEnter(String): Text to enter

        Returns:
            None
                """
        try:
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(()))
            alert = self.driver.switch_to.alert
            alert.send_keys(texttoEnter)
        except WebDriverException as WDE:
            if WDE.msg == "NoSuchElementError":
                raise NoSuchAttributeException(WDE.msg, WDE.stacktrace)
            else:
                raise WDE

    def _get_alert_text(self):
        """
        Get the text of an alert the alert
        Args:
            None

        Returns:
            It returns the text
        """
        try:
            alert = self.driver.switch_to.alert
            return alert.text()
        except WebDriverException as WDE:
            if WDE.msg == "NoSuchElementError":
                raise NoSuchAttributeException(WDE.msg, WDE.stacktrace)
            else:
                raise WDE

    def currenttime(self):
        """
        Get the current time
        Args:
            None

        Returns:
            current time
        """
        time = str(datetime.now().time())
        ctime = time.split(":")
        currenttime = ctime[0]
        currenttimet = int(currenttime)
        return currenttimet

    def switch_to_child_window(self):
        """
        Switch to child window
        Args:
            None

        Returns:
            perform action on child window
        """
        self.driver.switch_to.window(self.driver.window_handles[1])

    def switch_to_parent_window(self):
        """
        Switch to parent window
        Args:
            None

        Returns:
            perform action on parent window
        """
        self.driver.switch_to.window(self.driver.window_handles[0])
