# -*- coding:utf-8 -*-
'''
Create on 2017-5-9 by lijiangshui
'''

import unittest,random,sys
sys.path.append("./models")
sys.path.append("./page_obj")
from models import myunit,function
from page_obj.loginpage import Login
import time

class LoginTest(myunit.MyTestInit):
    u"""登录"""
    
    def user_login_verify(self,username="",password=""):
        Login(self.driver).user_login(username,password)

    # 检查用户名、密码正确
    def test_login_6(self):
        u"""用户名、密码正确"""
        po=Login(self.driver)
        po.handle_splash_screen()
        self.user_login_verify(username="KC1237",password="csu123")
        time.sleep(5)

        #print self.driver
        cur_activity=self.driver.current_activity
        #self.assertEqual(".ui.activity.main.MainActivity",cur_activity)
        # 退出
        po.my_click()
        time.sleep(1)
        po.person_setting_click()
        time.sleep(1)
        po.log_out()
        time.sleep(4)


if __name__=="__main__":
    unittest.main()
