#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   waiting_for_press.py
@Time    :   2021/03/09 16:31:56
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   等待用户输入任何键

err – if set to message goes to stderr instead of stdout, the same as with echo.

'''
import click

click.pause("请输入任何键", err=True)
