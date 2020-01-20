#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   df_apply_func.py
@Time    :   2019/10/15 17:39:01
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   apply函数

DOC:
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.apply.html#pandas.DataFrame.apply
'''
import pandas as pd


def demo_df_apply():
    df = pd.DataFrame([[4, 9]] * 3, columns=['A', 'B'])
    print(df)

    print(df.apply(lambda x: x-1))


if __name__ == "__main__":
    demo_df_apply()
