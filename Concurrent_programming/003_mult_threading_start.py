# -*- coding: utf-8 -*-
# @Time    : 2023/2/18 10:18
# @Author  : jinjie
# @File    : 003_mult_threading_start.py

import threading


# t.start()
loop = 1000000000
number = 0

def _add(count):
    global number
    for i in range(count):
        number += 1
    print(number) #单个子线程执行完毕的number值

t = threading.Thread(target=_add,args=(loop,))
t.start()

print(number)  #执行start后执行print 此时程序没有终止，在等待子线程的执行，因此number是个随机数


