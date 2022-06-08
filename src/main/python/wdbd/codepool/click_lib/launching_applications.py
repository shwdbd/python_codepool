#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   launching_applications.py
@Time    :   2021/03/09 16:45:08
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   启动应用程序
'''
import click

# 打开网页
# click.launch("https://click.palletsprojects.com/")
# 打开本地应用程序
click.launch("notepad.exe")
# 打开特定目录
click.launch("c:/temp", locate=True)
