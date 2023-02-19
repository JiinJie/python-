# -*- coding: utf-8 -*-
# @Time    : 2023/2/18 9:44
# @Author  : jinjie
# @File    : 002_start_多进程.py

import time
import requests
import multiprocessing

#默认在创建新的进程后会创建一个线程来执行操作


url_list = [
    ("name11.mp4","https://www.baidu.com"),
    ("name22.mp4","https://www.baidu.com"),
    ("name33.mp4","https://www.baidu.com"),
]

def task(file_name,video_url):
    res = requests.get(video_url)
    with open(file_name,mode='wb') as f:
        f.write(res.content)
    print(time.time())  #计算程序单个进程花费时间，一共打印n次（进程执行完毕并释放资源）

if __name__ == '__main__':  #创建多进程时一定要使用main从入口函数开始操作
    print(time.time())
    for name,url in url_list:
        t = multiprocessing.Process(target=task,args=(name,url))
        t.start()

