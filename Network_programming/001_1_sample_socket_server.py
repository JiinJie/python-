# -*- coding: utf-8 -*-
# @Time    : 2023/2/19 14:34
# @Author  : jinjie
# @File    : 001_1_sample_socket_server.py

### 服务端部分

import socket

# 1 监听本机的IP和端口
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(('127.0.0.1',8001))  #ip和端口
sock.listen(5)

while True:
    # 等待有人连接
    conn,addr = sock.accept()

    # 等待客户端发送消息
    client_data = conn.recv(1024)
    print(client_data.decode('utf-8'))

    # 给客户端回复消息
    conn.sendall('hello world'.encode('utf-8'))

    #关闭连接
    conn.close()


