#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   get_char_from_terminal.py
@Time    :   2021/03/09 16:29:01
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   从终端收取用户输入
'''
import click

click.clear()
click.echo('Continue? [yn] ', nl=False)
c = click.getchar()
click.echo()    # 输出换行
if c == 'y':
    click.echo('We will go on')
elif c == 'n':
    click.echo('Abort!')
else:
    click.echo('Invalid input :(')
