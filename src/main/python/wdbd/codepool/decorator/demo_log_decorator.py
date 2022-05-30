#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_log_decorator.py
@Time    :   2020/01/20 13:30:45
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   使用装饰器函数的示范代码

基本概念：
- 函数内函数
- 返回值为函数

本实例的功能：
- 提供一个logit()装饰器，在函数运行前、后记录日志
- 装饰器带参数

关键点：
- 有名为logging_decorator的内部函数，其以func为参数
- 通过 func(*args, **kwargs) 调用原函数
- 装饰器函数最后返回 logging_decorator 这一函数

'''
import time
from functools import wraps


# 装饰器函数
def logit(log_file=None):

    def write_log(log_str):
        if log_file is None:
            print(log_str)
        else:
            now = time.asctime(time.localtime(time.time()))
            with open(log_file, mode='a', encoding='utf-8') as log_f:
                log_f.write('{0} {1} \n'.format(now, log_str))

    # 装饰器函数
    def logging_decorator(func):
        @wraps(func)
        def wrapped_func(*args, **kwargs):
            log_str = '[日志] {0} 函数开始运行'.format(func.__name__)
            write_log(log_str)

            func(*args, **kwargs)

            log_str = '[日志] {0} 函数完成'.format(func.__name__)
            write_log(log_str)

        return wrapped_func

    return logging_decorator


@logit(log_file='dd_log.log')
def hi(name='Jack'):
    print('Hello, {0}'.format(name))


if __name__ == "__main__":
    hi()
