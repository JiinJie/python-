# -*- coding: utf-8 -*-
# @Time    : 2023/2/18 16:45
# @Author  : jinjie
# @File    : 013_mult_process_funcs.py


import multiprocessing
import os,time
import threading

def func():
    time.sleep(3)

def task(name):
    for i in range(5):
        t = threading.Thread(target=func)
        t.start()
    print(len(threading.enumerate())) #获取当前子进程中的所有线程，包括创建进程时的线程本身 5+1 = 6

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