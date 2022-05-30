#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   py_cls_getattr.py
@Time    :   2021/02/24 20:16:40
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   None
'''


class MyClass:

    params = {
        "count": 1,
        "name": "MyName"
    }

    def __getattr__(self, attrname):
        if attrname in self.params.keys():
            return self.params[attrname]
        else:
            raise AttributeError(attrname)

    def __setattr__(self, attrname, value):
        if attrname in self.params.keys():
            self.params[attrname] = value
        else:
            raise AttributeError(attrname)


class Params:

    # params = {
    # }

    def __init__(self):
        self.params = {}

    def __setattr__(self, attrname, value):
        if attrname == 'params':
            self.__dict__['params'] = {}
        else:
            # print(self.__dict__)
            self.__dict__["params"][attrname] = value

    def __getattr__(self, attrname):
        if attrname in self.__dict__["params"]:
            return self.params[attrname]
        else:
            raise AttributeError(attrname)


if __name__ == "__main__":
    # my = MyClass()
    # print("读取属性:")
    # print("my.count = {0}".format(my.count))
    # print("my.name = {0}".format(my.name))
    # try:
    #     print(my.xxx)
    # except Exception:
    #     print("无效属性xxx")

    # print("赋值属性:")
    # my.count = 2
    # my.name = "新名"
    # print("my.count = {0}".format(my.count))
    # print("my.name = {0}".format(my.name))
    # try:
    #     my.xxx = 12345
    # except Exception:
    #     print("无效属性xxx")

    p = Params()
    # print(p.__dict__)
    p.abc = "123"
    print(p.abc)
