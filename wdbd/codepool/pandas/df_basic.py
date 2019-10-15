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
    pass


def demo_construct_by_nprandom():
    """
    使用random.randn构建
    """
    # TODO 待实现
    pass


def demo_construct_by_dict():
    """
    使用dict构建
    """
    dict_data = {
        "id": ['600001', '600002', '600003'],
        "open": [12.9, 7.3, 6.2],   # FIXME 此处要改成随机函数
    }
    df = pd.DataFrame(data=dict_data)
    print(df)



    # TODO 待实现
    pass


def demo_selection():
    """
    .loc与.iloc的数据选择
    """
    # TODO 待实现
    pass


def demo_add_del_col():
    """
    新增列 与 删除列
    """
    # TODO 待实现
    pass


if __name__ == "__main__":
    demo_construct_by_dict()
