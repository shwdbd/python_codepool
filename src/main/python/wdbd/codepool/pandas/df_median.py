#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   df_median.py
@Time    :   2022/01/08 20:41:24
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   求中位数 示例
'''
import pandas as pd
import numpy as np


def get_df():
    """
    生成示例用DataFrame
    """
    data = {
        # 'date': ['20180101', '20180101', '20180102', '20190101'],
        # 'code': ['600016', '600020', '600016', '000001'],
        'price': [1.45, 6.12, 1.48, 2.45, 5.7, 1.2, 0.89],
        'price2': [2.45, 4.12, 1.48, 2.45, 5.7, 1.2, 0.89]
    }
    df = pd.DataFrame(data=data)
    # df.index = df['date']
    return df


def get_median_index(sr: pd.Series):
    """ 取得中位数的索引值 """
    if len(sr) % 2 > 0:
        return sr.loc[sr==sr.median()].index.values[0]
    else:
        sr = sr.copy()
        sr.sort_values(inplace=True)
        return sr[sr < sr.median()].index.values[-1], sr[sr > sr.median()].index.values[0]


if __name__ == "__main__":
    # df_median()

    df = pd.DataFrame(np.random.randn(7, 1), columns=list('A'))
    print(df.sort_values(by="A"))

    print(df["A"].median())
    print(get_median_index(df["A"]))
    print(df["A"].iloc[get_median_index(df["A"])])
