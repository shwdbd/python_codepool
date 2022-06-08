#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   init_p.py
@Time    :   2021/03/04 16:19:55
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   使用**kwargs参数透传
'''

class MyClass:

    params = {
        "count": 1,
        "name": "MyName"
    }

    def __init__(self, *args, **kwargs):
        super().__init__()

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


if __name__ == "__main__":
    my = MyClass(count=2, name="Tina", xxx="yyy")
    print("读取属性:")
    print("my.count = {0}".format(my.count))
    print("my.name = {0}".format(my.name))
