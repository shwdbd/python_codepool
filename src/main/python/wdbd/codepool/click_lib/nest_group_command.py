#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   nest_group_command.py
@Time    :   2021/06/24 13:33:37
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   嵌套命令

目标要实现两级的command：

command_group.py g1 cmd1

回显：
> group 1, command 1

'''
import click


@click.group()
def main():
    pass


@main.group(name="g1")
def cli_group_1():
    pass


@main.group(name="g2")
def cli_group_2():
    pass


@cli_group_1.command(name="cmd1")
def cmd_g1_1():
    click.echo("group 1, command 1")


@cli_group_2.command(name="cmd2")
def cmd_g2_2():
    click.echo("group 2, command 2")


if __name__ == '__main__':
    main()
