# -*- coding: utf-8 -*-
# @Time    : 2023/2/18 10:38
# @Author  : jinjie
# @File    : 005_mult_threading_setDaemon.py


# t.setDaemon()  守护线程，必须放在start前
# t.setDameon(True)
# 设置为守护线程，主线程执行完毕后，子线程自动关闭（不会等待子线程全部执行完毕）
# t.setDameon(False)
# 关闭守护线程，主线程将等待子线程，子线程全部执行完毕后，主线程才会关闭  ，默认是False


import threading
import time


def task(arg):
    print("子线程开始执行")
    time.sleep(5)
    print(f"子线程执行完毕{arg}")



t = threading.Thread(target=task,args=(11,),daemon=True)
#t.setDaemon()  #True/False  该方法已经被弃用，直接在线程中该参数进行定义即可

t.start()

