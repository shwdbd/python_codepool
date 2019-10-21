#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   df_selection.py
@Time    :   2019/10/15 17:37:50
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   DF的条件选择

1. select_by_loc        通过标签选择 .loc[ ['index1':'index2'] , ['colA']  ]    前闭后闭
2. select_by_iloc       通过位置选择 .iloc   前闭后开
   select_by_ix         ix 混合索引 pd 0.20后废弃
3. select_by_at_iat     at和iat索引
4. select_by_query      query 选择

'''
import pandas as pd
import numpy as np


def get_df():
    """
    生成示例用DataFrame
    """
    data = {
        'date': ['20180101', '20180101', '20180102'],
        'code': ['600016', '600020', '600016'],
        'price': [1.45, 6.12, 1.48]
    }
    df = pd.DataFrame(data=data)
    df.index = df['date']
    return df


def select_by_loc():
    """
    使用标签选择的代码用例，用index的选择

    DOC:
    https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html#pandas.DataFrame.loc
    """
    df = get_df()
    print(df)

    print(df.loc['20180101'])   # 单一选择
    print(df.loc[['20180101', '20180102']])     # 多选择
    print(df.loc['20180101': '20180102'])   # 区域选择，前闭后闭
    print(df.loc['A': 'X'])   # Empty DataFrame

    print('{0} 执行完毕！ {0}'.format('='*10))


def select_by_iloc():
    """
    通过位置选择 .iloc   前闭后开

    DOC:
    https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.iloc.html#pandas.DataFrame.iloc
    """
    df = get_df()
    print(df)

    print(df.iloc[1])   # pd.Series 第2行数据
    print(df.iloc[1:])  # 区域，前闭后开

    print('{0} 执行完毕！ {0}'.format('='*10))


def select_by_ix():
    """
    ix 混合索引

    pd 0.20.0后被废弃

    """
    pass


def select_by_at_iat():
    """
    at和iat索引，返回1个值

    DOC:
    https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.at.html#pandas.DataFrame.at
    https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.iat.html#pandas.DataFrame.iat
    """
    df = get_df()
    print(df)

    # at，按标签纸和列名
    print(df.at['20180102', 'code'])    # 600016
    try:
        print(df.at['20180199', 'code'])
    except Exception as ee:
        print(str(ee))  # KeyError: '20180199'

    # iat
    print(df.iat[1, 2])     # 第2行，第3列


def select_by_query():
    """
    query 选择

    DOC:
    https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.query.html#pandas.DataFrame.query
    """
    df = get_df()
    print(df)

    print(df.query("code=='600016' & price<1.46"))   # 条件选择


if __name__ == "__main__":
    select_by_query()
