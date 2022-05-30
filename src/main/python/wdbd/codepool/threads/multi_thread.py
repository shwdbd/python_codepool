#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   multi_thread.py
@Time    :   2020/02/22 16:04:52
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   简单的多线程

开N个线程函数，输出std内容

'''
import _thread
import time


# 为线程定义一个函数
def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s: %s" % (threadName, time.ctime(time.time())))


def run_thread():
    # 创建两个线程
    try:
        _thread.start_new_thread(print_time, ("线程1 = ", 2, ))
        _thread.start_new_thread(print_time, ("线程2 = ", 4, ))
    except Exception as err:
        print("Error: 无法启动线程 " + str(err))

    # while 1:
    #     pass
    time.sleep(30)
    print('程序最终结束')


if __name__ == "__main__":
    run_thread()
