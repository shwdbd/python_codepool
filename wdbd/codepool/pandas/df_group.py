#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   df_group.py
@Time    :   2019/10/15 17:40:01
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   df的group

类似于SQL中group by的操作。使用df.group(...)后生成一个Group对象，然后再进行sum等操作

DOC:
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html#pandas.DataFrame.groupby

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


if __name__ == "__main__":
    df = get_df()
    print(df)

    #
    group_obj = df.groupby(by=['code'])
    print(type(group_obj))
    print(group_obj.mean())
    # code
    # 600016  1.465
    # 600020  6.120
