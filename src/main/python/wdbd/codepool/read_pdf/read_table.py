#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   read_table.py
@Time    :   2022/06/15 16:47:25
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   使用pdfplumber读取表格内容
'''
import pdfplumber


if __name__ == "__main__":
    print(pdfplumber.__version__)

    file_path = r"src\main\python\wdbd\codepool\read_pdf\pdf\ca-warn-report.pdf"
    pdf = pdfplumber.open(file_path)
    p0 = pdf.pages[0]
    table = p0.extract_table()
    print(table[0])
    print(table[3])
    