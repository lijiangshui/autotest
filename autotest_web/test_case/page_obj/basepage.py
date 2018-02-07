# -*- coding:utf-8 -*-

'''
create on 2017-5-9 by lijiangshui
'''
# from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait


class BasePage(object):
    def __init__(self, appium_driver):
        self.driver = appium_driver

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

    def execute_script(self, src):
        return self.driver.execute_script(src)

    # 获取屏幕大小
    def get_size(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return (x, y)

    # 屏幕向左滑动
    def swipe_left(self, l, t, x1=0.75, y1=0.5, x2=0.05):
        # l=self.get_size()
        x1 = int(l[0] * x1)
        y1 = int(l[1] * y1)
        x2 = int(l[0] * x2)
        self.driver.swipe(x1, y1, x2, y1, t)

    # 屏幕向右滑动
    def swipe_right(self, l, t, x1=0.05, y1=0.5, x2=0.75):
        # l=self.get_size()
        x1 = int(l[0] * x1)
        y1 = int(l[1] * y1)
        x2 = int(l[0] * x2)
        self.driver.swipe(x1, y1, x2, y1, t)

    # 屏幕向上滑动
    def swipe_up(self, l, t, x1=0.5, y1=0.75, y2=0.25):
        # l = self.get_size()
        x1 = int(l[0] * x1)     # x坐标
        y1 = int(l[1] * y1)     # 起始y坐标
        y2 = int(l[1] * y2)     # 终点y坐标
        return self.driver.swipe(x1, y1, x1, y2, t)

    # 屏幕向下滑动
    def swipe_down(self, l, t, x1=0.5, y1=0.25, y2=0.75):
        # l = self.get_size()
        x1 = int(l[0] * x1)
        y1 = int(l[1] * y1)
        y2 = int(l[1] * y2)
        self.driver.swipe(x1, y1, x1, y2, t)

    # 屏幕点击
    def click_screen(self):
        l = self.get_size()
        x = int(l[0]*0.75)
        y = int(l[1]*0.75)
        self.driver.swipe(x, y, x, y, 1)

    def wait_element(self, timeout=10, poll_frequency=1, *loc):
        # timeout：超时的总时长  poll_frequency：循环去查询的间隙时间，默认0.5秒
        element = WebDriverWait(self.driver, timeout).\
                until(lambda x: x.find_element(*loc), "element not found")
        return element

    def get_element_center_point(self, *loc):
        x = self.find_element(*loc).location.get('x')
        y = self.find_element(*loc).location.get('y')
        return x, y

    def get_element_size(self, *loc):
        pass
