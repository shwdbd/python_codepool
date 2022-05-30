#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   parms.py
@Time    :   2021/09/03 11:03:54
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   参数传入示例

输出：
Hello 李四 ... 2021-09-03 11:14:55.065562
Hello 李四 ... 2021-09-03 11:14:56.071837
Hello 张三 ... 2021-09-03 11:14:57.074578
Hello 李四 ... 2021-09-03 11:14:57.074578
Hello 李四 ... 2021-09-03 11:14:58.075487
Hello 李四 ... 2021-09-03 11:14:59.075812
'''
import datetime
import schedule
import time


def hello(name: str):
    print("Hello {n} ... {t} ".format(n=name, t=datetime.datetime.now()))


# 每过3秒执行一次
schedule.every(3).seconds.do(hello, name="张三")
schedule.every(1).seconds.do(hello, name="李四")

# 发布后的周期任务需要用run_pending 函数来检测是否执行
# 因此需要一个While 循环不断地轮询这个函数
while True:
    schedule.run_pending()
    time.sleep(1)
