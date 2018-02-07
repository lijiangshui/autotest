# -*- coding:utf-8 -*-


from appium.webdriver.common.mobileby import MobileBy
from basepage import BasePage


class HomePage(BasePage):
    u"""首页"""

    menus_loc = (MobileBy.ID, "tabs")

    def menus(self):
        return self.find_element(*self.menus_loc)
