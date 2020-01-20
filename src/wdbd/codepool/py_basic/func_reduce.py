#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   func_reduce.py
@Time    :   2019/10/13 11:00:44
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   内置函数 reduce 使用示例

reduce(function, iterable[, initializer])
函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：
用传给 reduce 中的函数 function（有两个参数）先对集合中的第 1、2 个元素进行操作，
得到的结果再与第三个数据用 function 函数运算，最后得到一个结果。

! python3 必须显式引用
！function参数必须有两个

'''
from functools import reduce


if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    data = ['a', 'b', 'c', 'd']

    obj = reduce(lambda x, y: x+y, data)
    print(obj)
