#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  :  Thistledown
@Contact :  120768091@qq.com
@Software:  PyCharm
@File    :  Wiki-Crawler.py
@Time    :  2018/10/22 10:07
"""

# 引入开发包
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

response = urlopen('https://en.wikipedia.org/wiki/Main_Page').read().decode('utf-8')
soup = BeautifulSoup(response, 'lxml')

listUrls = soup.findAll('a', href=re.compile('^/wiki/'))
# 输出所有的词条及其对应的 URL
for url in listUrls:
    # 过滤以 .jpg 或 .JPG 结尾的 URL
    if not re.search('\.(jpg|JPG)$', url['href']):
        # string 只能获取一个，get_text() 获取标签下所有的文字
        print(url.get_text(), '<--->', 'https://en.wikipedia.org' + url['href'])


