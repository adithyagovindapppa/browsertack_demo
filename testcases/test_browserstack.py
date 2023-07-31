#
# import logging
# import time
#
#
# from selenium.webdriver.common.by import By
#
# from pageObject.login import Login
# from appium import webdriver
#
#
#
# from utilities import CustomLogger
# from utilities.readproperties import ReadConfig
#
#
# class TestLogin:
#     loginpage = None
#     logger = CustomLogger.setup_logger('Login', ReadConfig.get_logs_directory() + "/test_login.log",
#                                        level=logging.DEBUG)
#
#
#
#     def test_login_page_titles(self):
#         self.logger.info("***********************Open application*****************************")
#         self.logger.info("********************test_login_page started*********************")
#         username = 'adithyag_4QD0iV'
#         key = '1hYZKXrzURRGK6a7xxdw'
#         desired_cap = {
#             "app": "bs://13f854c9bf9e7e9f95bb7410b57f3498127cec23",
#             "browserName": "Chrome",
#             "deviceName": "Google Pixel 6 Pro",
#             "os_version": "13.0",
#             "realMobile": "true",
#             "autoGrantPermissions": "true",
#             "autoAcceptAlerts": "true",
#             "platformName": "Android",
#             "debug": " true",
#         }
#
#         print(username, key)
#         url = f'https://' + username + ':' + key +'@hub-cloud.browserstack.com/wd/hub'
#         print(url)
#         self.driver = webdriver.Remote(url, desired_cap)
#
#         # time.sleep(20)
#         self.login = Login(self.driver)
#         self.login.open_applicaton()
#         time.sleep(6)
#
#         dashboard_display = self.driver.find_element(By.ID, "com.questalliance.myquest:id/tv_welcome")
#         if dashboard_display.is_displayed():
#             assert True
#             self.logger.info("******************** Dashborad verify ************************")
#         else:
#             # self.driver.save_screenshot("/home/adithya/PycharmProjects/mobiletest/screenshots" + "login.png")
#             print("login failed")
#             self.logger.info("******************** Dashborad ended ************************")
#             assert False
#         self.driver.quit()

import logging
import time

from selenium.webdriver.common.by import By

from pageObject.login import Login
from appium import webdriver
from utilities import CustomLogger
from utilities.readproperties import ReadConfig


class TestLogin:
    # loginpage = None
    logger = CustomLogger.setup_logger('Login', ReadConfig.get_logs_directory() + "/test_login.log",
                                       level=logging.DEBUG)

    def test_login_page_titles(self):
        self.logger.info("***********************Test_001_Login*****************************")
        self.logger.info("********************test_login_page_tittle started*********************")
        desired_cap = {
            "app": "bs://13f854c9bf9e7e9f95bb7410b57f3498127cec23",
            "browserName": "Chrome",
            "deviceName": "Google Pixel 6 Pro",
            "os_version": "13.0",
            "realMobile": "true",
            "autoGrantPermissions": "true",
            "autoAcceptAlerts": "true",
            "platformName": "Android",
            "debug": " true",}
        self.driver = webdriver.Remote("https://adithyag_4QD0iV:1hYZKXrzURRGK6a7xxdw@hub-cloud.browserstack.com/wd/hub", desired_cap)
        # time.sleep(20)
        self.login = Login(self.driver)
        self.login.open_applicaton()
        time.sleep(10)

        dashboard_display = self.driver.find_element(By.ID, "com.questalliance.myquest:id/tv_welcome")
        if dashboard_display.is_displayed():
            assert True
            self.logger.info("******************** test_login_page_tittle test case passed ************************")
        else:
            self.driver.save_screenshot("/home/adithya/PycharmProjects/mobiletest/screenshots" + "login.png")
            print("login failed")
            self.logger.info("******************** test_login_page_tittle ended ************************")
            assert False

