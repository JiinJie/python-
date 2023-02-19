# -*- coding: utf-8 -*-
# @Time    : 2023/2/18 10:26
# @Author  : jinjie
# @File    : 004_mult_threading_join.py

import threading

# t.join()
loop = 1000000000
number = 0

def _add(count):
    global number
    for i in range(count):
        number += 1
    print(number) #单个子线程执行完毕的number值

t = threading.Thread(target=_add,args=(loop,))
t.start()

t.join() #等待子线程完成后再执行join，主线程继续向下执行
print(number)  #此时打印number，子线程已经结束，获取的就是最终的结果

# join()添加多个子线程

def _add():
    global number
    for i in range(1000000):
        number += 1
    print(number) #单个子线程执行完毕的number值

def _sub():
    global number
    for i in range(1000000):
        number -= 1

t1 = threading.Thread(target=_add)
t2 = threading.Thread(target=_sub)

t1.start()
t1.join()  #t1线程执行完毕后才会执行主线程

t2.start()
t2.join()  #t2线程执行完毕后才会执行主线程

print(number)