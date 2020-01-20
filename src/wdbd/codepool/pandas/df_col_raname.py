#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   df_col_raname.py
@Time    :   2019/10/15 17:38:30
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   df列改名

DOC:
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rename.html#pandas.DataFrame.rename

'''
import pandas as pd


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


def foo(label):
    """实验操作函数
    
    Arguments:
        label {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    """
    return label + "_new"


if __name__ == "__main__":
    df = get_df()
    print(df)

    # 直接改列名
    print(df.rename(columns={'code': 'id'}))

    # 用函数改列名
    print(df.rename(columns=foo))
