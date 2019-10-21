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

dropna:
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html#pandas.DataFrame.dropna
fillna:
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.fillna.html#pandas.DataFrame.fillna
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


if __name__ == "__main__":
    demo_fillna()
