# -*- coding: utf-8 -*-
# @Time    : 2023/2/18 18:35
# @Author  : jinjie
# @File    : 017_1_mult_process_pool.py

import time
from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor

def task(num):
    print(f"执行{num}")
    time.sleep(2)

if __name__ == '__main__':
    pool = ProcessPoolExecutor(4) #最多创建4个进程
    for i in range(10):
        pool.submit(task,i)

    pool.shutdown(True)

# 执行复杂的多进程操作（teardown）
import time
from concurrent.futures import ProcessPoolExecutor
import multiprocessing

def task(num):
    print(f"执行{num}")
    time.sleep(2)
    return num


def done_func(res):
    print(multiprocessing.current_process())
    time.sleep(1)
    print(res.result())
    time.sleep(1)


if __name__ == '__main__':

    pool = ProcessPoolExecutor(4)  # 最多创建4个进程
    for i in range(10):
        fur = pool.submit(task, i)
        fur.add_done_callback(fn=done_func) #done_func的调用是由主进程处理的
    print(multiprocessing.current_process())
    pool.shutdown(True)