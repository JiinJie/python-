# -*- coding: utf-8 -*-
# @Time    : 2023/2/19 14:58
# @Author  : jinjie
# @File    : 001_2_sample_socket_client.py


### 客户端部分
import socket

# 向指定IP建立连接
client = socket.socket()
client.connect(('127.0.0.1',8001))

# 发送请求
#client.sendall(b'hello')  #以byte的形式发送
client.sendall('hello'.encode('utf-8'))
reply = client.recv(1024)
print(reply)

#关闭连接
client.close()
