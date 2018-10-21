# Data-Acquisition
Python 数据采集

###### 课程地址：[python遇见数据采集_python数据采集教程-慕课网](https://www.imooc.com/learn/712)

`Python`  `2018年10月20日` `urllib` `BeautifulSoup`

[TOC]

## 课程介绍

- 环境搭建
- `urllib` 和 `BeautifulSoup`
- 存储数据到 `MySQL`
- 常见文档读取：`.txt`，`.pdf`
- 使用爬虫的注意事项

## Python 环境搭建

检查是否安装成功：

```powershell
> $ python
Python 3.6.5 |Anaconda, Inc.| (default, Mar 29 2018, 13:32:41) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 
>>> from urllib.request import urlopen
>>> from bs4 import BeautifulSoup
```

## urllib 的用法

- `urllib` 使 Python 3.x 中提供的一系列操作 URL 的库，它可以轻松地m模拟用户使用浏览器访问网页。

- 使用步骤：

  - 导入 urllib 库的 request 模块：

    ```python
    from urllib improt request
    ```

  - 请求 URL：

    ```python
    response = request.urlopen('https://www.xxx.com')
    ```

  - 使用响应对象输出数据

    ```python
    print(response.read().decode('utf-8))
    ```
- 模拟真实浏览器
    - 携带 User-Agent 头：
        ```python
        from urllib import request
        req = request.Request(url='www.xxx.com')
        req.add_header(key='User-Agent', val='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36')
        response = request.urlopen(req)
        print(response.read().decode('utf-8'))
        ```
- 使用 POST
    - 导入 urllib 库下面的 parse
        ```python
        from urllib import parse
        ```
    - 使用 urlencode 生成 post 数据
        ```python
        postData = parse.urlencode([
          (key1, val1),
          (key2, val2),
          (keyn, valn)
        ])
        ```
    - 使用 postData 发送 post 请求
        ```python
        request.urlopen(req, data=postData.encode('utf-8'))
        ```      
    - 得到请求状态
        ```python
        response.status
        ```        
    - 得到服务器的类型
        ```python
        response.reason
        ```
