#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   array_select.py
@Time    :   2019/10/13 21:42:44
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   nDarray 索引与切片 示例代码

1. demo_get_row_rol         取得第1行，第一列
2. demo_sum_by_row          行列操作（sum第一行，sum所有行）
3. demo_by_course           条件索引
4. demo_np_where            np.where 函数
5. demo_np_sign             np.sign 函数
6. demo_np_any_all          np.any和np.all函数

'''
import numpy as np


data = np.array(
    [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10]
    ]
)


def demo_get_row_rol():
    """
    取得第1行，第一列
    """
    print(data)
    print(data[0])  # 第一行 [1 2 3 4 5]
    print(data[:, 0])  # 第一行 [1, 6]


def demo_sum_by_row():
    """
    行列操作（sum第一行，sum所有行）
    """
    print(data[0].sum())    # sum第一行, 15
    print(data.sum())       # sum所有，55


def demo_by_course():
    """
    条件索引
    """
    # 取得偶数
    print(data[data % 2 == 0])  # [ 2  4  6  8 10]

    # 取得偶数且大于5的数
    # 每个条件都要用()
    print(data[(data % 2 == 0) & (data > 5)])   # [6  8 10]


def demo_np_where():
    """
    np.where 函数
    """
    # 取得偶数
    print(np.where(data % 2 == 0, 1, 0))
    # [[0 1 0 1 0]
    #  [1 0 1 0 1]]

    # 取得偶数或大于5的数
    print(np.where((data % 2 == 0) | (data < 5), 'yes', 'no'))
    # [['yes' 'yes' 'yes' 'yes' 'no']
    # ['yes' 'no' 'yes' 'no' 'yes']]


def demo_np_sign():
    """
    np.sign 函数

    取得字符正负号的函数，正数返回1, 负数返回-1， 零返回0

    官方文档：
    https://docs.scipy.org/doc/numpy/reference/generated/numpy.sign.html

    """
    dataArr = [0, 12, -6]
    data = np.array(dataArr)
    print(np.sign(data))    # [ 0  1 -1]


def demo_np_any_all():
    """
    np.any和np.all函数
    """
    data_a = np.array([1, 2, 3])
    data_b = data_a.copy()
    data_b[2] = 4

    print((data_a == data_b).all()) # False
    print((data_a == data_b).any()) # True


if __name__ == "__main__":
    demo_np_any_all()
