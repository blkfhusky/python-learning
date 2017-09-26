#!/usr/bin/env python3     
# -*- coding: utf-8 -*-  
# create by zhuxc@joyowo.com
# 2017/9/26

from bs4 import BeautifulSoup

with open("Simple.html") as wb_data:
    soup = BeautifulSoup(wb_data, 'lxml')
    # print(soup)
    images = soup.select('body > div.main-content > ul > li > img')
    titles = soup.select('body > div.main-content > ul > li > h3')
    cates = soup.select('body > div.main-content > ul > li > p.meta-info')
    # print(cates)
    # cates = soup.select('body > div.main-content > ul > li > p.meta-info > span')

    # print(images, titles, sep="\n============\n")

for title, image,cate in zip(titles, images, cates):
    data = {
        "title": title.get_text(),
        "image": image.get('src'),
        "cate": list(cate.stripped_strings) # 注意cate和title之间的多对一关系
    }
    print(data)



    """
    图片地址：在元素右键检查，copy selector
    body > div.main-content > ul > li:nth-child(1) > img
    """