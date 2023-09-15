# -*- coding: utf-8 -*-
# @Time    : 2023/2/19 15:30
# @Author  : jinjie
# @File    : 003_1_upload_file_server.py

# 服务端

import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(('127.0.0.1',8002))  #ip和端口
sock.listen(5)


# 准许客户端请求
conn,addr = sock.accept()

# 接收文件大小
data = conn.recv(1024)
total_file_size = int(data.decode('utf-8'))

# 接收文件内容
file_object = open('xxx.png',mode='wb')
recv_size = 0
while True:
    # 每次最多接收1024字节
    data = conn.recv(1024)
    file_object.write(data)
    file_object.flush() #将内存数据刷入磁盘文件

    recv_size += len(data)
    #上传完成
    if recv_size == total_file_size:
        break

# 接收完成，关闭连接
conn.close()
sock.close()
