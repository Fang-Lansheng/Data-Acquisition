#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  :  Thistledown
@Contact :  120768091@qq.com
@Software:  PyCharm
@File    :  urllib_test.py
@Time    :  2018/10/21 22:34
"""
from urllib.request import urlopen
from urllib.request import Request
from urllib import parse

req = Request("http://www.thsrc.com.tw/tw/TimeTable/SearchResult")

postData = parse.urlencode([
    ('StartStation', '2f940836-cedc-41ef-8e28-c2336ac8fe68'),
    ('EndStation', 'fbd828d8-b1da-4b06-a3bd-680cdca4d2cd'),
    ('DepartueSearchDate', '2018/10/21'),
    ('DepartueSearchTime', '06:30'),
    ('StartStationName', '南港站'),
    ('EndStationName', '桃園站'),
    ('SearchType', 'S')
])

req.add_header('Origin', 'http://www.thsrc.com.tw')
req.add_header('Referer', 'http://www.thsrc.com.tw/index.html')
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36')

response = urlopen(req, data=postData.encode('utf-8'))

print(response.read().decode('utf-8'))
