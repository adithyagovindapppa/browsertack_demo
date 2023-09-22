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
    def test_golive(self, setup):
        self.driver = setup
        self.driver.implicitly_wait(50)
        self.login = Login(self.driver)
        self.login.open_applicaton()
        # time.sleep(15)
        self.login.click_golive()
        # time.sleep(15)
        self.login.click_createmeeting()
        # time.sleep(10)
        self.login.click_participants()
        # time.sleep(5)
        if "tibil testing" in self.driver.page_source:
            assert True
        # else:
            assert False
    #
    def test_livemeeting(self, setup):
        self.driver = setup
        self.driver.implicitly_wait(50)
        self.login = Login(self.driver)
        self.login.learner_application()
        time.sleep(10)
        self.login.click_live()




