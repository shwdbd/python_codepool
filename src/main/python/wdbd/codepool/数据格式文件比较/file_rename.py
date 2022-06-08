#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   file_rename.py
@Time    :   2021/12/07 14:29:52
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   文件批量改名
'''
import os


def show_list():
    # 显示名
    root_dir = "E:/000 陈丹青/"

    # print(os.listdir(root_dir))
    for filename in os.listdir(root_dir):
        print(filename)


def renames():
    # 批量改名
    root_dir = "E:\\000 电影\\"
    replace_str = "阳光电影www.ygdy8.com."
    to_str = ""

    # print(os.listdir(root_dir))
    for filename in os.listdir(root_dir):
        new_file_name = filename.replace(replace_str, to_str)
        old_path = root_dir + "\\" + filename
        new_path = root_dir + "\\" + new_file_name
        os.rename(old_path, new_path)
        print("{0} => {1}".format(filename, new_file_name))


if __name__ == "__main__":
    show_list()
