#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   option_default.py
@Time    :   2021/03/09 17:14:42
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   Option参数default值示例

示例：
>python.exe option_default.py -n Mike
Name is Mike
>python.exe option_default.py
Name is Jack
>python.exe option_default.py --help
Usage: option_default.py [OPTIONS]

Options:
  -n, --name TEXT  姓名  [default: Jack]
  --help           Show this message and exit.

--------------------------
Option default参数说明
- default 参数默认值
- show_default 是否在帮助中显示默认值

'''
import click


@click.command()
@click.option("-n", "--name", help="姓名", default="Jack", show_default=True)
def cmd_str(name):
    click.echo("Name is {0}".format(name))


if __name__ == "__main__":
    cmd_str()
