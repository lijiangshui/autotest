#-*- coding:utf-8 -*-
import random,sys,time

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
