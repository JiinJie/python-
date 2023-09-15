# -*- coding: utf-8 -*-
# @Time    : 2023/2/19 15:31
# @Author  : jinjie
# @File    : 003_2_upload_file_client.py

# 客户端代码


import time,os
import socket

client = socket.socket()
client.connect(('127.0.0.1',8081))

file_path = input("请输入要上传的文件")  #用户输入上传文件路径

# 先发送文件大小
file_size = os.stat(file_path).st_size  # 获取文件大小，发送至服务器
client.sendall(str(file_size).encode('utf-8'))

print("文件准备中...")
time.sleep(2)
print("开始上传...")
file_object = open(file_path,mode='rb')
read_size = 0
while True:
    chunk  = file_object.read(1024)
    client.sendall(chunk)
    read_size += len(chunk)
    if read_size == file_size:
        break
print("上传完毕，关闭连接..")
client.close()



