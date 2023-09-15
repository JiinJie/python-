# -*- coding: utf-8 -*-
# @Time    : 2023/2/19 18:02
# @Author  : jinjie
# @File    : 006_1_zhanbao_server_new.py
import json
import os
import socket
import struct

def recv_data(conn,chunk_size=1024):
    # 获取头部信息长度
    has_read_size = 0
    bytes_list = []

    while has_read_size < 4:
        chunk = conn.recv(4 - has_read_size) #如果字节本身小于4则获取最后的内容
        has_read_size += len(chunk)
        bytes_list.append(chunk) #将所有字节放入列表
    header = b"".join(bytes_list)
    data_len = struct.unpack('i',header)[0]

    # 获取数据
    data_list = []
    has_read_size = 0
    while has_read_size < data_len:
        size = chunk_size \
            if(data_len - has_read_size) > chunk_size \
            else data_len - has_read_size

        chunk = conn.recv(size)
        data_list.append(chunk)
        has_read_size += len(chunk)

    data = b"".join(data_list)

    return data

def recv_file(conn,save_file_name,chunk_size=1024):
    # 获取文件路径
    save_file_path = os.path.join('files',save_file_name) #将文件放入files目录
    # 获取头部信息长度
    has_read_size = 0
    bytes_list = []

    while has_read_size < 4:
        chunk = conn.recv(4 - has_read_size) #如果字节本身小于4则获取最后的内容
        has_read_size += len(chunk)
        bytes_list.append(chunk) #将所有字节放入列表
    header = b"".join(bytes_list)
    data_len = struct.unpack('i',header)[0]

    # 获取文件数据
    file_object = open(save_file_path,mode='wb')
    has_read_data_size = 0
    while has_read_data_size < data_len:
        size = chunk_size if (data_len - has_read_data_size) > chunk_size else data_len - has_read_data_size
        chunk = conn.recv(size)
        file_object.write(chunk)
        file_object.flush()
        has_read_data_size += len(chunk)
    file_object.close()


def run():
    # 使用TCP连接
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # IP可复用(避免异常中断，ip未释放导致无法重启)
    sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    sock.bind(('127.0.0.1',8081))
    sock.listen(5)
    while True:
        conn,addr = sock.accept()

        while True:
            # 获取消息类型
            message_type = recv_data(conn).decode('utf-8')
            if message_type == 'close': #提示需要关闭与当前ip的会话
                print("连接已关闭")
                break
            # 文件格式 {'msg_type':'file','file_name':'xxx.xx'}
            # 消息格式 {'msg_type':'msg'}
            message_type_info = json.loads(message_type) #获取消息类型来判断走哪个方法

            if message_type_info['msg_type'] == "msg":
                data = recv_data(conn)
                print("接受到消息",data.decode('utf-8'))
            else:
                file_name = message_type_info['file_name']
                print("接收到文件，正在保存",file_name)
                recv_file(conn,file_name)


        conn.close()  #挥手操作

    sock.close()  #关闭连接


if __name__ == '__main__':
    run()