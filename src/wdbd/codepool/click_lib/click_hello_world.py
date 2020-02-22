#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   click_hello_world.py
@Time    :   2020/02/20 19:23:12
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   第一个Click的例子

程序首先会提示您输入姓名，然后根据count参数决定输出N次

- 最简单的Hello World，有Name作为必输的参数
- 有option参数Count

帮助信息：
Usage: click_hello_world.py [OPTIONS]

  输出欢迎信息

Options:
  --name TEXT      The person to greet.
  --count INTEGER  欢迎的次数
  --help           Show this message and exit.


'''
import click


@click.command()
@click.option('--name', prompt='请输入您的姓名', help='The person to greet.')
@click.option('--count', default=1, help='欢迎的次数')
def hello(name, count=1):
    """输出欢迎信息
    """
    if not name:
        print('请输入姓名')
        return

    for i in range(count):
        print('Hello World, {0}'.format(name))


if __name__ == "__main__":
    hello()
