#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   df_basic.py
@Time    :   2019/10/15 17:09:53
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   DF的构建与基本属性

1. demo_construct               手工构建df
2. demo_construct_by_nparray    使用np.ndarray构建
3. demo_construct_by_nprandom   使用random.randn构建
4. demo_construct_by_dict       使用dict构建
5. demo_selection               .loc与.iloc的数据选择
6. demo_add_del_col             新增列 与 删除列

DataFrame构造函数doc：
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame

'''
import pandas as pd
import numpy as np


def demo_construct():
    """
    手工构建df
    """
    # TODO 待实现
    pass


def demo_construct_by_nparray():
    """
    使用np.ndarray构建
    """
    # TODO 待实现
    print('执行完毕！')


def demo_construct_by_nprandom():
    """
    使用random.randn构建
    """
    # TODO 待实现
    print(np.random.randn(5))
    print('执行完毕！')


def demo_construct_by_dict():
    """
    使用dict构建
    """
    dict_data = {
        "id": ['600001', '600002', '600003'],
        "open": [12.9, 7.3, 6.2],   # FIXME 此处要改成随机函数
    }
    df = pd.DataFrame(data=dict_data)
    df.index = df.id
    print(df)
    print('执行完毕！')


def demo_selection():
    """
    .loc与.iloc的数据选择

    .loc 按值切片，前闭后闭
    https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html#pandas.DataFrame.loc

    .iloc 按位置切片，前闭后开
    https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.iloc.html#pandas.DataFrame.iloc

    """
    dict_data = {
        "id": ['600001', '600002', '600003'],
        "open": [12.9, 7.3, 6.2],
    }
    df = pd.DataFrame(data=dict_data)
    df.index = df.id
    print(df)

    # 按index值切片
    try:
        print(df.loc[['600001', '600003']])     # 不连续索引
    except KeyError:
        print('index key 未找到！')

    # 按value值切片
    print(df['open'].iloc[2:])

    print('执行完毕！')


def demo_add_del_col():
    """
    新增列 与 删除列
    """
    dict_data = {
        "id": ['600001', '600002', '600003'],
        "open": [12.9, 7.3, 6.2],   # FIXME 此处要改成随机函数
    }
    df = pd.DataFrame(dict_data)
    print(df)
    # 新增一列
    df['NEW'] = ['a', 'b', 'c']
    print(df)
    # 新增重名的列（覆盖）
    df['NEW'] = ['a2', 'b2', 'c2']
    print(df)
    # 删除一列
    del(df['NEW'])
    print(df)
    # 删除不存在的列
    try:
        del(df['NONE'])
    except KeyError:
        print('NONE 列不存在！')
    else:
        print('其他错误！')
    print('执行完毕！')


if __name__ == "__main__":
    demo_construct_by_nprandom()
