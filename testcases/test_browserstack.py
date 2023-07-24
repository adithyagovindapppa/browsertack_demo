
import logging
import time
# import pytest

from selenium.webdriver.common.by import By

from pageObject.login import Login
from appium import webdriver

from utilities import CustomLogger
from utilities.readproperties import ReadConfig


# from utilities import CustomLogger
# from utilities.readproperties import ReadConfig


class TestLogin:
    loginpage = None
    logger = CustomLogger.setup_logger('Login', ReadConfig.get_logs_directory() + "/test_login.log",
                                       level=logging.DEBUG)

    # logger = CustomLogger.setup_logger('Login', ReadConfig.get_logs_directory() + "/test_login.log",
    #                                    level=logging.DEBUG)

    # def __init__(self):
    #     self.logger = None

    def test_login_page_titles(self):
        self.logger.info("***********************Open application*****************************")
        self.logger.info("********************test_login_page started*********************")
        desired_cap = {
            "app": "bs://2bbc809d2f8fff41431867cb11a3aa74c82e749c",
            "browserName": "Chrome",
            "deviceName": "Google Pixel 6 Pro",
            "os_version": "13.0",
            "realMobile": "true",
            "autoGrantPermissions": "true",
            "autoAcceptAlerts": "true",
            # "devicename": "2B101JEGR10785",
            "platformName": "Android",
            "debug": " true",

            # ... other capabilities ...
            # ... other capabilities ...


        # "app": "/home/adithya/Downloads/quest.apk"
        }
        self.driver = webdriver.Remote("https://adithyag_SjW8cV:fEUxHF8ywXMFYyA6gMz6@hub-cloud.browserstack.com/wd/hub",
                                       desired_cap)

        # time.sleep(20)
        self.login = Login(self.driver)
        self.login.open_applicaton()
        time.sleep(6)

        dashboard_display = self.driver.find_element(By.ID, "com.questalliance.myquest:id/tv_welcome")
        if dashboard_display.is_displayed():
            assert True
            self.logger.info("******************** Dashborad verify ************************")
        else:
            # self.driver.save_screenshot("/home/adithya/PycharmProjects/mobiletest/screenshots" + "login.png")
            print("login failed")
            self.logger.info("******************** Dashborad ended ************************")
            assert False
        self.driver.quit()

