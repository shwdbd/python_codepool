#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   single_command.py
@Time    :   2021/03/09 15:22:15
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   单个简单Command示例
'''
import click


@click.command()
@click.option('--count', default=1, help='问候次数')
@click.option('--name', prompt='请输入您的姓名',
              help='问候人的姓名')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    # for x in range(count):
    #     click.echo('你好 %s!' % name)
    click.echo("count = {0}".format(count))
    click.echo("name = {0}".format(name))


if __name__ == '__main__':
    hello()
