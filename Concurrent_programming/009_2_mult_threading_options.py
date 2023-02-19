# -*- coding: utf-8 -*-
# @Time    : 2023/2/18 13:37
# @Author  : jinjie
# @File    : 009_2_mult_threading_options.py


# 子线程执行完毕后添加teardown操作
import time
import random
from concurrent.futures import ThreadPoolExecutor,Future

def task(video_url):
    print("开始执行任务",video_url)
    time.sleep(2)
    return random.randint(0,10) #随机返回一个random int
# task结束，teardown执行的方法
def done_func(resp):
    print(f"获取返回值{resp.result()}")
# 创建线程池
pool = ThreadPoolExecutor(10)

url_list = ["www.xx-{}.com".format(i) for i in range(200)]

for url in url_list:
# 提交任务到线程池
    future = pool.submit(task,url) # 返回这个submit对象
    future.add_done_callback(fn=done_func)  #子线程完成后有个回调过程
    """应用场景
    下载数据，写入数据库
    下载文字、图片，再次进行处理
    """
print("程序执行中")
pool.shutdown(True)  #等待线程池中所有线程执行完毕后才会继续执行主线程代码
print("程序执行完成")


#### 执行完毕后统一获取结果
import time
import random
from concurrent.futures import ThreadPoolExecutor,Future

def task(video_url):
    print("开始执行任务",video_url)
    time.sleep(2)
    return random.randint(0,10) #随机返回一个random int

pool = ThreadPoolExecutor(10)

future_list = []
for url in url_list:
    future = pool.submit(task,url)
    future_list.append(future)  #将子线程处理结果写入列表

pool.shutdown(True)
for fu in future_list: #最后统一处理结果
    print(fu.result())


