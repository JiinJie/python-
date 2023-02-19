# -*- coding: utf-8 -*-
# @Time    : 2023/2/18 11:31
# @Author  : jinjie
# @File    : 008_mult_threading_lock.py

####方法一：手动加锁
import threading

lock_obj = threading.RLock()  #冲突的程序需要使用同一个锁，如果方法有自己的锁，那么锁的意义就失效了

loop = 1000000
number = 0

def _add(count):
    lock_obj.acquire()  #方法必须要加锁(需要申请锁，如果没有申请到则继续等待)
    global number
    for i in range(count):
        number += 1
        lock_obj.release()  #方法运行结束，释放锁

def _sub(count):
    lock_obj.acquire()
    global number
    for i in range(count):
        number -= 1
        lock_obj.release()


t1 = threading.Thread(target=_add,args=(loop,))
t2 = threading.Thread(target=_sub,args=(loop,))

t1.start()
t2.start()

t1.join()
t2.join()

print(number)
# ------------------------------------------
####方法二：with上下文自动执行
import threading

def task():
    print("开始")
    with lock_obj:  #with自动加锁和释放
        global num
        for i in range(1000000):
            num += 1
    print(num)

for i in range(2):  #创建两个线程同时执行
    t = threading.Thread(target=task)
    t.start()

# ------------------------------------------
#### 同步锁 lock
import threading

num = 0
lock_obj = threading.Lock()

def task():
    print("子线程开始")
    lock_obj.acquire()
    global num
    for i in range(100000):
        num += 1
        lock_obj.release()
    print(num)

for i in range(2):
    t = threading.Thread(target=task)
    t.start()

# ------------------------------------------
#### 递归锁 Rlock
import threading

num = 0
lock_obj = threading.RLock()

def task():
    print("线程开始")
    lock_obj.acquire()
    lock_obj.acquire()  #可以支持嵌套锁
    global num
    for i in range(100000):
        num += 1
    lock_obj.release()
    lock_obj.release()  #可以解开多次
    print(num)

# ------------------------------------------
# 死锁
import threading
import time

lock_1 = threading.Lock()
lock_2 = threading.Lock()

def task1():
    lock_1.acquire()
    time.sleep(3)
    lock_2.acquire()
    print(111)
    lock_2.release()
    print(222)
    lock_1.release()
    print(333)

def task2():
    lock_2.acquire()
    time.sleep(3)
    lock_1.acquire()
    print('aaa')
    lock_1.release()
    print('bbb')
    lock_2.release()
    print('ccc')


t1 = threading.Thread(target=task1)
t1.start()

t2 = threading.Thread(target=task2)
t2.start()


