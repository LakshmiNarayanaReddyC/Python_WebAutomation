import pytest
from PageLocators.DraganDrop import DragDrop
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
# from utilities.logger_settings import logger_info

# def test_drag():
#     driver = webdriver.Chrome(ChromeDriverManager().install())
#     driver.implicitly_wait(10)
#     # logger_info.info("*************** Test_001_Login *****************")
#     # logger_info.info("****drag and drop method ****")
#     driver.get('https://jqueryui.com/resources/demos/droppable/default.html')
#     dd = DragDrop(driver)
#     dd.dragable()

def test_value():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(30)
    driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")
    driver.maximize_window()
    dd = DragDrop(driver)
    dd.selectvalue()
    print()
