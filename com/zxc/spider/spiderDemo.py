#!/usr/bin/env python3     
# -*- coding: utf-8 -*-  
# create by zhuxc@joyowo.com
# 2017/8/22

import requests

stockList=[]
crawlSite="http://hq.sinajs.cn/list=s_sh000002"
res = requests.get(crawlSite)
data = res.content
print(type(data).__name__)
print(data)
print(data.decode('gbk'))

stockList = data.split(b',')
print(stockList)