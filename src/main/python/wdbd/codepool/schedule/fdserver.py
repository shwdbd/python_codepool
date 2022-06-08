#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   fdserver.py
@Time    :   2021/09/03 16:43:18
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   使用schedule实现fdserver功能
'''


class BasicUnit:

    def download(self):
        print("Unit {n} download , {t}, {d}".format())


class FDServer:

    def __init__(self):
        self.unit_name_list = []

    def start(self):
        pass


if __name__ == "__main__":
    fdserver = FDServer()
    fdserver.start()
    # fdserver.shundown()

