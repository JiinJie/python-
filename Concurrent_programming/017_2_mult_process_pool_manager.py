# -*- coding: utf-8 -*-
# @Time    : 2023/2/18 19:18
# @Author  : jinjie
# @File    : 017_2_mult_process_pool_manager.py

# 在进程池中使用进程锁，需要基于Manager中的Lock和Rlock来实现

import time
import multiprocessing
from concurrent.futures.process import ProcessPoolExecutor

def task(lock):
    print("开始")
    # lock.acquire()
    # lock.relase()
    with lock:
        with open('f1.txt',mode='r',encoding='utf-8') as f:
            current_num = int(f.read())

        print("排队抢票了")
        time.sleep(1)
        current_num -= 1

        with open('f1.txt', mode='w', encoding='utf-8') as f:
            f.write(str(current_num))
        lock.release()

if __name__ == '__main__':
    pool = ProcessPoolExecutor(4)
    # lock_obj = multiprocessing.Rlock()  #不可以在线程池中使用
    manager = multiprocessing.Manager()
    lock_obj = manager.RLock()     #需使用manager中的进程锁
    for i in range(10):
        pool.submit(task,lock_obj)
