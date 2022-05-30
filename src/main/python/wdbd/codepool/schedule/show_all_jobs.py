#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   show_all_jobs.py
@Time    :   2021/09/03 11:17:09
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   回显当前运行全部任务示例

输出：
[Every 10 minutes do job() (last run: [never], next run: 2021-09-03 11:29:03),
 Every 2 seconds do job() (last run: [never], next run: 2021-09-03 11:19:05)]
[Every 10 minutes do job() (last run: [never], next run: 2021-09-03 11:29:03),
 Every 2 seconds do job() (last run: [never], next run: 2021-09-03 11:19:05)]
job()函数调用 ... 2021-09-03 11:19:05.186024
[Every 10 minutes do job() (last run: [never], next run: 2021-09-03 11:29:03),
 Every 2 seconds do job() (last run: 2021-09-03 11:19:05, next run: 2021-09-
  11:19:07)]
[Every 10 minutes do job() (last run: [never], next run: 2021-09-03 11:29:03),
 Every 2 seconds do job() (last run: 2021-09-03 11:19:05, next run: 2021-09-03
  11:19:07)]
job()函数调用 ... 2021-09-03 11:19:07.194646

'''
import datetime
import schedule
import time


def job():
    print("job()函数调用 ... {0} ".format(datetime.datetime.now()))


# 安排两个调度
schedule.every(10).minutes.do(job)
schedule.every(2).seconds.do(job)

# 发布后的周期任务需要用run_pending 函数来检测是否执行
# 因此需要一个While 循环不断地轮询这个函数
while True:
    schedule.run_pending()
    time.sleep(1)
    all_jobs = schedule.get_jobs()
    print(all_jobs)
