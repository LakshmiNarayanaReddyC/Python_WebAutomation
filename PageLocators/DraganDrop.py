from selenium.webdriver.common.by import By
from PageLocators.CommonMethods import BaseClass


class DragDrop:
    # drag = "draggable"
    # drop = "droppable"
    select_value ="//select[@id='Form_getForm_Country']/option"
    # value='India'

    def __init__(self, driver):
        self.driver = driver
        self.baseclass = BaseClass(self.driver)

    def selectvalue(self):
        self.baseclass.select_dropdown_value(By.ID, self.select_value , 4)


    # def dragable(self):
    #     self.baseclass.DragAndDrop(By.ID, self.drag, self.drop)
