#!/usr/bin/env python3     
# -*- coding: utf-8 -*-  
# create by zhuxc@joyowo.com
# 2017/8/22

import requests
# import bs4
from bs4 import BeautifulSoup

html = requests.get("https://hangzhou.anjuke.com/").text
soup = BeautifulSoup(html, "lxml")
# print(soup)
# href = soup.xpath('//li/a/text()')
# print(href)

from lxml import etree
"""
    BeautifulSoup不支持xpath。
    lxml兼容BeautifulSoup，并且支持xpath，速度更快
"""

Selector = etree.HTML(html)
href = Selector.xpath('//a/@href')
print(href)
