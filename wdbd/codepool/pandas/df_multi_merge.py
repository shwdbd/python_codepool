#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   df_multi_merge.py
@Time    :   2019/10/28 16:00:55
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   None
'''
import pandas as pd
from functools import reduce


def df_merge(x, y):
    return x.merge(y, on='id')


if __name__ == "__main__":
    data_A = {
        "id": ['600001', '600002', '600003'],
        "open": [12.9, 7.3, 6.2],   
    }
    df_A = pd.DataFrame(data_A)
    print(df_A)

    data_B = {
        "id": ['600001', '600002', '600003'],
        "item": ['TYPEA', 'TYPEB', 'TYPEC'],   
    }
    df_B = pd.DataFrame(data_B)
    print(df_B)

    data_C = {
        "id": ['600001', '600002', '600003'],
        "age": [500, 0, 300],   
    }
    df_C = pd.DataFrame(data_C)
    print(df_C)

    # df = df_A.merge(df_B, on='id')
    # print(df)

    df = reduce(df_merge, [df_A, df_B, df_C]  )
    print(df)

