#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   spinners.py
@Time    :   2020/12/23 14:38:19
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   Spinners 实例
'''
from progress.spinner import Spinner
import time


def spinners_show():
    # loading 10秒钟，然后结束

    spinner = Spinner('Loading ')
    state = "START"
    idx = 0
    while state != 'FINISHED':
        # Do some work
        time.sleep(1)

        if idx == 10:
            state = "FINISHED"
        idx += 1
        spinner.next()
    spinner.finish()


if __name__ == "__main__":
    spinners_show()
