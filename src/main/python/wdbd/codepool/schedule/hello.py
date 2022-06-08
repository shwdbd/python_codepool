#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   hello.py
@Time    :   2021/09/03 10:14:24
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   最简单的任务调度示例

实现：每过5秒，调用一次job函数

输出：
job()函数调用 ... 2021-09-03 10:31:02.330010
job()函数调用 ... 2021-09-03 10:31:04.344174
job()函数调用 ... 2021-09-03 10:31:06.360144

'''
import datetime
import schedule
import time


def job():
    print("job()函数调用 ... {0} ".format(datetime.datetime.now()))


# 每过2秒执行一次
# schedule.every(10).minutes.do(job)
schedule.every(2).seconds.do(job)

# 发布后的周期任务需要用run_pending 函数来检测是否执行
# 因此需要一个While 循环不断地轮询这个函数
while True:
    schedule.run_pending()
    time.sleep(1)
