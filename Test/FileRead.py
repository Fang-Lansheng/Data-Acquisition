#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  :  Thistledown
@Contact :  120768091@qq.com
@Software:  PyCharm
@File    :  FileRead.py
@Time    :  2018/10/22 10:52
"""
from urllib.request import urlopen

from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice

# 读取 TXT
# txtFile = urlopen('https://en.wikipedia.org/robots.txt')
txtFile = open('./robots.txt', encoding='utf-8')
print(txtFile.read())
txtFile.close()

# 读取 PDF
print('*' * 100)

# 获取文档对象
pdfFIle = open('naacl06-shinyama.pdf', 'rb')    # 以二进制读模式打开
# 创建与文档关联的解释器
parser = PDFParser(pdfFIle)
# PDF 文档的对象
doc = PDFDocument()
# 链接解释器和文档对象
parser.set_document(doc)
doc.set_parser(parser)
# 对文档进行初始化
doc.initialize("")  # 文档无密码，输入空字符串
# PDF 资源管理器
resource = PDFResourceManager()
# 参数分析器
laparam = LAParams()
# 聚合器
device = PDFPageAggregator(resource, laparams=laparam)
# 页面解释器
interpreter = PDFPageInterpreter(resource, device=device)
# 使用文档对象从页面读取内容
nPage = 1
for page in doc.get_pages():
    print('page %s ---------------------------------------------------------------------' % nPage)
    nPage = nPage + 1
    # 使用页面解析器来读取
    interpreter.process_page(page=page)
    # 使用聚合器来接收内容
    layout = device.get_result()
    for out in layout:
        if hasattr(out, 'get_text'):
            print(out.get_text())

