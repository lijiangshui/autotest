# -*- coding:utf-8 -*-

#from selenium import webdriver
#from selenium.webdriver import Remote
from appium import webdriver
import os

PATH=lambda p:os.path.abspath(
os.path.join(os.path.dirname(__file__),p)                            
)

#
def app_driver():
    desired_caps={}
    desired_caps['device'] = 'android'
    desired_caps['platformName']='Android'
    desired_caps['browserName']=''
    desired_caps['version']='4.4.4'
    desired_caps['deviceName']='LA2-SN'#这是测试机的型号，可以查看手机的关于本机选项获得

    
    #desired_caps['app'] = PATH('F:\\ljs\\app-release.apk')#被测试的App在电脑上的位置
    desired_caps['app'] = PATH(u'F:\ljs\中南e行\SouthChina.apk')#被测试的App在电脑上的位置
    
    #如果知道被测试对象的apppage，appActivity可以加上下面这两个参数，如果不知道，可以注释掉，不影响用例执行
    #desired_caps['appPackage']='com.subject.zhongchou'
    #desired_caps['appActivity']='.ZhongChou'
    dr = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
    return dr

if __name__=="__main__":
    dr=app_driver()
    dr.quit()