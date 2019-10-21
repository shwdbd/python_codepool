#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   df_daterange_func.py
@Time    :   2019/10/15 17:39:30
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   pd.date_range示例

date_range是pd的全局函数

DOC:
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.date_range.html#pandas.date_range


'''
import pandas as pd


if __name__ == "__main__":
    # 生成日期区间，前闭后闭：
    print(pd.date_range(start='1/1/2018', end='1/08/2018'))
    # DatetimeIndex(['2018-01-01', '2018-01-02', '2018-01-03', '2018-01-04',
    #           '2018-01-05', '2018-01-06', '2018-01-07', '2018-01-08'],
    #          dtype='datetime64[ns]', freq='D')

    print(pd.date_range(start='1/1/2018', end='1/08/2018', periods=3))  # 每隔3天
