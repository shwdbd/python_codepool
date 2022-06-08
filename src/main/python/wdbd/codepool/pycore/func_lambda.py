#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   func_lambda.py
@Time    :   2019/10/13 09:32:20
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   匿名函数 lambda 用法示例

1. demo_lambda  lambda使用示例
'''


def demo_lambda():
    sqr = lambda x: x**2
    print(sqr(2))


if __name__ == "__main__":
    demo_lambda()