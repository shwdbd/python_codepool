#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   SimpleMock.py
@Time    :   2021/12/24 10:21:28
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   简单Mock模拟
'''
from unittest.mock import Mock
from unittest.mock import patch
import wdbd.pymock.foo as foo


def first_mock():
    """ 直接使用Mock对象进行模拟 """
    m = Mock()      # m是一个Mock出的类
    # 简单类模拟
    m.return_value = 100
    print(m())      # 100

    # 类函数模拟
    m = Mock()
    m.foo.return_value = 123
    print(m.foo())    # 123

    # 类属性模拟
    m = Mock()
    m.configure_mock(name='Jack')
    print(m.name)   # Jack


def mock_side_effect():
    # 试验side_effect

    # 优先级高于return_value
    m = Mock(return_value=100)
    m.side_effect = "abc"
    print(m())      # a，注意此处认为字符串是一个列表
    m.side_effect = {"abc"}
    print(m())      # abc

    # 返回列表，逐一运行
    m = Mock(side_effect=["Jack", 123])
    print(m())
    print(m())
    try:
        print(m())
    except Exception:
        print("模拟停止")

    # 返回异常
    m = Mock(side_effect=KeyError("foo"))
    try:
        print(m())
    except KeyError:
        print("获得异常，KeyError")


# --------------------------------------------------

def mock_os_getcwd():
    with patch("wdbd.pymock.foo.os") as mock_os:
        mock_os.getcwd.return_value = "xxxx/yyyy"
        foo.foo_getcwd()


@ patch("wdbd.pymock.foo.os")
def mock_os_getcwd_tag(mock_os):
    mock_os.getcwd.return_value = "1111/2222"
    foo.foo_getcwd()


if __name__ == "__main__":
    # first_mock()
    # mock_side_effect()

    foo.foo_getcwd()    # C:\gitee\shwdbd\python_codepool
    mock_os_getcwd()    # xxxx/yyyy
    mock_os_getcwd_tag()    # 1111/2222
