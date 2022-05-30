#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   factory_abstract.py
@Time    :   2021/12/27 15:09:15
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   抽象工厂示例

产品系列：IActor
- Head
- Body（必须先组件）
- Arm
- Leg

具体产品：Human, Oxman(牛头人)

'''
from abc import ABCMeta, abstractmethod


# 抽象产品接口
class IActor(metaclass=ABCMeta):

    @abstractmethod
    def say(self):
        raise AttributeError("子类必须继承")

    def __str__(self) -> str:
        return "[body={b}] header={h}".format(b=self.body, h=self.header)


class Header:

    def __init__(self, name):
        self.name = name


class Body:

    def __init__(self, name):
        self.name = name


# 具体产品
class Human(IActor):

    def __init__(self, header, body):
        self.body = body
        # self.


# 抽象工厂
class IActorFactory(metaclass=ABCMeta):

    @abstractmethod
    def make_body(self):
        raise AttributeError("子类必须继承")

    @abstractmethod
    def make_head(self):
        raise AttributeError("子类必须继承")
