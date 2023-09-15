# -*- coding: utf-8 -*-
# @Time    : 2023/2/19 17:22
# @Author  : jinjie
# @File    : 006_2_zhanbao_client.py

import os,json,socket,struct


def send_data(conn,content):
    data = content.encode('utf-8')
    header = struct.pack('i',len(data))
    # 发送长度和数据包内容
    conn.sendall(header)
    conn.sendall(data)


def send_file(conn,file_path):
    file_size = os.stat(file_path).st_size
    header = struct.pack('i',file_size)
    conn.sendall(header)

    has_send_size = 0
    file_object = open(file_path,mode='rb')
    while has_send_size < file_size:
        chunk = file_object.read(1024)
        conn.sendall(chunk)
        has_send_size += len(chunk)
    file_object.close()


def run():
    client = socket.socket()
    client.connect(('127.0.0.1',8081))

    while True:
        """
        发送消息格式为：
        -消息：msg|hello
        -文件： file| xxx.png
        """
        content = input("请输入>>>") #"msg|hello"
        if content.upper() == "Q":
            send_data(client,"close")  #发送一个close文本给服务端表示关闭
            break

        input_text_list = content.split('|')
        if len(input_text_list) != 2:
            print("格式错误，请重新输入")

        message_type,info = input_text_list
        # 发消息
        if message_type == "msg":
            # 发消息类型
            send_data(client,json.dumps({"msg_type":"msg"}))

            # 发内容
            send_data(client,info)

        # 发文件
        elif message_type == "file":
            file_name = info.rsplit(os.sep,maxsplit=1)[-1] #使用sep进行路径分割（不同系统使用的不一致\/都有）  -1表示从最右侧进行分割

            # 发送和消息类型
            send_data(client,json.dumps({"msg_type":"file",'file_name':file_name}))

            # 发内容
            send_file(client,info)

    client.close()


if __name__ == '__main__':
    run()


