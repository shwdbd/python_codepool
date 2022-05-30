#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   tags.py
@Time    :   2021/09/03 13:35:55
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   标签任务示例

- 设置标签
- 按标签查询
- 按标签取消


'''
import datetime
import schedule
import time


def job_t1():
    print("T1()函数调用 ... {0} ".format(datetime.datetime.now()))


def job_t2():
    print("T2()函数调用 ... {0} ".format(datetime.datetime.now()))


# 每过2秒执行一次
schedule.every(2).seconds.do(job_t1).tag("组A", "组C")
schedule.every(2).seconds.do(job_t2).tag("组B", "组C")

# 按Tag过滤
print(schedule.get_jobs("组C"))
# [Every 2 seconds do job_t1() (last run: [never], next run: 2021-09-03 13:41:07),
#  Every 2 seconds do job_t2() (last run: [never], next run: 2021-09-03 13:41:07)] 

# 发布后的周期任务需要用run_pending 函数来检测是否执行
# 因此需要一个While 循环不断地轮询这个函数
count = 3
while count > 0:
    schedule.run_pending()
    time.sleep(5)
    count = count - 1
    print("next")

# 停一个组
schedule.clear("组A")
print(schedule.get_jobs())

# 全部停掉
schedule.clear()
print(schedule.get_jobs())
