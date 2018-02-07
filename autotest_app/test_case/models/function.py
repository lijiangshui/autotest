#-*- coding:utf-8 -*-
import random,sys,time
import datetime
from appium import webdriver


def create_mobile_num():
    mobile_number_segment=['134','135','136','137''138','139','147','150','151','152','157','158','159''182','183','187','188']
    mobile_number_segment=random.sample(mobile_number_segment,1)
    number="0123456789"
    slice=random.sample(number,8)
    s=""
    for c in slice:
            s+=c
            
    if s[0]=='0':
            s=random.sample("123456789",1)[0]+s[1:]
    
    return mobile_number_segment[0]+s

def create_email():
    number="0123456789"
    slice=random.sample(number,3)
    s=""
    for c in slice:
	s+=c
    email = "li"+s+"@126.com"
    return email

def get_week_day(date):
    week_day = {
        0: '星期1',
        1: '星期2',
        2: '星期3',
        3: '星期4',
        4: '星期5',
        5: '星期6',
        6: '星期天',
    }
    day = date.weekday() #weekday()可以获得是星期几
    return  week_day[day]
#print(datetime.datetime.now())
#print(get_week_day(datetime.datetime.now()))    
    

if __name__=="__main__":
    print create_email()
