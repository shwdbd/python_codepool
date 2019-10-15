#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   series.py
@Time    :   2019/10/15 16:55:25
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   Series的构建与基本属性

1. demo_construct_by_list       用list构建Series
2. demo_construct_by_dict       用dict构建Series
3. demo_construct               纯手工构建

Series构造函数doc:
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html#pandas.Series

'''
import pandas as pd
import numpy as np


def demo_construct_by_list():
    """
    用list构建Series
    """
    list_data = ['a', 'b', 'c']
    index_data = [1, 2, 3]
    sr = pd.Series(data=list_data, index=index_data)
    print(sr)
    # 1    a
    # 2    b
    # 3    c
    # dtype: object


def demo_construct_by_dict():
    """
    用dict构建Series
    """
    dict_data = {
        'name': 'Jack',
        'age': 2
    }
    sr = pd.Series(data=dict_data)
    print(sr)
    # name    Jack
    # age        2
    # dtype: object


def demo_construct():
    """
    纯手工构建

    sr.values:np.ndarray
    sr.index
    sr.name sr.index.name
    """
    data = np.arange(5)
    sr = pd.Series(data, index=['a', 'b', 'c', 'd', 'e'], dtype=float)
    sr.index.name = 'tag'
    sr.name = 'score'
    print(sr)
    # tag
    # a    0.0
    # b    1.0
    # c    2.0
    # d    3.0
    # e    4.0
    # Name: score, dtype: float64

    # 常用属性
    print(len(sr))  # 5
    print(sr.ndim)  # 1
    print(sr.shape)  # (5,)
    print(sr.values)  # [0. 1. 2. 3. 4.]
    print(type(sr.values))  # <class 'numpy.ndarray'>
    # Index(['a', 'b', 'c', 'd', 'e'], dtype='object', name='tag')
    print(sr.index)
    print(type(sr.index))   # <class 'pandas.core.indexes.base.Index'>
    # print(len(sr))  # 5
    # print(len(sr))  # 5

    # 选择
    print('第2个元素=', sr[1])  # 1.0
    print('按index顺序选第2个元素=', sr.iloc[1:2])    # 1.0
    print('按index值选第2、5个元素=\n', sr.loc[['b', 'e']])    # 返回Series对象


if __name__ == "__main__":
    demo_construct_by_dict()
