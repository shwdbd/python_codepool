#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   df_null.py
@Time    :   2019/10/15 17:38:47
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   空值的处理

df.dropna 按行删除
df.isnull
df.fillna
df.

https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html#pandas.DataFrame.dropna


'''
import pandas as pd


def get_df():
    df = pd.DataFrame({"name": ['Alfred', 'Batman', 'Catwoman'],
                    "toy": [np.nan, 'Batmobile', 'Bullwhip'],
                    "born": [pd.NaT, pd.Timestamp("1940-04-25"),
                             pd.NaT]})
    return df




