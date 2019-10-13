#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   csv_io.py
@Time    :   2019/10/13 19:04:53
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   csv导入导出示例（应移到pandas中)

使用pandas api进行cvs的读写
使用pandas 读 csv，文档：
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html#pandas.read_csv
使用pandas.DataFrame 写csv，文档：
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html#pandas.DataFrame.to_csv 

1. readcsv_simple           从csv中读取数据，不带index
2. readcsv_with_index       从csv中读取数据，指定index
3. readcsv_with_datefield   从csv中读取数据，指定日期字段

'''
import pandas as pd
import os


def readcsv_simple():
    """
    从csv中读取数据，不带index
    """
    csv_file = os.getcwd() + r'\wdbd\codepool\numpy_study\data\data.csv'
    df = pd.read_csv(filepath_or_buffer=csv_file)
    print(df)   # 直接读取，会有unnamed列 和 新增的index列


def readcsv_with_index():
    """
    从csv中读取数据，指定index
    """
    csv_file = os.getcwd() + r'\wdbd\codepool\numpy_study\data\data.csv'
    df = pd.read_csv(filepath_or_buffer=csv_file,  index_col=0)
    print(df)   # 指定第一列为index列
    print(df['trade_date'].dtype)


def readcsv_with_datefield():
    """
    从csv中读取数据，指定日期字段
    """
    csv_file = os.getcwd() + r'\wdbd\codepool\numpy_study\data\data.csv'
    df = pd.read_csv(filepath_or_buffer=csv_file,  index_col=1, parse_dates=True)
    print(df)   # 指定第一列为index列
    print(df.index.dtype)   # 日期格式已经转成datetime64


if __name__ == "__main__":
    readcsv_with_index()
