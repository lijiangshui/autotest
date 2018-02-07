# -*- coding:utf-8 -*-

'''
'''

from appium.webdriver.common.mobileby import MobileBy
from basepage import BasePage
from loginpage import Login
import time

class Login(BasePage):
    login_page_loc=(MobileBy.ID,"tabs")
    login_username_loc=(MobileBy.ID,"edit_login_account")
    login_password_loc=(MobileBy.ID,"edit_login_password")
    login_button_loc=(MobileBy.ID,"app_login")
    
    # 滑动引导页，跳转到首页，再跳转登录页
    def handle_splash_screen(self):
	for i in range(3):
	    # 一定要设定一个等待时间，否则报错
	    time.sleep(0.5)
	    self.swipe_left(500)
	self.click_screen()
	print self.driver.current_activity
	self.find_element(*self.login_page_loc).click()
	    
    def login_username(self,username):
	self.find_element(*self.login_username_loc).clear()
	self.find_element(*self.login_username_loc).send_keys(username)

    def login_password(self,password):
	self.find_element(*self.login_password_loc).clear()
	self.find_element(*self.login_password_loc).send_keys(password)

    def login_button(self):
        self.find_element(*self.login_button_loc).click()

    def user_login(self,username="username",password="pwd"):
	self.login_username(username)
	self.login_password(password)
	self.login_button()
	    

    user_login_success_loc=(MobileBy.ID,"tv_my_name")

    def user_login_success(self):
        return self.find_element(*self.user_login_success_loc).text
