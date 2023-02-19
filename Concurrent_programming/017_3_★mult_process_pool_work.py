# -*- coding: utf-8 -*-
# @Time    : 2023/2/18 19:27
# @Author  : jinjie
# @File    : 017_3_★mult_process_pool_work.py
import os
import time
# 需求批量读取文件中的访问次数和ip数

# 方法1 使用manager.dict()
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Manager

def task(file_name,count_dict):
    ip_set = set()
    total_count = 0
    ip_count = 0
    file_path = os.path.join("files",file_name)
    file_object = open(file_path,mode='r',encoding='utf-8')
    for line in file_object:
        if not line.strip():
            continue
        user_ip = line.split(" - -",maxsplit=1)[0].split(",")[0]
        total_count += 1
        if user_ip in ip_set:
            continue
        ip_count += 1
        ip_set.add(user_ip)
    count_dict[file_name] = {"total":total_count,'ip':ip_count}
    time.sleep(1)

def run():
    # 根据目录读取文件并初始化字典
    pool = ProcessPoolExecutor(4)
    with Manager() as manager:
        """ count_dict = {"20210322.log":{"total":10000,'ip':800}} """
        count_dict = manager.dict()  #dict是进程共享的

        for file_name in os.listdir("files"): #将所有文件加入线程池
            pool.submit(task,file_name,count_dict)

        pool.shutdown(True)
        for k,v in count_dict.items():
            print(k,v)

# if __name__ == '__main__':
#     run()




#  方法二：使用闭包,和回调函数
import os
import time
from concurrent.futures import ProcessPoolExecutor


def tasK(file_name):
    ip_set = set()
    total_count = 0
    ip_count = 0
    file_path = os.path.join("files",file_name)
    file_object = open(file_path,mode='r',encoding='utf-8')
    for line in file_object:
        if not line.strip():
            continue
        user_ip = line.split(" - -",maxsplit=1)[0].split(",")[0]
        total_count += 1
        if user_ip in ip_set:
            continue
        ip_count += 1
        ip_set.add(user_ip)
    time.sleep(1)

    return{"total":total_count,'ip':ip_count}


def outer(info,file_name):
    def done(res,*args,**kwargs):
        info[file_name] = res.result()

    return done


def run():
    info = {}
    pool = ProcessPoolExecutor(4)
    for file_name in os.listdir("files"):
        fur = pool.submit(task,file_name)
        fur.add_done_callback(outer(info,file_name)) #通过闭包函数传参

    pool.shutdown(True)
    for k,v in info.items():
        print(k,v)


if __name__ == '__main__':
    run()


