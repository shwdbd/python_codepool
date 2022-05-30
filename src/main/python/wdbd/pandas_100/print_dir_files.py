#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   print_dir_files.py
@Time    :   2022/01/24 13:39:37
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   打印出 目录下的所有文件名
'''
import os


if __name__ == "__main__":
    dir_path = "C:/BILI/Python自动化办公--Pandas玩转Excel（全30集）"
    for f in os.listdir(dir_path):
        print(f)
