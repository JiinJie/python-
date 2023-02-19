# -*- coding: utf-8 -*-
# @Time    : 2023/2/18 16:20
# @Author  : jinjie
# @File    : 012_1_mult_process_fork.py

import multiprocessing

def task():  #fork模式下，子进程中数据会直接拷贝父进程的
    print(name)
    file_object.write("xiaohong\n")
    file_object.flush() #将内容写入磁盘

if __name__ == '__main__':
    multiprocessing.set_start_method("fork")

    name = []
    file_object = open('x1.txt',mode='a+',encoding='utf-8')
    file_object.write("xiaoming\n")
    #file_object.flush()  # 如果在次数flush则内存中不会保留xiaoming，子进程中fileobject为空

    p1 = multiprocessing.Process(target=task)
    p1.start()

"""  
#出现两个xiaoming是因为拷贝时，xiaoming已经在内存中，
#子进程再次调用写入数据时会将其写入。父进程再次写入就出现重复数据
xiaoming
xiaohong
xiaoming
"""

