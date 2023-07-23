import time
# from lib2to3.pgen2 import driver

# import self as self
# from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait

# from utilities.readproperties import ReadConfig


class WebDriverWait:
    pass


class Login:
    textbox_selection = "com.questalliance.myquest:id/tv_choose_language"
    textbox_username = "com.questalliance.myquest:id/tiet_email_mobile"
    textbox_box = "com.questalliance.myquest:id/tiet_password"
    textbox_password = "com.questalliance.myquest:id/tiet_password"
    button_login = "com.questalliance.myquest:id/tv_login"

    def __init__(self, value):
        # super().__init__(value)
        self.driver = value

    def open_applicaton(self):
        # time.sleep(30)
        self.driver.find_element(By.ID, self.textbox_selection).click()
        time.sleep(6)
        # self.driver.find_element(By.ID, self.textbox_username).send_keys(ReadConfig.getUserID())
        # print(ReadConfig.getUserID())
        self.driver.find_element(By.ID, self.textbox_username).send_keys("kiransv8123@gmail.com")
        self.driver.find_element(By.ID, self.textbox_box).click()
        time.sleep(6)
        # self.driver.find_element(By.ID, self.textbox_password).send_keys(ReadConfig.getPassword())
        # print(ReadConfig.getPassword())
        self.driver.find_element(By.ID, self.textbox_password).send_keys("Kiran@123")
        time.sleep(6)
        # # self.driver.
        # self.driver.execute_script('mobile: shell', {'command': 'input keyevent 111'})
        self.driver.hide_keyboard()
        time.sleep(6)
        self.driver.find_element(By.ID, self.button_login).click()



