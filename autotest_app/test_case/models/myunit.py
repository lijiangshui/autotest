#-*- coding:utf-8 -*-

from appium import webdriver
import unittest
from app_driver import app_driver
import time
#import os


class MyTestInit(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.driver=app_driver()


	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()

		
if __name__=="__main__":
	unittest.main()

