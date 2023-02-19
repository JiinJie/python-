# -*- coding: utf-8 -*-
# @Time    : 2023/2/18 9:35
# @Author  : jinjie
# @File    : 001_start_多线程.py

import time
import requests
import threading

"""
# 基本结构
def func(a1,a2,a3): #定义需要并发执行的方法
    pass

t = threading.Thread(target=func,args=(11,22,33)) #target是方法名
t.start()  #开始执行并发操作
"""

url_list = [
    ("name11.mp4","https://www.baidu.com"),
    ("name22.mp4","https://www.baidu.com"),
    ("name33.mp4","https://www.baidu.com"),
]


def task(file_name,video_url):
    res = requests.get(video_url)
    with open(file_name,mode='wb') as f:
        f.write(res.content)
    print(time.time())  #计算程序单个线程花费时间，一共打印n次（n个线程）

for name,url in url_list:
    t = threading.Thread(target=task,args=(name,url)) #args是方法的入参
    t.start()

#在此处记录的时间是所有线程执行完毕后的时间
# print(time.time())