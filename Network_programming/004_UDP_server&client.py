# -*- coding: utf-8 -*-
# @Time    : 2023/2/19 16:15
# @Author  : jinjie
# @File    : 004_UDP_server&client.py

### 使用UTP发送数据时，不需要创建连接，直接发送即可
# ----服务端----
import socket

# UDP使用 socket.SOCK_DGRAM ,TCP使用socket.SOCK_STREAM
server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #注意协议
server.bind(('127.0.0.1',8082))

while True:
    data,(host,port) = server.recvfrom(1024)  #也会发生阻塞，等待客户端发送消息
    print(data,host,port)
    server.sendto('ok,ok'.encode('utf-8'),(host,port))

# ----客户端----

import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
while True:
    text = input("请输入要发送的内容")
    if text.upper() == "Q":
        break
    client.sendto(text.encode('utf-8'),('127.0.0.1',8082))
    data,(host,port) = client.recvfrom(1024)
    print(data.decode('utf-8'))




