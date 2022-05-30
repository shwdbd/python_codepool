#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   type_hints.py
@Time    :   2020/08/05 10:48:10
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   类型标注示例

类型标注就是显示声明 变量 的数据类型。

自python3.5开始，PEP484为python引入了类型注解(type hints)
- 类型检查，防止运行时出现参数和返回值类型、变量类型不符合。
- 作为开发文档附加说明，方便使用者调用时传入和返回参数类型。
- 该模块加入后并不会影响程序的运行，不会报正式的错误，只有提醒pycharm目前支持typing检查，参数类型错误会黄色提示

'''


def add(x: int, y: int) -> int:
    return x+y


if __name__ == "__main__":
    print(add(2, 3))
    print(add("x", 2))  # 会报错
