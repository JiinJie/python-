# -*- coding: utf-8 -*-
# @Time    : 2023/2/19 15:11
# @Author  : jinjie
# @File    : 002_2_sample_work_client.py

# 客户端
import socket

#向指定IP发送连接请求

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',8002))

# 连接成功后获取登录信息
message = client.recv(1024)
print(message.decode('utf-8'))

while True:
    content = input("请输入内容，退出请输入q或Q")
    if content.upper() == "Q":
        break
    client.sendall(content.encode('utf-8'))

    # 等待服务端回复消息
    reply = client.recv(1024)
    print(reply.decode('utf-8'))

#关闭连接
client.close()


