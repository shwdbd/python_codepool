#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   df_null.py
@Time    :   2019/10/15 17:38:47
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   空值的处理

1. demo_dropna      df.dropna 删除空值的数据
2. demo_isna_notsa  空值判断
3. demo_fillna      控制填充
4. demo_fillna_method   演示fillna不同method的用法
5. demo_fillna_dict     演示使用dict按列使用不同值替换

dropna:
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html#pandas.DataFrame.dropna

fillna:(value=None, method=None, axis=None, inplace=False, limit=None, downcast=None)
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.fillna.html#pandas.DataFrame.fillna
- method:
    - backfill/bfill    后一行填充
    - ffill/pad         前一行的值填充
    - None  指定值填充
- limit: 替换N个后停止
TODO 使用dict，按列填充不同的值


isna:
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.isna.html#pandas.DataFrame.isna
nasa:
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.notna.html#pandas.DataFrame.notna

'''
import pandas as pd
import numpy as np


def get_df():
    df = pd.DataFrame({"name": ['Alfred', 'Batman', 'Catwoman'],
                       "toy": [np.nan, 'Batmobile', 'Bullwhip'],
                       "born": [pd.NaT, pd.Timestamp("1940-04-25"),
                                pd.NaT]})
    return df


def demo_dropna():
    """
    df.dropna 删除空值的数据

    可按index，也可按columns进行搜索

    """
    df = get_df()
    print(df)

    print(df.dropna(axis='index'))   # 按行搜索
    print(df.dropna(how='any', subset=['name', 'toy']))  # 按行搜索，指定找null的列名

    print('{0} 执行完毕！ {0}'.format('='*10))


def demo_isna_notsa():
    """
    判断是否有空值
    """
    df = get_df()

    print(df.isna())    # 返回一个boolean的DataFrame
    print(df.notna())

    print('{0} 执行完毕！ {0}'.format('='*10))


def demo_fillna():
    """
    用数值填充N/A
    """
    df = get_df()
    print(df)

    # 用单一值填充
    print(df.fillna(value='AAA'))

    # 用dict填充
    # 不同列使用不同默认值填充
    values = {'toy': 'AAA', 'born': 'BBB'}
    print(df.fillna(value=values))


def demo_fillna_method():
    """
    演示 fillna 不同method参数下的情况
    """
    df = pd.DataFrame([[np.nan, 2, np.nan, 0],
                       [3, 4, np.nan, 1],
                       [np.nan, np.nan, np.nan, 5],
                       [np.nan, 3, np.nan, 4]],
                      columns=list('ABCD'))
    print(df)
    #      A    B   C  D
    # 0  NaN  2.0 NaN  0
    # 1  3.0  4.0 NaN  1
    # 2  NaN  NaN NaN  5
    # 3  NaN  3.0 NaN  4

    # method = ffill
    print('fillna.method = padfill : ')      # 前一行填充后一行
    print(df.fillna(method='pad'))
    #      A    B    C    D
    # 0  NaN  2.0 NaN  0
    # 1  3.0  4.0 NaN  1
    # 2  3.0  4.0 NaN  5
    # 3  3.0  3.0 NaN  4
    print('fillna.method = ffill, axis=columns : ')
    print(df.fillna(method='ffill', axis='columns'))    # 前一列填充后一列
    #      A    B    C    D
    # 0  NaN  2.0  2.0  0.0
    # 1  3.0  4.0  4.0  1.0
    # 2  NaN  NaN  NaN  5.0
    # 3  NaN  3.0  3.0  4.0

    # method = bfill
    print('fillna.method = bfill : ')      # 后一行填充后一行
    print(df.fillna(method='bfill'))
    #  A    B   C  D
    # 0  3.0  2.0 NaN  0
    # 1  3.0  4.0 NaN  1
    # 2  NaN  3.0 NaN  5
    # 3  NaN  3.0 NaN  4


def demo_fillna_dict():
    """演示使用dict按列使用不同值替换
    """
    df = pd.DataFrame([[np.nan, 2, np.nan, 0],
                       [3, 4, np.nan, 1],
                       [np.nan, np.nan, np.nan, 5],
                       [np.nan, 3, np.nan, 4]],
                      columns=list('ABCD'))
    print(df)
    #      A    B   C  D
    # 0  NaN  2.0 NaN  0
    # 1  3.0  4.0 NaN  1
    # 2  NaN  NaN NaN  5
    # 3  NaN  3.0 NaN  4
    print(df.fillna({'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd'}))
    #    A  B  C  D
    # 0  a  2  c  0
    # 1  3  4  c  1
    # 2  a  b  c  5
    # 3  a  3  c  4


if __name__ == "__main__":
    demo_fillna_dict()
