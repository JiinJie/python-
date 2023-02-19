# -*- coding: utf-8 -*-
# @Time    : 2023/2/18 13:42
# @Author  : jinjie
# @File    : 009_3_★mult_threading_instance.py

# 线程池的实例
"""
实现文件的批量下载和重命名
"""
import os,csv
import requests
from concurrent.futures import ThreadPoolExecutor


def download_func(file_name,image_url):
    print(f"开始执行子线程操作{file_name}")
    res = requests.get(url=image_url,
                       headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"},
                       )

    if not os.path.exists('images'):
        print("正在创建images文件夹")
        # 如果目录不存在则自动创建
        os.makedirs("images")
    file_path = os.path.join("images",file_name)
    # 将图片写入目录
    with open(file_path,mode="wb") as img_object:
        img_object.write(res.content)


# 创建线程池，维护10个线程
pool = ThreadPoolExecutor(10)

with open("download_img.csv",mode='r',encoding='utf-8') as file_object:
    reader = csv.reader(file_object)
    for name_id,name,url in reader:
        file_name = "{}.png".format(name)
        pool.submit(download_func,file_name,url)  # 提交任务



# import csv
# with open("download_img.csv",mode='r',encoding='utf-8') as file_object:
#     reader = csv.reader(file_object)
#     for name_id,name,url in reader:
#         print(name_id,name,url)

