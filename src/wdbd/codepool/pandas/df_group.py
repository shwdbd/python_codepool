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

DOC:



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


def groupby_and_order_and_max():
    """
    按多个字段groupby，然后分类进行排序并显示前几个数字

    示例，将下面的df，找出不同class中成绩前两名的记录
    df:
    name     sex       score    class
    Wang     Male      78       AAA
    Liu      Female    50       BBB
    Li       Male      48       AAA
    Mary     Female    84       AAA
    ...

    思路：
    1. 先按score排序；
    2. 按class进行groupby，然后用head(2)取前两行
    3. 最后按class排序

    """
    data = {
        'name': ['Wang', 'Liu', 'Li', 'Mary', 'Tom'],
        'sex': ['Male', 'Female', 'Male', 'Female', 'Male'],
        'score': [78, 50, 48, 84, 90],
        'class': ['AAA', 'BBB', 'AAA', 'AAA', 'BBB']
    }
    df = pd.DataFrame(data=data)
    # print(df)

    df.sort_values(by=['score'], inplace=True, ascending=[False])
    print(df)
    df2 = df.groupby(by='class').head(2).sort_values(by=['class'])
    print(df2)


def simple_groupby():
    """最简单的groupby示例
    """
    df = get_df()
    print(df)

    # 执行
    group_obj = df.groupby(by=['code'])
    print(type(group_obj))
    print(group_obj.mean())
    # code
    # 600016  1.465
    # 600020  6.120


if __name__ == "__main__":
    groupby_and_order_and_max()
