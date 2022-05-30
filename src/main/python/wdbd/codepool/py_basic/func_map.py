#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   func_map.py
@Time    :   2019/10/13 09:39:27
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   map函数用法示例

map(function, iterable, ...)
iterable中每个元素都应用function

'''

if __name__ == "__main__":
    m = map(lambda x: x**2, [1, 2, 3, 4])
    print(list(m))
