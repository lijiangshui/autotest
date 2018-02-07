# -*- coding: UTF-8 -*-
#!/usr/bin/env python
#
# ━━━━━━神兽出没━━━━━━
# 　　　┏┓　　　┏┓
# 　　┏┛┻━━━┛┻┓
# 　　┃　　　　　　　┃
# 　　┃　　　　　　　┃
# 　　┃　┳┛　┗┳　┃
# 　　┃　　　　　　　┃
# 　　┃　　　┻　　　┃
# 　　┃　　　　　　　┃
# 　　┗━┓　　　┏━┛Code is far away from bug with the animal protecting.
# 　　　　┃　　　┃    神兽保佑,代码无bug.
# 　　　　┃　　　┃
# 　　　　┃　　　┗━━━┓
# 　　　　┃　　　　　　　┣┓
# 　　　　┃　　　　　　　┏┛
# 　　　　┗┓┓┏━┳┓┏┛
# 　　　　　┃┫┫　┃┫┫
# 　　　　　┗┻┛　┗┻┛
#
# ━━━━━━感觉萌萌哒━━━━━━

def print_trangle():
    w = 9
    for i in range(0,w/2+1):
        for j in range(i,w/2):
            print "-",
        for k in range(0,2*i+1):
            print "*",
        print
            
def print_trangle1():
    w = 7
    for i in range(0,w):
        for j in range(i,w-1):
            print "-",
        for k in range(0,2*i+1):
            print "*",
        print
def print_diamond():
    w = 7
    for i in range(0,w):
        for j in range(i,w-1):
            print "-",
        for k in range(0,2*i+1):
            print "*",
        print
    
    for i in range(w-2,0,-1):
        for j in range(i,w-1):
            print "-",
        for k in range(0,2*i+1):
            print "*",
        print
            
if __name__ == "__main__":
    #print_trangle()
    #print_trangle1()
    print_diamond()
