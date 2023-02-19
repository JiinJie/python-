# -*- coding: utf-8 -*-
# @Time    : 2023/2/18 16:02
# @Author  : jinjie
# @File    : 012_2_mult_process_spawn.py
# 使用spawn模式传递参数


import multiprocessing

def task(name,file_object):
    name,file_object = name,file_object
    print(name)
    file_object.write("xiaohong\n")
    file_object.flush()


if __name__ == '__main__':
    #multiprocessing.set_start_method("spawn")

    name = []
    file_object = open('x1.txt',mode='a+',encoding='utf-8')
    file_object.write("xiaoming\n")

    # 1.pickle模块是将python中所有的数据结构以及对象转换成bytes类型。
    # 2.多进程对象执行时存在不能被序列化的对象
    # 3.结合代码分析：

    p1 = multiprocessing.Process(target=task,args=(name,file_object,))
    p1.start()