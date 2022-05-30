#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   first_bar.py
@Time    :   2020/12/23 09:57:21
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   进度条实例
'''
from progress.bar import Bar
import time


def show_bar():
    # loading 10秒钟，然后结束
    action_list = ['A', 'B', 'C', 'D', 'E']
    bar = Bar('Processing', max=len(action_list))
    for action in action_list:
        time.sleep(1)
        bar.next()
    bar.finish()


if __name__ == "__main__":
    show_bar()
