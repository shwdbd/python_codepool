#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   np_random.py
@Time    :   2019/10/15 22:26:40
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   随机函数

numpy random 函数DOC：
https://docs.scipy.org/doc/numpy-1.15.0/reference/routines.random.html

1. demo_rand                产生随机数 rand, randn, randint，
2. demo_rand_int            产生随机整数
2. demo_seed                使用种子产生随机数
3. demo_choice              用choice函数

'''
import numpy as np


def demo_rand():
    """
    产生随机数
    """
    # rand函数：
    # https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.random.rand.html#numpy.random.rand
    # np.random.seed(10)
    array = np.random.rand(1, 2)
    print(type(array))  # numpy.ndarray
    print(array)

    # randn函数：返回标准分布的样本
    # https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.random.randn.html#numpy.random.randn
    array = np.random.randn(2, 2)
    print(type(array))  # numpy.ndarray
    print(array)


def demo_rand_int():
    """
    产生随机int
    """
    arr = np.random.randint(5, size=(1, 2))     # 产生2*2的，元素小于5的数组
    print(arr)  # [[3 0]]

    arr = np.random.randint(5, high=10, size=5)    # 产生5个大小在[5, 10)区间的数组
    print(arr)  # [7 6 8 8 8]


def demo_seed():
    """
    使用种子产生随机数

    使用确定的seed，可以使每次随机出来的数字都一样
    """
    np.random.seed(10)
    print(np.random.rand(5))

    np.random.seed(10)
    print(np.random.rand(5))


def demo_choice():
    """
    用choice函数

    文档：
    https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.random.choice.html#numpy.random.choice
    """
    mm = ['Java', 'C++', 'Python']
    arr = np.random.choice(mm, size=5)
    print(arr)  # ['C++' 'Python' 'Python' 'C++' 'Python']

    # 带分布律参数：
    mm = ['Java', 'C++', 'Python']
    arr = np.random.choice(mm, size=5, p=[0.9, 0.05, 0.05])
    print(arr)  # ['Java' 'Python' 'Java' 'Java' 'Java']


if __name__ == "__main__":
    demo_choice()
