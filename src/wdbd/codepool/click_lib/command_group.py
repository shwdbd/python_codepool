#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   command_group.py
@Time    :   2020/02/20 19:45:43
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   Click Command Group 代码示例

有多个命令需要执行

'''
import click


@click.command()
@click.option('--name', prompt='请输入您的姓名', help='The person to greet.')
def hello(name):
    """输出欢迎信息
    """
    print('Hello World'.format(name))


@click.command()
@click.option('--count', default=1, help='欢迎的次数')
def bye(count=1):
    """输出再见信息
    """
    for i in range(count):
        print('Bye')


@click.group()
def cli():
    pass


cli.add_command(hello)
cli.add_command(bye)


if __name__ == "__main__":
    cli()
