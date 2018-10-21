#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  :  Thistledown
@Contact :  120768091@qq.com
@Software:  PyCharm
@File    :  BeautifulSoup_Test.py
@Time    :  2018/10/21 22:50
"""
import re

from bs4 import BeautifulSoup as bs

html_doc = """
<html><head><title>The Dormouse's story<a>Hello</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://exampleScom/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = bs(html_doc, 'lxml')

# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.title.get_text())
# print(soup.p)
# print(soup.p.name)
# print(soup.a)
# print(soup.find(id='link2').string)
# print(soup.find(id='link2').get_text())
#
# print(soup.find_all('a'))
# for link in soup.find_all('a'):
#     print(link.string)

# print(soup.find('p', {'class':'story'}))

print('-'* 100)
print(soup.findAll('a', href=re.compile('^http://example\.com')))
