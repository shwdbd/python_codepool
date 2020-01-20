#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   for_baisc.py
@Time    :   2019/10/11 10:04:14
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   For循环用法示例
'''
import numpy as np


def for_range_usage():
    """
    for x in range()的用法
    """
    # 最简单，无步幅
    for i in range(1, 11):
        print(i)
    print('继续运行 ... ')

    # 指定步幅
    for i in range(1, 11, 3):
        print(i)
    print('继续运行 ... ')

    # 使用 numpy ，指定小数步幅
    for i in np.arange(0, 1, 0.3):
        print(i)
    print('继续运行 ... ')


def for_range_in_vender():
    """
    使用for...range在list，dict等容器中的用法    
    """
    lst_int = [1, 2, 3, 4, 5]
    for i in lst_int[3:]:
        print(i)
    print('继续运行 ... ')

    dict_employee = {
        "name": 'Jack Wang',
        "age": 20
    }
    for i in dict_employee.values():
        print(i)
    print('继续运行 ... ')
    for i, j in dict_employee.items():
        print(i, j)
    print('继续运行 ... ')


if __name__ == "__main__":
    for_range_in_vender()
