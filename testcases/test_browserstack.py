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

    def test_login_page_titles(self, setup):
        self.logger.info("***********************Open application*****************************")
        self.logger.info("********************test_login_page started*********************")
        self.driver = setup
        self.driver.implicitly_wait(50)
        # self.cal = Login(self.driver)
        self.login = Login(self.driver)
        self.login.open_applicaton()
        # time.sleep(20)
        self.login.click_batch()
        # time.sleep(10)
        # self.login.delete_batch_1()
        # time.sleep(5)
        self.login.click_add_new_batch()
        # time.sleep(5)
        self.login.select_dates()
        # time.sleep(5)
        self.login.click_add_batch_button()
        # time.sleep(5)
        self.login.click_view_button()
        # time.sleep(5)
        self.login.add_learner()
        # time.sleep(10)
        self.login.search_learner()
        # time.sleep(10)
        self.login.logout_app()
        time.sleep(5)
        # if "Learner" in self.driver.page_source:
        #     assert True
        # else:
        #     assert False

    def test_golive(self, setup):
        self.driver = setup
        self.driver.implicitly_wait(50)
        self.login = Login(self.driver)
        self.login.open_applicaton()
        time.sleep(5)
        # time.sleep(15)
        self.login.click_golive()
        time.sleep(5)
        self.login.click_createmeeting()
        # time.sleep(10)
        self.login.click_participants()
        # time.sleep(5)
        self.login.logout_app1()
        if "tibil testing" in self.driver.page_source:
            assert True
        # else:
            assert False
    # #
    def test_livemeeting(self, setup):
        self.driver = setup
        self.driver.implicitly_wait(50)
        self.login = Login(self.driver)
        self.login.learner_application()
        time.sleep(10)
        self.login.click_live()



# jj
