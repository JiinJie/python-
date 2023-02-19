# -*- coding: utf-8 -*-
# @Time    : 2023/2/18 15:23
# @Author  : jinjie
# @File    : 011_mult_process_start.py

# # 默认spawn模式不会引用父线程中的资源
# import multiprocessing
#
# def task():
#     print(name)
#
# if __name__ == '__main__':
#     multiprocessing.set_start_method("spawn")  #fork/spawn/forkserver
#     name = []
#
#     p1 = multiprocessing.Process(target=task)
#     p1.start()

"""
  File "F:\PyCharm_project\pythonProject1\011_mult_process_start.py", line 9, in task
    print(name)
NameError: name 'name' is not defined
"""

# 将父线程中资源传递至开辟的子线程中
import multiprocessing
import os,time
import threading

def func():
    time.sleep(3)

def task(name):
    for i in range(5):
        t = threading.Thread(target=func)
        t.start()
    print(len(threading.enumerate())) #获取当前子进程中的所有线程，包括创建进程时的线程本身

    print(name)
    print(os.getpid())  #获取当前子进程pid
    print(os.getppid())  #获取当前子进程的父进程的pid

if __name__ == '__main__':
    multiprocessing.set_start_method("spawn")  #fork/spawn/forkserver
    name = []

    p1 = multiprocessing.Process(target=task,args=(name,))
    p1.daemon = True  # 开启进程守护
    p1.name = "hahaha"  # 命名进程
    p1.start()  # 进程开始执行
    p1.join() #等待进程结束
