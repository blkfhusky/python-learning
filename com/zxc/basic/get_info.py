#!/usr/bin/env python3     
# -*- coding: utf-8 -*-  
# create by zhuxc@joyowo.com
# 2017/9/26
import requests
import json
from bs4 import BeautifulSoup


url = 'https://zhuanlan.zhihu.com/p/21563130'
agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
headers = {
    'User-Agent': agent
}
"""
session = requests.session()
# res = session.get(url, headers=headers)
res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'lxml')
print(res.text)
comments = soup.select(
    '#react-root > div > div > div.Layout-main.av-card.av-paddingBottom.av-bodyFont.Layout-titleImage--normal > div.PostComment > div.PostCommentList > div:nth-child(1) > div.CommentItem-content')
print(comments)
"""

url = 'https://zhuanlan.zhihu.com/api/posts/21563130/comments?limit=-1&offset=0'
res = requests.get(url, headers=headers)
comments = json.loads(res.text)
# print(comments)
print(len(comments))
for comment in comments:
    data = {
        "name": comment['author']['name'],
        "content": comment['content']
    }
    print(data)




