#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_decorator_class.py
@Time    :   2020/01/20 14:07:45
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   装饰器类使用示范

关键点：
- 装饰器类 是通过__call__函数进行控制，其余同装饰器函数使用方式差不多
- 装饰器类可以继承


'''

# here put the import lib


import time
from functools import wraps


class Logit:

    def __init__(self, log_file=None):
        super().__init__()
        self.log_file = log_file

    def write_log(self, log_str):
        if self.log_file is None:
            print(log_str)
        else:
            now = time.asctime(time.localtime(time.time()))
            with open(self.log_file, mode='a', encoding='utf-8') as log_f:
                log_f.write('{0} {1} \n'.format(now, log_str))

    def __call__(self, func):
        @wraps(func)
        def wrapped_func(*args, **kwargs):
            log_str = '[日志] {0} 函数开始运行'.format(func.__name__)
            self.write_log(log_str)

            func(*args, **kwargs)

            log_str = '[日志] {0} 函数完成'.format(func.__name__)
            self.write_log(log_str)

        return wrapped_func


@Logit(log_file='xxxx.log')
def hi(name='Jack'):
    print('Hello, {0}'.format(name))


if __name__ == "__main__":
    hi('马汀')
