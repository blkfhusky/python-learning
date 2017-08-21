#!/usr/bin/env python3     
# -*- coding: utf-8 -*-  
# create by zhuxc@joyowo.com
# 2017/8/21

# str = input("输入整行：")
# print("整行内容为：", str)

import os
print("=============")
file = open("test.txt", "r", 1)
print("文件操作：", file.readlines())

position = file.tell()
print("当前文件位置为：", position)

print(os.getcwd())