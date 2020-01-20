#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   func_muti_args.py
@Time    :   2019/10/12 22:31:57
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   函数不定长参数 Usage

1. demo_args_simple             args简单使用
2. demo_args_and_normalargs     args和普通参数混合使用
3. demo_args_diff_type          args使用不同类型的参数
4. demo_kwargs_simple           kwargs简单使用

'''


def foo_args(*args):
    print(type(args))
    print(args)


def foo_args2(name, *args):
    print('Name = ' + str(name))
    print(type(args))
    for arg in args:
        print("{0} : {1}".format(arg, type(arg)))


def foo_kwargs(name, **kwargs):
    print('Name = ' + str(name))
    print(type(kwargs))
    print(kwargs)
    for arg in kwargs:
        print("{0} : {1} : {2}".format(arg, kwargs[arg], type(kwargs[arg])))


def demo_args_simple():
    """
    *args简单使用
    """
    foo_args(1, 2, 3)
    # <class 'tuple'>   其实就是一个tuple
    # (1,2,3)
    foo_args()
    # ()


def demo_args_and_normalargs():
    """
    args和普通参数混合使用
    """
    foo_args2('Jack', 'Mike')


def demo_args_diff_type():
    """[summary]
    """
    foo_args2('Jack', 'Mike', 20, 4.5)


def demo_kwargs_simple():
    """[summary]
    """
    foo_kwargs('Jack', a=1, b="abc", c=0.55)


if __name__ == "__main__":
    demo_kwargs_simple()
