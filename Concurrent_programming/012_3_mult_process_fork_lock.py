# -*- coding: utf-8 -*-
# @Time    : 2023/2/18 16:35
# @Author  : jinjie
# @File    : 012_3_mult_process_fork_lock.py
import multiprocessing
import time
import threading


def func():
    print("来了")
    with lock:
        print(666)
        time.sleep(1)


def task():
    #子线程中也被加锁，是子进程中的主线程申请的锁。
    for i in range(5):
        t = threading.Thread(target=func)
        t.start()
    #这个子进程中其他所有线程都无法直接操作，必须等待解锁才可以操作func中的锁
    #lock.release()  #解锁

if __name__ == '__main__':
    multiprocessing.set_start_method("fork")
    name = []
    lock = threading.RLock()  #主进程中定义一个锁
    lock.acquire() #当前是加锁状态

