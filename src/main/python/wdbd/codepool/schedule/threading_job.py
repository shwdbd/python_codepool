#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   threading_job.py
@Time    :   2021/09/03 15:03:20
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   并行运行示例

输出：
[1] I'm running on thread <Thread(Thread-1, started 9588)>
[2] I'm running on thread <Thread(Thread-2, started 32504)>
[3] I'm running on thread <Thread(Thread-3, started 47836)>
[1] I'm running on thread <Thread(Thread-4, started 49468)>
[2] I'm running on thread <Thread(Thread-5, started 38944)>
[3] I'm running on thread <Thread(Thread-6, started 5048)>

'''
import threading
import time
import schedule


def job1():
    print("[1] I'm running on thread %s" % threading.current_thread())


def job2():
    print("[2] I'm running on thread %s" % threading.current_thread())


def job3():
    print("[3] I'm running on thread %s" % threading.current_thread())


def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()


schedule.every(3).seconds.do(run_threaded, job1)
schedule.every(3).seconds.do(run_threaded, job2)
schedule.every(3).seconds.do(run_threaded, job3)


while True:
    schedule.run_pending()
    time.sleep(1)
