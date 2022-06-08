#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   array_ref.py
@Time    :   2019/10/13 21:36:34
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   ndarray切片引用性质示例，含copy函数

ndarray的切片等操作都是指针，如果需要使用复制则显式使用.copy函数

'''
import numpy as np


if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    na = np.array(data)
    b = na[3:]
    b[0] = 100
    print(list(b))  # [100, 5]
    print(list(na))  # [1 2 3 100 5]
    c = b.copy()
    c[0] = 500
    print(list(c))  # [500, 5]
    print(list(na))  # [1 2 3 100 5]
