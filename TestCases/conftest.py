import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.opera import OperaDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pyautogui


# @pytest.fixture()
def setUp(browserName):
    global driver
    if browserName == 'Chrome':
        # Use pip install webdriver-manager to resolve chrome driver version support issue
        # driver = webdriver.Chrome(ChromeDriverManager().install())
        # https: https://pypi.org/project/webdriver-manager/
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        print("Launching Chrome Browser !!")
    elif browserName == 'Firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        print("Launching FireFox Browser !!")
    elif browserName == 'IE':
        driver = webdriver.Ie(executable_path=IEDriverManager().install())
        print("Launching IE Browser !!")
    elif browserName == "Edge":
        driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())
        print("Launching Edge Browser !!")
    elif browserName == "Opera":
        driver = webdriver.Opera(executable_path=OperaDriverManager().install())
        print("Launching Opera Browser !!")
    else:
        print("please enter the correct browser:" + browserName)
        raise Exception(f'"{browserName["browser"]}" is not a supported browser')
        # raise Exception("Browser Driver not found")
    driver.maximize_window()
    return driver


# THIS WILL GET THE VALUE FROM CLI AS A HOOK. WE NEED NOT ABOUT USING THIS FUNCTION. IT WILL AUTOMATICALLY GET EXECUTED
def pytest_addoption(parser):
    parser.addoption("--browser")


# THIS FIXTURE WILL RETURN THE BROWSER VALUE TO SETUP METHOD
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def auth():
    """
    To Take authentication info from the user
    """
    auth = []
    print("Enter the username:")
    username = pyautogui.prompt('Enter the username')
    auth.append(username)
    print("Enter the password")
    password = pyautogui.password('Enter the password')
    auth.append(password)
    print("Enter the project key:")
    auth.append(input())
    return auth


# PYTEST HTML REPORT
#
# # A HOOK TO ADD THE ENVIRONMENT INFORMATION TO THE HTML REPORT
# def pytest_configure(config):
#     config._metadata['Browser Name'] = 'Google Chrome'
#     config._metadata['Project Name'] = 'Web Automation Framework'
#     config._metadata['Module Name'] = 'Web Application'
#     config._metadata['Tester'] = 'Lakshmi Narayana'


# # A HOOK TO DELETE/MODIFY THE ENVIRONMENT INFORMATION FROM THE HTML REPORT
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)
