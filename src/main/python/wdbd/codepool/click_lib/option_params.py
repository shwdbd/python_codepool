#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   option_params.py
@Time    :   2021/03/09 20:20:25
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   Option常规参数示例

常规参数包括：STR,INT,FLOAT,BOOL类型

Option有type参数指定类型，可通过click.XXX指定类型或直接python类型指定

'''
import click


@click.command()
@click.option("-s", "--str-p", help="字符串参数", default="Jack", type=str)
@click.option("-s2", "--str-p2", help="字符串2参数", default="周三", type=click.STRING)
@click.option("-i", "--int-p", help="字符串参数", default=10, type=click.INT)
@click.option("-f", "--float-p", help="字符串参数", default=10.00, type=click.FLOAT)
@click.option("-b", "--bool-p", help="字符串参数", default=True, type=click.BOOL)
@click.option("-ff", "--file-p", help="文件参数", type=click.File(mode='r', ))
def command_func(str_p, str_p2, int_p, float_p, bool_p, file_p):
    click.echo("字符串参数 = {0}".format(str_p))
    click.echo("字符串参数2 = {0}".format(str_p2))
    click.echo("INT参数 = {0}".format(int_p))
    click.echo("FLOAT参数 = {0}".format(float_p))
    click.echo("BOOL参数 = {0}".format(bool_p))


if __name__ == "__main__":
    command_func()
