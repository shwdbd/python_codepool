#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   random.py
@Time    :   2019/10/15 22:26:40
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   随机函数

标准差随机数


'''
import numpy as np

# TODO 生成指定范围内float数列
# TODO 生成指定范围内int数列

def get_random_float():
    sampl = np.random.uniform(low=0.5, high=13.3, size=(5,))
    print(sampl)


if __name__ == "__main__":
    # print(np.random.rand(3,2))
    get_random_float()
