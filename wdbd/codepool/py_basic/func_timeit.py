#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   func_timeit.py
@Time    :   2019/10/13 11:17:32
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   程序计时函数 timeit

语法：
timeit(函数名_字符串，运行环境_字符串，number=运行次数)

运行本模块中的函数：
t = timeit('func()', 'from __main__ import func', number=1000)

'''
from timeit import timeit, repeat


def foo():
    s = 0
    for i in range(1000):
        s += i
    # print(s)


if __name__ == "__main__":
    t = timeit('foo()', 'from __main__ import foo', number=1000*10)
    print(t)

    # 重复实验：
    t = repeat('foo()', 'from __main__ import foo', number=100, repeat=5)
    print(t)
