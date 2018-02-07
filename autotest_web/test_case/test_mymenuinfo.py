# -*- coding:utf-8 -*-
'''
Create on 2017-5-9 by lijiangshui
'''

from models import myunit
from models import function
# from page_obj.loginpage import Login
from page_obj.mymenupage import MyMenuInfo
import unittest
import time
import datetime
import sys
sys.path.append("./models")
sys.path.append("./page_obj")
reload(sys)
sys.setdefaultencoding("utf-8")


class MyMenutest(myunit.MyTestInit):
    u"""个人信息"""

    po = None

    @classmethod
    def setUpClass(cls):
        global po
        super(MyMenutest, cls).setUpClass()
        po = MyMenuInfo(cls.driver)
        po.click_my_menu()

    # def test_person_1(self):
    #    global po
    #    #po = MyMenuInfo(self.driver)
    #    #po.click_my_menu()
    #    personal_type = po.get_personal_type()
    #    personal_my_department = po.get_personal_my_department()
    #    personal_sex = po.get_personal_sex()
    #    #person_my_number = po.get_personal_my_number()
    #    #personal_email = po.get_personal_email()
    #    #personal_lable.po.get_personal_lable()
    #    #print person_type,personal_my_department,personal_sex
    #    self.assertEqual(u"学生", personal_type)
    #    self.assertEqual(u"软件学院", personal_my_department)
    #    self.assertEqual(u"男", personal_sex)

    # def test_person_2(self):
    #    global po
    #    #po = MyMenuInfo(self.driver)

    #    # 手机号码
    #    #number = function.create_mobile_num()
    #    #po.set_personal_my_number(number)
    #    #time.sleep(1)
    #    #my_number = po.get_personal_my_number()
    #    #self.assertEqual(number, my_number)
    #    #
    #    #time.sleep(1)
    #    ## 邮箱
    #    #email = function.create_email()
    #    #po.set_personal_email(email)
    #    #my_email = po.get_personal_email()
    #    #self.assertEqual(email,my_email())
    #    number = function.create_mobile_num()
    #    email = function.create_email()
    #    number_email_is_see = po.set_number_email(number, email)
    #    my_number = po.get_personal_my_number()
    #    my_email = po.get_personal_email()
    #    # 手机号码
    #    self.assertEqual(number, my_number[0])
    #    # 号码是否可见
    #    #print number_email_is_see[0][0],number_email_is_see[0][1]
    #    #print "---------------------"
    #    #print my_number[1][0],my_number[1][1]
    #    #self.assertEqual(number_email_is_see[0], my_number[1])
    #    # 邮箱
    #    self.assertEqual(email, my_email[0])
    #    # 邮箱是否可见
    #    #print number_email_is_see[1][0], number_email_is_see[1][1]
    #    #self.assertEqual (number_email_is_see[1], my_email[1])
    #    #print my_email[1][0],my_email[1][1]
    #    time.sleep(1)
    #    # 个人标签
    #    set_lable = po.set_personal_label()
    #    time.sleep(1)
    #    get_label = po.get_personal_label()
    #    self.assertEqual(set_lable, get_label)

    # 创建日程
    def test_schedul_1(self):
        # po = MyMenuInfo(self.driver)
        po.my_schedule()
        # # time.sleep(1)
        # # 创建前日程数
        # pre_nums = po.schedule_list_size()
        # po.add_schedule()
        # # time.sleep(1)
        # content = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
        # po.edit_content(content)
        # po.select_start_end_time("start", "minutes", 6)
        # # time.sleep(1)
        # po.confirm_select_time()
        # po.select_start_end_time("end", "minutes", 9)
        # # time.sleep(1)
        # po.confirm_select_time()
        # po.remind("10m")

        # # content = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
        # # po.edit_content(content)
        # # time.sleep(2)
        # # start_time = time.\
        # #   strftime("%Y%m%d%H%M", time.localtime(time.time()+1200))
        # # po.start_end_time(start_time)
        # # end_time = time.\
        # #   strftime("%Y%m%d%H%M", time.localtime(time.time()+3600))
        # # po.start_end_time(end_time,2)
        # # po.remind("-1")
        # # po.add_friend()
        # po.schedule_confirm()
        # # time.sleep(3)
        # # 创建后日程数
        # cur_nums = po.schedule_list_size()
        # self.assertEqual(pre_nums, cur_nums)

    # 修改日程
    def test_schedul_2(self):
        # po = MyMenuInfo(self.driver)
        # po.my_schedule()
        # time.sleep(1)
        po.schedule_list_1()
        po.schedule_edit()
        content = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
        po.edit_content(content)
        po.select_start_end_time("start", "minutes", 6)
        # time.sleep(3)
        start_time = po.get_start_end_time()
        start_date = datetime.\
            datetime(start_time[0], start_time[1], start_time[2])
        start_week_day = function.get_week_day(start_date)
        # time.sleep(1)
        po.select_start_end_time("end", "minutes", 9)
        end_time = po.get_start_end_time()
        end_date = datetime.datetime(end_time[0], end_time[1], end_time[2])
        end_week_day = function.get_week_day(end_date)
        schedule_time =\
            str(start_time[1]) + u"月" + str(start_time[2]) + u"日" +\
            start_week_day + " " + \
            str(start_time[3]) + ':' + str(start_time[4]) + u"分" + '-' +\
            str(end_time[1]) + u"月" + str(end_time[2]) + u"日" +\
            end_week_day + " " +\
            str(end_time[3]) + ':' + str(end_time[4]) + u"分"
        po.remind("5m")
        remind = po.get_after_edit_remind()
        # po.add_friend()
        po.schedule_confirm()
        # 系统问题 需要返回上级重新进入才刷新
        po.back()
        po.my_schedule()
        po.schedule_list_1()

        self.assertEqual(content, po.get_schedule_title())
        self.assertEqual(schedule_time, po.get_schedule_time())
        self.assertEqual(remind, po.get_after_save_remind())
        po.back()

    # 删除日程
    def test_schedul_3(self):
        # 删除前日程数
        pre_nums = po.schedule_list_size()
        po.schedule_delete()
        # 删除后日程数
        cur_nums = po.schedule_list_size()
        self.assertEqual(pre_nums, cur_nums)

    @classmethod
    def tearDownClass(cls):
        super(MyMenutest, cls).tearDownClass()


if __name__ == "__main__":
    unittest.main()
