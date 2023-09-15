# -*- coding: utf-8 -*-
# @Time    : 2023/2/19 17:09
# @Author  : jinjie
# @File    : 006_0_zhanbao_server_old.py


import socket
import struct

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(('127.0.0.1',8081))
sock.listen(5)
conn,addr = sock.accept()

# 固定读取4个字节（int类型）
header1 = conn.recv(4)
data_length1 = struct.unpack('i',header1)[0]  #读取header中整个报文的长度
has_recv_len = 0
data1 = b""
while True:
    now_len = data_length1 - has_recv_len
    if now_len > 1024:
        lth = 1024
    else:
        lth = now_len
    chunk = conn.recv(lth)  #当前recv长度大于1024则取1024，小于则取当前长度
    data1 += chunk
    if has_recv_len == data_length1:
        break
print(data1.decode('utf-8'))




