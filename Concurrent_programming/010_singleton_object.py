# -*- coding: utf-8 -*-
# @Time    : 2023/2/18 14:55
# @Author  : jinjie
# @File    : 010_singleton_object.py
import threading
import time


class Singleton:
    instance = None
    lock = threading.RLock()  #类变量中创建锁

    def __init__(self,name):
        self.name = name

    def __new__(cls, *args, **kwargs):
        # 先写在这里避免进入循环，可以优化性能
        if cls.instance:
            return cls.instance

        with cls.lock: ###添加锁
            # 如果instance不存在则创建新对象，如果存在则直接返回
            if cls.instance:
                return cls.instance
            time.sleep(0.1)
            cls.instance = object.__new__(cls) #创建一个空对象
            return cls.instance

def task():
    obj = Singleton('CCC')
    print(obj)


for i in range(5): # 创建五个对象
    t = threading.Thread(target=task)
    t.start()

""" 出现多个对象
<__main__.Singleton object at 0x000001C402F136D0>
<__main__.Singleton object at 0x000001C402F12E90>
<__main__.Singleton object at 0x000001C402F13AF0>
<__main__.Singleton object at 0x000001C402F136D0>
<__main__.Singleton object at 0x000001C402F12B00>
"""


# obj1 = Singleton('AAA')
# print(obj1)
# obj2 = Singleton('BBB')
# print(obj2)
# """ 两个对象共用一个实例
# <__main__.Singleton object at 0x0000023AF3043C70>
# <__main__.Singleton object at 0x0000023AF3043C70>
# """
