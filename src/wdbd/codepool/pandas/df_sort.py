#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   df_sort.py
@Time    :   2019/10/15 17:39:47
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   df排序

1. sort_by_columns      按指定列排序 sort_values, sort_index



'''
import pandas as pd
import numpy as np


def get_df():
    df = pd.DataFrame({
        'col1': ['A', 'A', 'B', np.nan, 'D', 'C'],
        'col2': [2, 1, 9, 8, 7, 4],
        'col3': [0, 1, 9, 4, 2, 3], })
    return df


def sort_by_columns():
    """
    df排序

    有两个函数：sort_by_values, sort_by_index

    https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_values.html#pandas.DataFrame.sort_values
    https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_index.html#pandas.DataFrame.sort_index

    """
    df = get_df()
    print(df)

    # 简单按列排序, np.NaN是最后
    print(df.sort_values(by='col1'))

    # 多列排序 ,col1升序，col2降序
    print(df.sort_values(by=['col1', 'col2'], ascending=[True, False]))

    # 按索引排序
    print(df.sort_index(ascending=False))


if __name__ == "__main__":
    sort_by_columns()
