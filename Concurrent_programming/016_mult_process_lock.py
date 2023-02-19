# -*- coding: utf-8 -*-
# @Time    : 2023/2/18 18:35
# @Author  : jinjie
# @File    : 016_mult_process_lock.py

## 可能会出现进程冲突问题导致结果不为20
import multiprocessing
import time
from multiprocessing import Process,Value,Array

def func(n,):
    n.value = n.value + 1

if __name__ == '__main__':

    num = Value('i',0)
    for i in range(20):
        p = Process(target=func,args=(num,))
        p.start()

    time.sleep(3)
    print(num.value)


## 通过进程锁来操作多进程
import time
import multiprocessing

def task(lock):
    print("开始")
    lock.acquire() #第一个进程进来后直接卡住，让其他进程等待
    with open('f1.txt',mode='r',encoding='utf-8') as f:
        current_num = int(f.read())

    print("组队抢票")
    time.sleep(0.5)
    current_num -= 1

    with open('f1.txt',mode='w',encoding='utf-8') as f:
        f.write(str(current_num))
    lock.release()


if __name__ == '__main__':
    #multiprocessing.set_start_method("spawn")
    lock = multiprocessing.RLock()

    for i in range(10):
        p = multiprocessing.Process(target=task,args=(lock,))
        #进程锁可以作为参数，线程锁不可以传递
        p.start()


    # python早期版本必须加上sleep等待子进程，否则会报错
    #time.sleep(5)

    # 方式二：使用join
    process_list = []
    for i in range(10):
        p = multiprocessing.Process(target=task,args=(lock,))
        #进程锁可以作为参数，线程锁不可以传递
        p.start()
        process_list.append(p)

        #spawn模式特殊处理
        for item in process_list:
            item.join()  #等所有进程都进列表后再join