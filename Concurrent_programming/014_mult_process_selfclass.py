# -*- coding: utf-8 -*-
# @Time    : 2023/2/18 17:18
# @Author  : jinjie
# @File    : 014_mult_process_selfclass.py

# 自定义线程类

import multiprocessing

class MyProcess(multiprocessing.Process):
    def run(self):
        print("创建自定义进程",self._args)

def func():
    pass

if __name__ == '__main__':
    multiprocessing.set_start_method("func")
    p = MyProcess(args=('ddd',))
    p.start()
    print("进程执行中..")

    # 通常情况下创建的进程不会超过cpu线程的个数，同时，一般创建偶数个进程
    cpu_num = multiprocessing.cpu_count()
    print(cpu_num)