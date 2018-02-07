# -*- coding:utf-8 -*-


from appium.webdriver.common.mobileby import MobileBy
# from selenium.webdriver.support.ui import WebDriverWait
# from appium.webdriver.common.touch_action import TouchAction
# from basepage import BasePage
from homepage import HomePage
from loginpage import Login
import time


class MyMenuInfo(HomePage):
    u"""我的菜单"""

    menus_loc = (MobileBy.ID, "tabs")
    # ********************* 个人信息 **********************************
    my_personal_info_loc    = (MobileBy.ID, "rel_person_information")
    my_colletion_loc        = (MobileBy.ID, "rel_my_collection")
    my_personal_subject_loc = (MobileBy.ID, "rel_personal_subject")
    my_personal_setting_loc = (MobileBy.ID, "rel_personal_setting")
    my_personal_about_loc   = (MobileBy.ID, "rel_personal_about")
    back_loc                = (MobileBy.ID, "common_top_left_layout")
    
    def back(self):
        self.find_element(*self.back_loc).click()

    def click_my_menu(self, username="KC1237", password="csu123"):
        login = Login(self.driver)
        login.handle_splash_screen()
        login.user_login(username, password)
        # time.sleep(15)
        self.wait_element(20, 1, *self.menus_loc)
        login.my_click()
        # time.sleep(5)

    def my_personal_info(self):
        self.wait_element(*self.my_personal_info_loc).click()

    # 类型 部门 性别
    personal_type_loc           = (MobileBy.ID, "edit_personal_mytype")
    personal_my_department_loc  = (MobileBy.ID, "edit_personal_mydepartment")
    personal_sex_loc            = (MobileBy.ID, "edit_personal_sex")

    # 手机号码
    edit_personal_my_number_loc = (MobileBy.ID, "edit_personal_mynumber")
    set_personal_my_number_loc  = (MobileBy.ID, "personal_et_number")
    set_number_friend_see_loc   = (MobileBy.ID, "personal_checkbox_phfriend")
    set_number_group_see_loc    = (MobileBy.ID, "personal_checkbox_phgroup")
    
    # 邮箱
    edit_personal_email_loc     = (MobileBy.ID, "edit_personal_myemail")
    set_email_loc               = (MobileBy.ID, "personal_et_mail")
    set_email_friend_see_loc    = (MobileBy.ID, "personal_checkbox_friend")
    set_email_group_see_loc     = (MobileBy.ID, "personal_checkbox_group")
    
    # 个人标签
    edit_personal_label_loc    = (MobileBy.ID, "tv_personalinformation_label")
    set_personal_label_1_loc   = (MobileBy.XPATH, "//android.widget.ListView/android.widget.LinearLayout[1]/android.widget.ImageView[1]")
    set_personal_label_2_loc   = (MobileBy.XPATH, "//android.widget.ListView/android.widget.LinearLayout[2]/android.widget.ImageView[1]")
    set_personal_label_3_loc   = (MobileBy.XPATH, "//android.widget.ListView/android.widget.LinearLayout[3]/android.widget.ImageView[1]")
    personal_lable_name_1_loc  = (MobileBy.XPATH, "//android.widget.ListView/android.widget.LinearLayout[1]/android.widget.TextView[1]")
    personal_lable_name_2_loc  = (MobileBy.XPATH, "//android.widget.ListView/android.widget.LinearLayout[2]/android.widget.TextView[1]")
    personal_lable_name_3_loc  = (MobileBy.XPATH, "//android.widget.ListView/android.widget.LinearLayout[3]/android.widget.TextView[1]")
    personal_label_confirm_loc = (MobileBy.ID, "tv_common_right_function_btn")

    def get_personal_type(self):
        return self.find_element(*self.personal_type_loc).text

    def get_personal_my_department(self):
        return self.find_element(*self.personal_my_department_loc).text

    def get_personal_sex(self):
        return self.find_element(*self.personal_sex_loc).text

    def set_number_email(self, mynumber, myemail):

        number_email_is_see = []

        number_is_see = self.set_personal_my_number(mynumber)
        number_email_is_see.append(number_is_see)
        self.back()
        self.find_element(*self.my_personal_info_loc).click()
        time.sleep(1)
        email_is_see = self.set_personal_email(myemail)
        number_email_is_see.append(email_is_see)

        self.back()

        # 重新进入个人信息页面才会保存
        self.find_element(*self.my_personal_info_loc).click()

        return number_email_is_see

    def set_personal_my_number(self, mynumber):
        number_is_see = []
        self.find_element(*self.edit_personal_my_number_loc).click()
        time.sleep(1)
        self.find_element(*self.set_personal_my_number_loc).clear()
        self.find_element(*self.set_personal_my_number_loc).send_keys(mynumber)
        self.driver.hide_keyboard()
        time.sleep(1)
        self.find_element(*self.set_number_friend_see_loc).click()
        self.find_element(*self.set_number_group_see_loc).click()
        time.sleep(1)
        checked = self.find_element(*self.set_number_friend_see_loc).get_attribute("checked")
        if checked == "true":
            number_is_see.append(u"号码好友可见")
        else:
            number_is_see.append(u"号码好友不可见")
        checked = self.find_element(*self.set_number_group_see_loc).get_attribute("checked")
        if checked == "true":
            number_is_see.append(u"号码群组可见")
        else:
            number_is_see.append(u"号码群组不可见")

        time.sleep(1)
        self.back()
        return number_is_see
        # self.driver.hide_keyboard()
        # self.back()
        # time.sleep(1)
        # self.find_element(*self.my_personal_info_loc).click()

    def get_personal_my_number(self):
        number = []
        number_is_see = []
        text = self.find_element(*self.edit_personal_my_number_loc).text
        number.append(text)
        self.find_element(*self.edit_personal_my_number_loc).click()
        time.sleep(1)
        checked = self.find_element(*self.set_number_friend_see_loc).get_attribute("checked")
        if checked == "true":
            number_is_see.append(u"号码好友可见")
        else:
            number_is_see.append(u"号码好友不可见")
        checked = self.find_element(*self.set_number_group_see_loc).get_attribute("checked")
        if checked == "true":
            number_is_see.append(u"号码群组可见")
        else:
            number_is_see.append(u"号码群组不可见")

        number.append(number_is_see)
        self.back()
        return number

    def get_personal_email(self):
        email = []
        # 隐藏键盘
        # self.driver.hide_keyboard()
        self.find_element(*self.edit_personal_email_loc).click()
        time.sleep(1)
        text = self.find_element(*self.set_email_loc).text
        email.append(text)
        checked = self.find_element(*self.set_email_friend_see_loc).\
            get_attribute("checked")
        if checked == "true":
            email.append(u"邮箱好友可见")
        else:
            email.append(u"邮箱好友不可见")
        checked = self.find_element(*self.set_email_group_see_loc).\
            get_attribute("checked")
        if checked == "true":
            email.append(u"邮箱群组可见")
        else:
            email.append(u"邮箱群组不可见")
        self.back()
        return email

    def set_personal_email(self, email):
        email_is_see = []
        try:
            self.wait_element(*self.edit_personal_email_loc)
        finally:
            self.find_element(*self.edit_personal_email_loc).click()
            time.sleep(1)
            self.find_element(*self.set_email_loc).clear()
            self.find_element(*self.set_email_loc).send_keys(email)
            self.driver.hide_keyboard()
            time.sleep(1)
            self.find_element(*self.set_email_friend_see_loc).click()
            self.find_element(*self.set_email_group_see_loc).click()
            # self.driver.hide_keyboard()
            # self.back()
            # self.find_element(self.my_personal_info_loc).click()
        checked = self.find_element(*self.set_email_friend_see_loc).\
            get_attribute("checked")
        if checked == "true":
            email_is_see.append(u"邮箱好友可见")
        else:
            email_is_see.append(u"邮箱好友不可见")
        checked = self.find_element(*self.set_email_group_see_loc).\
            get_attribute("checked")
        if checked == "true":
            email_is_see.append(u"邮箱群组可见")
        else:
            email_is_see.append(u"邮箱群组不可见")
        self.back()
        return email_is_see

    def get_personal_label(self):
        self.find_element(*self.edit_personal_label_loc).click()
        label = []
        # for tag in self.set_personal_label():
        #     if tag == 1:
        #         label.append(self.find_element(*self.personal_lable_name_1_loc).text)
        #     else:
        #         label.append(None)
        try:
            self.find_element(*self.set_personal_label_1_loc)
            text = self.find_element(*self.personal_lable_name_1_loc).text
            label.append(text)
        except:
            label.append(None)

        try:
            self.find_element(*self.set_personal_label_2_loc)
            text = self.find_element(*self.personal_lable_name_2_loc).text
            label.append(text)
        except:
            label.append(None)
        try:
            self.find_element(*self.set_personal_label_3_loc)
            text = self.find_element(*self.personal_lable_name_3_loc).text
            label.append(text)
        except:
            label.append(None)
        self.back()
        return label

    def set_personal_label(self):
        self.find_element(*self.edit_personal_label_loc).click()
        tag = []
        try:
            self.find_element(*self.set_personal_label_1_loc)
        except:
            self.find_element(*self.personal_lable_name_1_loc).click()
            tag.append(u"党员")
        else:
            self.find_element(*self.set_personal_label_1_loc).click()
            tag.append(None)

        time.sleep(1)
        try:
            self.find_element(*self.set_personal_label_2_loc)
        except:
            self.find_element(*self.personal_lable_name_2_loc).click()
            tag.append(u"羽毛球")
        else:
            self.find_element(*self.set_personal_label_2_loc).click()
            tag.append(None)

        time.sleep(1)
        try:
            self.find_element(*self.set_personal_label_3_loc)
        except:
            self.find_element(*self.personal_lable_name_3_loc).click()
            tag.append(u"乒乓球")
        else:
            self.find_element(*self.set_personal_label_3_loc).click()
            tag.append(None)
        self.find_element(*self.personal_label_confirm_loc).click()
        return tag

    def my_collection(self):
        return self.find_element(*self.my_collection_loc).click()

    def my_personal_subject(self):
        self.find_element(*self.my_personal_subject_loc).click()

    def my_personal_setting(self):
        self.find_element(*self.my_personal_setting_loc).click()

    def my_person_about(self):
        self.find_element(*self.my_person_about_loc).click()

    # ********************我的日程*************************
    # 创建日程
    my_schedule_loc  = (MobileBy.ID, "rel_my_schedule")
    add_schedule_loc = (MobileBy.ID, "iv_add")
    edit_content_loc = (MobileBy.ID, "edit_content")
    is_whole_day_loc = (MobileBy.ID, "is_whole_day")
    start_time_loc   = (MobileBy.ID, "starttime")

    year_loc    = (MobileBy.XPATH, "//android.widget.DatePicker/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.NumberPicker[1]/android.widget.EditText")
    month_loc   = (MobileBy.XPATH, "//android.widget.DatePicker/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.NumberPicker[2]/android.widget.EditText")
    day_loc     = (MobileBy.XPATH, "//android.widget.DatePicker/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.NumberPicker[3]/android.widget.EditText")
    hour_loc    = (MobileBy.XPATH, "//android.widget.TimePicker/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.NumberPicker[1]/android.widget.EditText")
    minutes_loc = (MobileBy.XPATH, "//android.widget.TimePicker/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.NumberPicker[2]/android.widget.EditText")

    end_time_loc            = (MobileBy.ID, "endtime")
    confirm_select_time_loc = (MobileBy.ID, "schedule_confirm")
    remind_loc              = (MobileBy.ID, "remind")
    edit_remind_loc         = (MobileBy.ID, "tv_remind")
    no_remind_loc           = (MobileBy.ID, "no_remind")
    before_0m_remind_loc    = (MobileBy.ID, "before_begin_action")
    before_5m_remind_loc    = (MobileBy.ID, "before_begin_fiveminuteaction")
    before_10m_remind_loc   = (MobileBy.ID, "before_begin_tenminuteaction")
    before_15m_remind_loc   = (MobileBy.ID, "before_begin_fifminuteaction")
    before_30m_remind_loc   = (MobileBy.ID, "before_begin_thirtyminuteaction")
    before_1d_remind_loc    = (MobileBy.ID, "before_begin_onehouraction")
    before_2d_remind_loc    = (MobileBy.ID, "before_begin_twodayaction")
    before_7d_remind_loc    = (MobileBy.ID, "before_begin_oneweekaction")
    
    
    add_friend_loc       = (MobileBy.ID, "iv_bottom_headimg")
    my_friend_loc        = (MobileBy.XPATH, "//android.widget.ExpandableListView/android.widget.LinearLayout[4]")
    add_my_friend_1_loc  = (MobileBy.XPATH, "//android.widget.ExpandableListView/android.widget.LinearLayout[5]")
    add_menber_loc       = (MobileBy.ID, "tv_add_member")

    schedule_confirm_loc = (MobileBy.ID, "tv_common_right_function_btn")

    def my_schedule(self):
        self.wait_element(5, 0.5, *self.my_schedule_loc).click()
        # self.find_element(*self.my_schedule_loc).click()

    def add_schedule(self):
        self.wait_element(5, 0.5, *self.add_schedule_loc).click()
        # self.find_element(*self.add_schedule_loc).click()

    def edit_content(self, content):
        self.wait_element(5, 0.5, *self.edit_content_loc).clear()
        # self.find_element(*self.edit_content_loc).clear()
        self.find_element(*self.edit_content_loc).send_keys(content)

    def is_whole_day(self):
        self.find_element(*self.is_whole_day_loc).click()

    # def start_end_time(self,future_time,tag=1):
    #     # tag == 1 开始时间
    #     if tag == 1:
    #         self.find_element(*self.start_time_loc).click()
    #     if tag == 2:
    #         self.find_element(*self.end_time_loc).click()
    #     self.find_element(*self.year_loc).click()
    #     self.find_element(*self.year_loc).send_keys(future_time[0:4])
    #     self.find_element(*self.month_loc).click()
    #     self.find_element(*self.month_loc).send_keys(future_time[4:6])
    #     self.find_element(*self.day_loc).clear()
    #     self.find_element(*self.day_loc).send_keys(future_time[6:8])
    #     self.find_element(*self.hour_loc).click()
    #     self.find_element(*self.hour_loc).send_keys(future_time[8:10])
    #     print future_time[8:10]
    #     #self.find_element(*self.minutes_loc).click()
    #     self.find_element(*self.minutes_loc).send_keys(future_time[10:12])
    #     print future_time[10:12]
    #     self.driver.hide_keyboard()

    def get_element_top_letf_point(self, *loc):
        x = self.find_element(*loc).location.get('x')
        y = self.find_element(*loc).location.get('y')
        return x, y

    def get_element_size(self, *loc):
        return self.find_element(*self.year_loc).size

    def select_start_end_time(self, flag, t, num):
        # flag 开始时间结束时间; t 年 月 日 时 分; num 滑动次数
        if flag == "start":
            self.wait_element(5, 0.5, *self.start_time_loc).click()
            # self.find_element(*self.start_time_loc).click()
        else:
            self.wait_element(5, 0.5, *self.end_time_loc).click()
            # self.find_element(*self.end_time_loc).click()
        time.sleep(1)
        if t == "year":
            # 获取元素左上角的坐标
            element_point = self.get_element_top_letf_point(*self.year_loc)
            # 获取元素大小(宽和高)
            element_size = self.get_element_size(*self.year_loc)
        elif t == "month":
            element_point = self.get_element_top_letf_point(*self.month_loc)
            element_size = self.get_element_size(*self.month_loc)
        elif t == "day":
            element_point = self.get_element_top_letf_point(*self.day_loc)
            element_size = self.get_element_size(*self.day_loc)
        elif t == "hour":
            element_point = self.get_element_top_letf_point(*self.hour_loc)
            element_size = self.get_element_size(*self.hour_loc)
        else:
            # self.find_element(*self.minutes_loc).click()
            # 获取元素左上角的坐标
            element_point = self.get_element_top_letf_point(*self.minutes_loc)
            # 获取元素大小(宽和高)
            element_size = self.get_element_size(*self.minutes_loc)
            # width = self.find_element(*self.year_loc).size["width"]
            # height = self.find_element(*self.year_loc).size["height"]
            # print width, height
        # 元素中心点坐标
        x = element_point[0] + element_size["width"]/2
        y = element_point[1] + element_size["height"]/2
        # 向上滑动
        if flag == "start":
            for i in range(0, num):
                super(MyMenuInfo, self).swipe_up((x, y), 1000, 1, 1, 0.2)
        else:
            for i in range(0, num):
                super(MyMenuInfo, self).swipe_up((x, y), 1000, 1, 1, 0.2)

    def confirm_select_time(self):
        self.find_element(*self.confirm_select_time_loc).click()

    def get_start_end_time(self):
        year    = self.find_element(*self.year_loc).text
        month   = self.find_element(*self.month_loc).text
        day     = self.find_element(*self.day_loc).text
        hours   = self.find_element(*self.hour_loc).text
        minutes = self.find_element(*self.minutes_loc).text
        self.confirm_select_time()
        return int(year), int(month), int(day), int(hours), int(minutes)

        # self.find_element(*self.year_loc).send_keys(future_time[0:4])
        # self.find_element(*self.month_loc).click()
        # self.find_element(*self.month_loc).send_keys(future_time[4:6])
        # self.find_element(*self.day_loc).clear()
        # self.find_element(*self.day_loc).send_keys(future_time[6:8])
        # self.find_element(*self.hour_loc).click()
        # self.find_element(*self.hour_loc).send_keys(future_time[8:10])
        # print future_time[8:10]
        # #self.find_element(*self.minutes_loc).click()
        # self.find_element(*self.minutes_loc).send_keys(future_time[10:12])
        # print future_time[10:12]
        # self.driver.hide_keyboard()

    def remind(self, value="-1"):
        self.find_element(*self.remind_loc).click()
        if value == "-1":
            self.find_element(*self.no_remind_loc).click()
        elif value == "0":
            self.find_element(*self.before_0_remind_loc).click()
        elif value == "5m":
            self.find_element(*self.before_5m_remind_loc).click()
        elif value == "10m":
            self.find_element(*self.before_10m_remind_loc).click()
        elif value == "15m":
            self.find_element(*self.before_15m_remind_loc).click()
        elif value == "30m":
            self.find_element(*self.before_30m_remind_loc).click()
        elif value == "1h":
            self.find_element(*self.before_1h_remind_loc).click()
        elif value == "1d":
            self.find_element(*self.before_1d_remind_loc).click()
        elif value == "2d":
            self.find_element(*self.before_2d_remind_loc).click()
        else:
            self.find_element(*self.before_7d_remind_loc).click()

    def get_after_edit_remind(self):
        return self.find_element(*self.edit_remind_loc).text

    def add_friend(self):
        self.find_element(*self.add_friend_loc).click()
        self.find_element(*self.my_friend_loc).click()
        self.find_element(*self.add_my_friend_1_loc).click()

    def schedule_confirm(self):
        self.find_element(*self.schedule_confirm_loc).click()

    # 查看日程
    schedule_title_loc  = (MobileBy.ID, "action_title")
    schedule_time_loc   = (MobileBy.ID, "action_time")
    schedule_remind_loc = (MobileBy.ID, "action_remind")

    def get_schedule_title(self):
        return self.wait_element(5, 0.5, *self.schedule_title_loc).text
        # return self.find_element(*self.schedule_title_loc).text

    def get_schedule_time(self):
        return self.find_element(*self.schedule_time_loc).text

    def get_after_save_remind(self):
        return self.find_element(*self.schedule_remind_loc).text

    # 修改日程
    schedule_list_1_loc       = (MobileBy.XPATH, "//android.widget.ListView/android.widget.LinearLayout[2]")
    schedule_list_1_title_loc = (MobileBy.XPATH, "//android.widget.ListView/android.widget.LinearLayout[2]/android.widget.TextView[1]")
    schedule_list_1_time_loc  = (MobileBy.XPATH, "//android.widget.ListView/android.widget.LinearLayout[2]/android.widget.TextView[2]")
    schedule_edit_loc         = (MobileBy.ID, "action_edit")

    def schedule_list_1(self):
        self.wait_element(5, 0.5, *self.schedule_list_1_loc).click()

    def schedule_edit(self):
        self.find_element(*self.schedule_edit_loc).click()


    # 删除日程
    schedule_delete_loc     = (MobileBy.ID, "action_delete")
    schedule_delete_confirm = (MobileBy.ID, "btn_ok")
    schedule_list_loc       = (MobileBy.ID, "calendar_list")

    def schedule_delete(self):
        self.find_element(*self.schedule_list_1_loc).click()
        self.find_element(*self.schedule_delete_loc).click()
        self.find_element(*self.schedule_delete_confirm).click()

    def schedule_list_size(self):
        self.wait_element(5, 0.5, *self.add_schedule_loc)
        return len(self.find_elements(*self.schedule_list_loc))-1
