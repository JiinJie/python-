# -*- coding: utf-8 -*-
# @Time    : 2023/2/18 17:32
# @Author  : jinjie
# @File    : 015_mult_process_share_memory.py

# 示例

import multiprocessing

def task(data):
    data.append(666)

if __name__ == '__main__':
    data_list = []
    p = multiprocessing.Process(target=task,args=(data_list,))
    p.start()
    p.join()
    print(f"主进程 data_list={data_list}")

