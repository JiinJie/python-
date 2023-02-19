# -*- coding: utf-8 -*-
# @Time    : 2023/2/18 10:59
# @Author  : jinjie
# @File    : 006_mult_threading_other_args.py


import threading

# 获取一个线程名字
def task(arg):
    #name = threading.current_thread().getName() #getName被弃用
    name = threading.get_ident()
    id = threading.get_native_id()
    """get_ident()和get_native_id()获取的值相同"""
    print(arg)
    print(name,id)

for i in range(10):
    #threading.settrace()  通过settrace在线程运行前来定义名称
    t = threading.Thread(target=task,args=(11,),name='aaa')
    # setName已经被弃用
    #t.setName('aa-{}'.format(i))
    t.start()


