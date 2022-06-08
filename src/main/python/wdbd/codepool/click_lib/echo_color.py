#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   echo_color.py
@Time    :   2021/03/09 15:27:57
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   输出不同颜色的字体

两种控制字体和颜色的方法：click.Sytle 和 click.secho

本示例中使用两种方法，显示不同的字体、字色和背景

'''
import click


if __name__ == '__main__':
    click.echo("标准字体")
    # 使用style
    click.echo(click.style('绿色文字', fg='green'))
    # 使用secho
    click.secho("红字", fg="red")
    click.secho("红字黄底", fg="red", bg='yellow')
    # click.secho("红字白底加粗", fg="red", bg='white', bold=True, blink=True)
