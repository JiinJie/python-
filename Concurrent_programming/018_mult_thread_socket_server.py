# -*- coding: utf-8 -*-
# @Time    : 2023/2/19 11:24
# @Author  : jinjie
# @File    : 018_mult_thread_socket_server.py

#多线程实现socket服务

## ---------服务端----------------

import socket
import threading

def task(conn):
    while True:
        client_data = conn.recv(1024)
        data = client_data.decode('utf-8')
        print("收到客户端发来的消息",data)
        if data.upper() == "Q":  #如果是结束标记Q则退出
            break
        conn.sendall("收到收到".encode('utf-8'))
    conn.close()

def run():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind(('127.0.0.1',8081))
    sock.listen(5)  #最多支持5人排队
    while True:  #子线程执行后（不需要等待处理完成），会继续返回主线程再次等待
        # 主线程等待客户端连接
        conn,addr = sock.accept()
        # 创建子线程执行task函数
        t = threading.Thread(target=task,args=(conn,))
        t.start()

    sock.close()


if __name__ == '__main__':
    run()

## ---------客户端----------------
import socket

# 客户端发起请求
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',8001))

while True:
    txt = input(">>>")
    client.sendall(txt.encode('utf-8'))
    if txt.upper() == "Q":
        break
    reply = client.recv(1024)
    print(reply.decode('utf-8'))

# 关闭连接，关闭连接时会向服务器发送空数据
client.close() #发送 q