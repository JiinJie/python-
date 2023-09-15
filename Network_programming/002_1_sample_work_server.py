# -*- coding: utf-8 -*-
# @Time    : 2023/2/19 14:58
# @Author  : jinjie
# @File    : 002_1_sample_work_server.py

# 案例 智障客服

# 服务端
import socket

# 1 监听本机的IP和端口
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(('127.0.0.1',8002))  #ip和端口
sock.listen(5)

while True:
    # 等待有人连接
    conn,addr = sock.accept()
    print("用户接入中...")

    # 给客户端回复消息
    conn.sendall('欢迎进入客服系统，请输入您的提问'.encode('utf-8'))

    while True:
        # 等待客户端发送消息
        client_data = conn.recv(1024)
        if not client_data:
            break
        data_str = client_data.decode('utf-8')
        print(f"客户端提问:{data_str}")
        conn.sendall(f"你说的对，就是'{data_str}'".encode('utf-8'))

    print("用户连接已断开")
    conn.close()



