#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   df_where.py
@Time    :   2019/11/11 16:15:52
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   df.where 函数使用示范代码

df.where(cond, other=nan, inplace,...) 
是用不符合cond条件的数据用other填充，符合条件的数据用原来的值填充

! 注意 np.where 和 pd.where 用法不同
- np.where(cond, yes_value, no_value)
- df.where(cond, no_value)

API DOC:
pandas ： file:///C:/wjjpan/SynologyDrive/07%20dev/pandas_doc/reference/api/pandas.DataFrame.where.html#pandas.DataFrame.where
numpy : https://numpy.org/doc/1.16/reference/generated/numpy.where.html#numpy.where

'''
import pandas as pd
import numpy as np


def demo_where():
    """
    替换示例
    """
    df = pd.DataFrame(np.arange(0, 5), columns=['age'])
    print(df)
    df.where(df['age'] < 3, 'child', inplace=True)
    print(df)


def demo_np_where():
    """
    np.where 的使用示例
    """
    a = np.arange(5)
    print(a)
    b = np.where(a < 3, 'man', 'child')
    print(b)    # ['man' 'man' 'man' 'child' 'child']


if __name__ == "__main__":
    demo_np_where()
