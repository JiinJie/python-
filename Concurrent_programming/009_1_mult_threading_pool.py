# -*- coding: utf-8 -*-
# @Time    : 2023/2/18 12:56
# @Author  : jinjie
# @File    : 009_1_mult_threading_pool.py

# 线程池

# 基础使用
import time
from concurrent.futures import ThreadPoolExecutor

def func(args1,args2):
    print("开始执行")
    print(args1,args2)
    pass


pool = ThreadPoolExecutor(100)  #线程池最大使用数为100
# 将该方法提交至线程池
pool.submit(fn=func,'args1','args2') #args直接添加

# 线程池实例
import time
from concurrent.futures import ThreadPoolExecutor

def task(video_url,num):
    print("开始执行任务",video_url)
    time.sleep(5)
# 创建线程池
pool = ThreadPoolExecutor(10)

url_list = ["www.xx-{}.com".format(i) for i in range(200)]

for url in url_list:
# 提交任务到线程池
    pool.submit(task,(url,2)) #传递task方法，和url和num参数
print("程序执行中")
pool.shutdown(True)  #等待线程池中所有线程执行完毕后才会继续执行主线程代码
print("程序执行完成")




