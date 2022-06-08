#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   builder.py
@Time    :   2021/12/27 16:33:23
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   建造器
'''
from abc import ABCMeta, abstractmethod


class Player:

    def __init__(self):
        self.head = ""
        self.body = ""

    def __str__(self) -> str:
        return "head={h}, body={b}".format(h=self.head, b=self.body)


# 抽象builder
class PlayerBuilder(metaclass=ABCMeta):

    def __init__(self):
        self.player = Player()

    @abstractmethod
    def build_body(self):
        pass

    @abstractmethod
    def build_head(self):
        pass


# 人类builder
class HumanBuilder(PlayerBuilder):

    def build_body(self):
        self.player.body = "人身"

    def build_head(self):
        self.player.head = "人头"


# 不死族builder
class UndeadBuilder(PlayerBuilder):

    def build_body(self):
        self.player.body = "鬼身"

    def build_head(self):
        self.player.head = "鬼头"


class PlayerDiector:
    # 规范构造的顺序

    def build_player(self, builder: PlayerBuilder):
        builder.build_body()
        builder.build_head()
        return builder.player


if __name__ == "__main__":
    # client
    builder = UndeadBuilder()
    director = PlayerDiector()
    p = director.build_player(builder)
    print(p)
    builder = HumanBuilder()
    p = director.build_player(builder)
    print(p)
