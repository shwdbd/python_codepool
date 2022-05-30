#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   proxy.py
@Time    :   2022/01/04 21:44:02
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   代理模式

- 虚代理
- 保护代理

虚代理，用读取大文件举例
保护代理，加上权限设置功能

'''
from abc import ABCMeta, abstractmethod


class AbstractReader(metaclass=ABCMeta):

    @abstractmethod
    def read(self):
        """ 读文件 """
        pass

    @abstractmethod
    def write(self, new_context):
        """ 写文件 """
        pass


class FileReader(AbstractReader):

    def __init__(self):
        self.file = "大文件"    # 模拟读文件
        # 加载文件内容
        self.file_context = "x" * 100

    def read(self):
        """ 读文件 """
        return self.file_context

    def write(self, new_context):
        """ 写文件 """
        self.file_context = new_context


class FileProxy:
    """ 文件虚代理 """

    def __init__(self):
        self.f = None    # 初期不初始化

    def read(self):
        """ 读文件 """
        if self.f is None:
            self.f = FileReader()
        return self.f.read()

    def write(self, new_context):
        """ 写文件 """
        if self.f is None:
            self.f = FileReader()
        self.f.write(new_context)


def client():
    """ 客户端调用 """
    file_proxy = FileProxy()
    # 此处并没有读文件
    print("此处并没有真实读文件内容")
    print(file_proxy.read())


if __name__ == "__main__":
    client()
