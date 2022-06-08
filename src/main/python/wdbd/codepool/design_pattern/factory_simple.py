#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   factory_simple.py
@Time    :   2021/12/27 14:34:35
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   简单工厂

create_api，根据参数决定返回Tushare还是Baostock还是Tushare免费用户API

'''


class Tushare:
    """Tushare数据接口
    """

    def __init__(self, is_free=True):
        self.is_free = is_free

    def call(self):
        if self.is_free:
            print("Tushare free api")
        else:
            print("Tushare pro api")


class Baostock():
    """Baostock数据接口
    """

    def call(self):
        print("Baostock api")


class APIFactory:

    def get_api(self, name):
        if name == "Tushare":
            return Tushare()
        elif name == "TusharePro":
            return Tushare(is_free=False)
        elif name == "Baostock":
            return Baostock()
        else:
            raise TypeError("无法识别的API类型")


if __name__ == "__main__":
    af = APIFactory()
    api = af.get_api("TusharePro")
    api.call()
    api = af.get_api("Tushare")
    api.call()
