# -*- coding: utf-8 -*-
# @Time    : 2023/2/18 11:21
# @Author  : jinjie
# @File    : 007_mult_threading_selfclass.py

import threading

# 自定义线程类，将需要的操作写入run方法中

class MyThread(threading.Thread): #继承自Thread
    def run(self) -> None:  #执行线程时会直接执行run方法
        print('开始执行线程')
        #print('开始执行线程',self_args)  #self_args报错


t = MyThread(args=(10,))
t.start()