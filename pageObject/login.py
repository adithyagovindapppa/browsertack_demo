import time

from selenium.webdriver.common.by import By

from testcases.demo import result
from selenium.webdriver.support import  expected_conditions as EC


class WebDriverWait:
    pass


class Login():
    textbox_selection = "com.questalliance.myquest:id/tv_choose_language"
    textbox_username = "com.questalliance.myquest:id/tiet_email_mobile"
    textbox_password = "com.questalliance.myquest:id/tiet_password"
    button_login = "com.questalliance.myquest:id/tv_login"
    batches = "//android.widget.FrameLayout[@content-desc='Batches']/android.view.ViewGroup/android.widget.TextView"
    addnew_batch = "com.questalliance.myquest:id/tv_add_new_batch"
    startdate = "com.questalliance.myquest:id/et_start_date_day"
    startdate_box = "//android.view.View[@content-desc='14 September 2023']"
    okbutton = "android:id/button1"
    enddate = "com.questalliance.myquest:id/et_end_date_day"
    enddate_box = "//android.view.View[@content-desc='29 September 2023']"
    okbutton1 = "android:id/button1"
    addbatch_button = "com.questalliance.myquest:id/tv_add_batch"
    view = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TextView[10]"
    add_learners = "com.questalliance.myquest:id/tv_add_new_learners"
    search = "com.questalliance.myquest:id/et_search"
    search_box = "com.questalliance.myquest:id/et_search"
    check_box = "com.questalliance.myquest:id/fl_root"
    addlearners = "com.questalliance.myquest:id/tv_add_learners"
    delete_batch = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TextView[8]"
    delete_button = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TextView[3]"
    exit = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ImageView[1]"
    page_source = "com.questalliance.myquest:id/dummy_view"
    menubox = "com.questalliance.myquest:id/navDrawerIV"
    log_out = "com.questalliance.myquest:id/tv_logout"
    yes_logout = "com.questalliance.myquest:id/yesBtn"


    go_live = "//android.widget.FrameLayout[@content-desc='Go Live']/android.view.ViewGroup/android.widget.TextView"
    create_meeting = "com.questalliance.myquest:id/iv_create_meeting"
    meeting_name = "com.questalliance.myquest:id/et_meeting_name"
    enter_name = "com.questalliance.myquest:id/et_meeting_name"
    startmeeting_date = "com.questalliance.myquest:id/tv_start_date"
    enter_startdate = "//android.view.View[@content-desc='28 September 2023']"
    enter_ok = "android:id/button1"
    startmeeting_time = "com.questalliance.myquest:id/tv_start_time"
    enter_starttime = "//android.widget.RadialTimePickerView.RadialPickerTouchHelper[@content-desc='1']"
    enter_ok1 = "android:id/button1"
    endmeeting_date = "com.questalliance.myquest:id/tv_end_date"
    enter_enddate = "//android.view.View[@content-desc='30 September 2023']"
    enter_ok2 = "android:id/button1"
    endmeeting_time = "com.questalliance.myquest:id/tv_end_time"
    enter_endtime = "//android.widget.RadialTimePickerView.RadialPickerTouchHelper[@content-desc='4']"
    enter_ok3 = "android:id/button1"
    participants = "com.questalliance.myquest:id/iv_category_icon"
    participants_click = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.TextView[3]"
    guests = "com.questalliance.myquest:id/add_guest_label"
    guests_search = "com.questalliance.myquest:id/et_meeting_name"
    guests_entername = "com.questalliance.myquest:id/et_meeting_name"
    click_guestsname = "com.questalliance.myquest:id/iv_rb"
    click_add = "com.questalliance.myquest:id/tv_add_mem"
    click_done = "com.questalliance.myquest:id/tv_save_btn"
    description = "com.questalliance.myquest:id/et_description"
    description_enter = "com.questalliance.myquest:id/et_description"
    click_save = "com.questalliance.myquest:id/tv_save_btn"

    go_liveclick = "//android.widget.FrameLayout[@content-desc='Go Live']/android.view.ViewGroup/android.widget.TextView"
    upcoming_ses = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.TextView[1]"
    join_meeting = "com.questalliance.myquest:id/btn_vc_join"








    def __init__(self, value):
        # super().__init__(value)
        self.driver = value
        self.default_explicit_wait = 30

    def open_applicaton(self):
        # time.sleep(30)
        self.driver.find_element(By.ID, self.textbox_selection).click()
        # time.sleep(2)
        self.driver.find_element(By.ID, self.textbox_username).send_keys(result[0])
        # time.sleep(2)
        self.driver.find_element(By.ID, self.textbox_password).send_keys(result[1])
        # time.sleep(5)
        self.driver.hide_keyboard()
        # time.sleep(3)
        self.driver.find_element(By.ID, self.button_login).click()
        # time.sleep(5)


    def learner_application(self):
        self.driver.find_element(By.ID, self.textbox_selection).click()
        # time.sleep(6)
        self.driver.find_element(By.ID, self.textbox_username).send_keys(result[2])
        # time.sleep(6)
        self.driver.find_element(By.ID, self.textbox_password).send_keys(result[3])
        # time.sleep(6)
        self.driver.hide_keyboard()
        # time.sleep(6)
        self.driver.find_element(By.ID, self.button_login).click()

    def click_batch(self):
        self.driver.find_element(By.XPATH, self.batches).click()
        # WebDriverWait(self.driver,self.default_explicit_wait).unitl(EC.presence_of_element_located(self.batches)).click()

    # def delete_batch_1(self):
    #     self.driver.find_element(By.XPATH, self.delete_batch).click()
    #     # time.sleep(5)
    #     self.driver.find_element(By.XPATH, self.delete_button).click()
    #     # time.sleep(5)
    #     self.driver.find_element(By.XPATH, self.exit).click()


    def click_add_new_batch(self):
        self.driver.find_element(By.ID, self.addnew_batch).click()

    def select_dates(self):
        self.driver.find_element(By.ID, self.startdate).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.startdate_box).click()
        time.sleep(5)
        self.driver.find_element(By.ID, self.okbutton).click()
        time.sleep(5)
        self.driver.find_element(By.ID, self.enddate).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.enddate_box).click()
        time.sleep(5)
        self.driver.find_element(By.ID, self.okbutton1).click()

    def click_add_batch_button(self):
        self.driver.find_element(By.ID, self.addbatch_button).click()

    def click_view_button(self):
        self.driver.find_element(By.XPATH, self.view).click()

    def add_learner(self):
        self.driver.find_element(By.ID, self.add_learners).click()

    def search_learner(self):
        self.driver.find_element(By.ID, self.search).click()
        time.sleep(5)
        self.driver.find_element(By.ID, self.search_box).send_keys("Tibil")
        time.sleep(5)
        self.driver.find_element(By.ID, self.check_box).click()
        time.sleep(8)
        self.driver.find_element(By.ID, self.addlearners).click()
        time.sleep(9)

    def logout_app(self):
        self.driver.find_element(By.ID, self.menubox).click()
        # time.sleep(8)
        self.driver.find_element(By.ID, self.log_out).click()
        # time.sleep(10)
        self.driver.find_element(By.ID, self.yes_logout).click()

 # ------------------------------------------------------------------------
    def click_golive(self):
        self.driver.find_element(By.XPATH, self.go_live).click()

    def click_createmeeting(self):
        self.driver.find_element(By.ID,self.create_meeting).click()
        # time.sleep(5)
        self.driver.find_element(By.ID,self.meeting_name).click()
        # time.sleep(5)
        self.driver.find_element(By.ID,self.enter_name).send_keys("tibil meeting")
        # time.sleep(5)
        self.driver.find_element(By.ID,self.startmeeting_date).click()
        # time.sleep(10)
        self.driver.find_element(By.XPATH,self.enter_startdate).click()
        # time.sleep(15)
        self.driver.find_element(By.ID,self.enter_ok).click()
        # time.sleep(10)
        self.driver.find_element(By.ID,self.startmeeting_time).click()
        # time.sleep(10)
        self.driver.find_element(By.XPATH,self.enter_starttime).click()
        # time.sleep(10)
        self.driver.find_element(By.ID,self.enter_ok1).click()
        # time.sleep(10)
        self.driver.find_element(By.ID,self.endmeeting_date).click()
        # time.sleep(10)
        self.driver.find_element(By.XPATH,self.enter_enddate).click()
        # time.sleep(10)
        self.driver.find_element(By.ID, self.enter_ok2).click()
        # time.sleep(10)
        self.driver.find_element(By.ID, self.endmeeting_time).click()
        # time.sleep(10)
        self.driver.find_element(By.XPATH, self.enter_endtime).click()
        # time.sleep(10)
        self.driver.find_element(By.ID, self.enter_ok3).click()
        time.sleep(5)

    def click_participants(self):
        self.driver.find_element(By.ID,self.participants).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,self.participants_click).click()
        time.sleep(5)
        self.driver.find_element(By.ID,self.guests).click()
        time.sleep(5)
        self.driver.find_element(By.ID,self.guests_search).click()
        time.sleep(5)
        self.driver.find_element(By.ID,self.guests_entername).send_keys("Tibil")
        time.sleep(5)
        self.driver.find_element(By.ID,self.click_guestsname).click()
        time.sleep(5)
        self.driver.find_element(By.ID,self.click_add).click()
        time.sleep(9)
        self.driver.find_element(By.ID,self.click_done).click()
        time.sleep(9)
        self.driver.find_element(By.ID,self.description).click()
        time.sleep(5)
        self.driver.find_element(By.ID,self.description_enter).send_keys("tibil")
        # time.sleep(5)
        self.driver.hide_keyboard()
        time.sleep(5)
        self.driver.find_element(By.ID,self.click_save).click()
        time.sleep(5)

    def logout_app1(self):
            self.driver.find_element(By.ID, self.menubox).click()
            time.sleep(5)
            self.driver.find_element(By.ID, self.log_out).click()
            time.sleep(5)
            self.driver.find_element(By.ID, self.yes_logout).click()

        # ------------------------------------------------------------------------
    def click_live(self):
        self.driver.find_element(By.XPATH, self.go_liveclick).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.upcoming_ses).click()
        time.sleep(5)
        self.driver.find_element(By.ID, self.join_meeting).click()





