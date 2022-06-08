#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   当前路径.py
@Time    :   2021/05/12 10:01:55
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   打印当前系统的路径
'''
import os
import sys


if __name__ == "__main__":
    # 当前执行python代码文件夹路径：
    modpath = os.path.dirname(os.path.abspath(sys.argv[0]))
    print(modpath)
    # 当前python文件路径
    print(os.path.abspath(sys.argv[0]))

    # 当前项目根目录：
    project_name = "python_codepool"
    curPath = os.path.abspath(os.path.dirname(__file__))
    rootPath = curPath[:curPath.find(
        project_name + "\\") + len(project_name + "\\")]
    print(rootPath)
