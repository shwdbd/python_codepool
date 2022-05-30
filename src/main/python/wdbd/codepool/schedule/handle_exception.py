#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   handle_exception.py
@Time    :   2021/09/03 16:32:55
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   异常处理示例
'''
import functools
import schedule
import time


# 异常捕获装饰器
# 错误则终止
def catch_exceptions(cancel_on_failure=False):
    def catch_exceptions_decorator(job_func):
        @functools.wraps(job_func)
        def wrapper(*args, **kwargs):
            try:
                return job_func(*args, **kwargs)
            except Exception as err:
                print(str(err))
                # import traceback
                # print(traceback.format_exc())
                if cancel_on_failure:
                    return schedule.CancelJob
        return wrapper
    return catch_exceptions_decorator


@catch_exceptions(cancel_on_failure=True)
def bad_task():
    # 肯定会抛出异常
    return 1 / 0


schedule.every(3).seconds.do(bad_task)

while True:
    schedule.run_pending()
    time.sleep(1)
