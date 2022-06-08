#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   scheduler.py
@Time    :   2021/12/24 15:30:36
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   任务分发
'''
import datetime
# from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler


class Job:

    def __init__(self, name):
        self.name = name

    def execute(self):
        print("{t} | {n} job action!".format(n=self.name, t=datetime.datetime.now()))


def run():
    scheduler = BlockingScheduler()
    # scheduler = BackgroundScheduler()
    # 3秒执行一次
    scheduler.add_job(Job("Jack").execute, 'interval', seconds=3)  
    # 固定时间执行一次
    # scheduler.add_job(Job("Date").execute, 'date', run_date=datetime.date(2021, 12, 25))   # 指定时间执行
    # 每分钟的第5秒处罚：
    scheduler.add_job(Job("Five Seconds").execute, 'cron', second="5")

    scheduler.start()


if __name__ == "__main__":
    run()
