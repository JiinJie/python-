# -*- coding: utf-8 -*-
# @Time    : 2023/2/18 14:41
# @Author  : jinjie
# @File    : aaa.py
import requests
import os

file_name = "aaaaa.png"
image_url = "https://t7.baidu.com/it/u=1297102096,3476971300&fm=193&f=GIF"
file_path = os.path.join("images",file_name)

res = requests.get(url=image_url,
                   headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"},
                   )

with open(file_path, mode="wb") as img_object:
    img_object.write(res.content)