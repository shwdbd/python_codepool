#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   options_choice.py
@Time    :   2021/03/09 20:36:59
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   选择型Option参数

Option的type是click.Choice

>python.exe options_choice.py
性别 = None
>python.exe options_choice.py -s MALE
性别 = male
>python.exe options_choice.py -s xxx
Error: Invalid value for "-s" / "--sex": invalid choice: xxx. (choose from male, female)

'''
import click


@click.command()
@click.option("-s", "--sex", help="性别", type=click.Choice(['male', 'female'], case_sensitive=False))
def command_func(sex):
    click.echo("性别 = {0}".format(sex))


if __name__ == "__main__":
    command_func()
