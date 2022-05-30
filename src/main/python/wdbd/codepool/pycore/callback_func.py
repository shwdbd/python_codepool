#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   callback_func.py
@Time    :   2021/03/17 15:04:09
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   回调函数

控制台输出：
F1() jack
F2() mike
'''


def f1(name):
    print("F1()", name)


def f2(name):
    print("F2()", name)


def callback_func(name, callback_func):
    callback_func(name)


if __name__ == "__main__":
    # 回调函数
    callback_func("jack", f1)
    callback_func("mike", f2)
