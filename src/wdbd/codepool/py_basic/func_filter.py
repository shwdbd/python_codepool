#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   func_filter.py
@Time    :   2019/10/13 11:10:35
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   内置函数 filter 使用示例

filter(function, iterable)
function是判断True/False的函数，filter将注意判断iterable中值是否满足条件，返回检验值为True的list对象

'''

# here put the import lib

if __name__ == "__main__":
    data = [2, 4, 5, 8, 7]

    obj = filter(lambda x: x % 2 == 1, data)
    print(obj)  # 返回filter对象
    print(list(obj))    # [5, 7]
