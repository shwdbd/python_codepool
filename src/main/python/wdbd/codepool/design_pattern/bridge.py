#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   bridge.py
@Time    :   2021/12/27 17:25:15
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   桥模式

shape = Line(color=Red())
shape.drow()

shape = Point(color=Blue())
shape.drow()

'''
from abc import ABCMeta, abstractmethod


# 抽象类
class Color(metaclass=ABCMeta):

    @abstractmethod
    def paint(self):
        pass


class Shape(metaclass=ABCMeta):

    def __init__(self, color: Color):
        self.color = color

    @abstractmethod
    def drow(self):
        pass


# 具体类
class Red(Color):

    def paint(self):
        return "红色"


class Blue(Color):

    def paint(self):
        return "蓝色"


class Line(Shape):

    name = "线"

    def drow(self):
        print("{color} {shape}".format(color=self.color.paint(), shape=self.name))


class Point(Shape):

    name = "点"

    def drow(self):
        print("{color} {shape}".format(color=self.color.paint(), shape=self.name))


if __name__ == "__main__":
    shape = Line(color=Red())
    shape.drow()

    shape = Point(color=Blue())
    shape.drow()
