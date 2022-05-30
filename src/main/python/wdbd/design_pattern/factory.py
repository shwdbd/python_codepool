#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   factory.py
@Time    :   2021/12/27 14:48:45
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   工厂方法 示例

抽象产品：FincialDataSource
抽象产品工厂：DataSourceFactory

'''
from abc import ABCMeta, abstractmethod


# 抽象产品
class FincialDataSource(metaclass=ABCMeta):

    @abstractmethod
    def get_source(self):
        raise AttributeError("子类必须继承")


# 具体产品
class Tushare(FincialDataSource):

    def get_source(self):
        print("get tushare !")


class Baostock(FincialDataSource):

    def get_source(self):
        print("get baostock !")


# 抽象工厂
class DataSourceFactory(metaclass=ABCMeta):

    @abstractmethod
    def get_api(self):
        raise AttributeError("子类必须继承")


# 具体工厂
class TushareFactory(DataSourceFactory):

    def get_api(self):
        return Tushare()


class BaostockFactory(DataSourceFactory):

    def get_api(self):
        return Baostock()


if __name__ == "__main__":
    # tushare
    af = TushareFactory()
    api = af.get_api()
    api.get_source()
