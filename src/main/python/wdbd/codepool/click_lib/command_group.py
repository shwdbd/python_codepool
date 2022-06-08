#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   command_group.py
@Time    :   2020/02/20 19:45:43
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   命令组


'''
import click


@click.command()
def cmd1():
    click.echo("command 1")


@click.command()
def cmd2():
    click.echo("command 2")


@click.command()
def cmd3():
    click.echo("command 3")


@click.group()
def cli_group1():
    pass


cli_group1.add_command(cmd1)
cli_group1.add_command(cmd2)


@click.group()
def cli_group2():
    pass


cli_group2.add_command(cmd2)
cli_group2.add_command(cmd3)


if __name__ == "__main__":
    cli_group2()
