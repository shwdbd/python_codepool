#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   ndarray.py
@Time    :   2019/10/13 18:46:33
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   ndarray 使用示例

1. demo_ndarray      用list建立ndarray，显示三大属性(dim, shape, dtype)

'''

import numpy as np


def demo_ndarray():
    """
    用list建立ndarray，显示三大属性(dim, shape, dtype)
    """
    list_data = list(range(10))

    na = np.array(list_data, dtype=int)    # 注意，使用的是 np.array
    print('Type is {0}'.format(type(na)))   # numpy.ndarray 对象
    print('Len = {0}'.format(len(na)))
    print('shape = {0}'.format(na.shape))
    print('ndim = {0}'.format(na.ndim))
    print('strides = {0}'.format(na.strides))
    print('size = {0}'.format(na.size))
    print('data = {0}'.format(na.data))
    print('itemsize = {0}'.format(na.itemsize))


if __name__ == "__main__":
    demo_ndarray()
