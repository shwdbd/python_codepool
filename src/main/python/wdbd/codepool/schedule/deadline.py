#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   deadline.py
@Time    :   2021/09/03 14:01:23
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   任务截止时间示例
'''
import datetime
import schedule
import time


def job():
    print("job()函数调用 ... {0} ".format(datetime.datetime.now()))


# 每过2秒执行一次
schedule.every(2).seconds.until("14:20:20").do(job)
# 输出：
# job()函数调用 ... 2021-09-03 14:20:13.212451
# job()函数调用 ... 2021-09-03 14:20:15.232049
# job()函数调用 ... 2021-09-03 14:20:17.255637
# job()函数调用 ... 2021-09-03 14:20:19.281764

# 发布后的周期任务需要用run_pending 函数来检测是否执行
# 因此需要一个While 循环不断地轮询这个函数
while True:
    schedule.run_pending()
    time.sleep(1)

print("End")    # 不会运行到
