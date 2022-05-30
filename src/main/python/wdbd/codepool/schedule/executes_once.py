#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   executes_once.py
@Time    :   2021/09/03 10:39:18
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   只调用一次的示例

输出：
Job executed! 2021-09-03 10:43:10.885978

'''
import schedule
import time
import datetime


def job_that_executes_once():
    # 此处编写的任务只会执行一次...
    print("Job executed! {0} ".format(datetime.datetime.now()))
    return schedule.CancelJob


# schedule.every().day.at('22:30').do(job_that_executes_once)
# 每分钟第10秒时候执行，只执行一次
schedule.every().minute.at(':10').do(job_that_executes_once)


while True:
    schedule.run_pending()
    time.sleep(1)
