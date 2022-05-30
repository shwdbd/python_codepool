#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   run_by_force.py
@Time    :   2021/09/03 14:23:36
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   强制运行任务示例
'''
import datetime
import schedule


def job_t1():
    print("T1()函数调用 ... {0} ".format(datetime.datetime.now()))


def job_t2():
    print("T2()函数调用 ... {0} ".format(datetime.datetime.now()))


# 分为两组
schedule.every(2).seconds.do(job_t1).tag("组A", "组C")
schedule.every(2).seconds.do(job_t2).tag("组B", "组C")

# 全部任务
schedule.run_all()  # 强制运行一次

# 立即运行所有作业，每次作业间隔10秒
print("wait")
schedule.run_all(delay_seconds=10)
