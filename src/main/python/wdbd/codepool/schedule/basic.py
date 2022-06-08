#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   basic.py
@Time    :   2021/09/03 10:36:02
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   常见周期调用示例
'''
import schedule
import time
import datetime


def job():
    print("job()函数调用 ... {0} ".format(datetime.datetime.now()))


# 每十分钟执行任务
schedule.every(10).minutes.do(job)
# 每个小时执行任务
schedule.every().hour.do(job)
# 每天的10:30执行任务
schedule.every().day.at("10:30").do(job)
# 每个月执行任务
schedule.every().monday.do(job)
# 每个星期三的13:15分执行任务
schedule.every().wednesday.at("13:15").do(job)
# 每分钟的第17秒执行任务
schedule.every().minute.at(":17").do(job)


while True:
    schedule.run_pending()
    time.sleep(1)
