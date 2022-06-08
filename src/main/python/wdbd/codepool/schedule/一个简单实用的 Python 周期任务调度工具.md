# 一个简单实用的 Python 周期任务调度工具

参考文档：<https://zhuanlan.zhihu.com/p/403576859>

官方网站：<https://github.com/627376948/schedule>

文档网站：<https://schedule.readthedocs.io/en/stable/>

? 用这个能做什么操作？

- 仿windows的定时任务？
- 用schedule重现FD的任务调度

## 安装和HelloWorld

安装：

```shell
pip install schedule
```

参考文档：<https://schedule.readthedocs.io/en/stable/installation.html>

第一个示例：(hello.py)

```python
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
```

## 常用任务调度方式

schedule支持从秒到月级别的计划调度，下面是示例(完整代码见basic.py)

```python
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
```

## 基本使用

本节讨论了schedule的基本常见使用方式

### 1. 只调用一次

某个任务只想调用一次，可以这样：(完整代码：executes_once.py)

```python
def job_that_executes_once():
    # 此处编写的任务只会执行一次...
    print("Job executed! {0} ".format(datetime.datetime.now()))
    return schedule.CancelJob

# 每分钟第10秒时候执行，只执行一次
schedule.every().minute.at(':10').do(job_that_executes_once)

# 输出：
# Job executed! 2021-09-03 10:43:10.885978
```

### 2. 参数传递

被调用的函数可以接收参数传入，但使用的是kwag样式的参数传入方式，（完整代码见parms.py）

```python
def hello(name: str):
    print("Hello {n} ... {t} ".format(n=name, t=datetime.datetime.now()))

# 每过3秒执行一次
schedule.every(3).seconds.do(hello, name="张三")
schedule.every(1).seconds.do(hello, name="李四")
```

### 3. 获取目前所有的作业（JOB）

通过schedule.get_jobs()可以访问全部的任务，并获得一下信息：

- 调度时间
- 上次、下次运行时间

下面是示例代码，完整代码见show_all_jobs.py

```python
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

# 输出：
# [Every 10 minutes do job() (last run: [never], next run: 2021-09-03 11:29:03), Every 2 seconds do job() (last run: [never], next run: 2021-09-03 11:19:05)]
# [Every 10 minutes do job() (last run: [never], next run: 2021-09-03 11:29:03), Every 2 seconds do job() (last run: [never], next run: 2021-09-03 11:19:05)]
# job()函数调用 ... 2021-09-03 11:19:05.186024
# [Every 10 minutes do job() (last run: [never], next run: 2021-09-03 11:29:03), Every 2 seconds do job() (last run: 2021-09-03 11:19:05, next run: 2021-09-03 11:19:07)]
# [Every 10 minutes do job() (last run: [never], next run: 2021-09-03 11:29:03), Every 2 seconds do job() (last run: 2021-09-03 11:19:05, next run: 2021-09-03 11:19:07)]
# job()函数调用 ... 2021-09-03 11:19:07.194646

```

### 4. 为任务打标签

任务可以设置多个标签，以便于查询和批量操作。下面案例中就标签设置、查询、批量取消进行示例。完整代码见

```python
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
```

### 5. 设定任务截止时间

截止日期时间之后，该作业将无法运行。完整示例代码见deadline.py

```python
# 每过2秒执行一次
schedule.every(2).seconds.until("14:20:20").do(job)
```

### 6. 强制运行任务

可以强制执行，详细代码见run_by_force.py

```python
def job_t1():
    print("T1()函数调用 ... {0} ".format(datetime.datetime.now()))


def job_t2():
    print("T2()函数调用 ... {0} ".format(datetime.datetime.now()))


# 分为两组
schedule.every(2).seconds.do(job_t1).tag("组A", "组C")
schedule.every(2).seconds.do(job_t2).tag("组B", "组C")

# 全部任务
schedule.run_all()  # 强制运行一次

# 立即运行所有作业，每次作业间隔10秒
print("wait")
schedule.run_all(delay_seconds=10)
```

## 高级场景

### 1. 装饰器

### 2. 并行运行

支持多线程并行运行，示例完整代码：threading_job.py

```python
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
```

### 3. 日志记录

这里日志指schedule的日志系统，通过配置可以控制schedule的日志输出，方便调试程序。

### 4. 异常处理

**Schedule不会自动捕捉异常，它遇到异常会直接抛出。**这会导致一个严重的问题：后续所有的作业都会被中断执行，因此我们需要捕捉到这些异常。

你可以手动捕捉，但是某些你预料不到的情况需要程序进行自动捕获，加一个装饰器就能做到了：

完整示例代码：handle_exception.py

```python
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
```

## FDserver的实现

### 需求

1. Unit指定时间执行，每日
2. Unit每日只成功执行一次
3. 多线程执行，一个Unit只开一个线程


### 代码结构

## 附录：代码清单

| 源文件 | 说明 |
| -- | -- |
| hello.py | 最简单的任务调度示例 |
| basic.py | 常见周期调用示例 |
| executes_once.py | 只调用一次的示例 |
| parms.py | 参数传入示例 |
| show_all_jobs.py | 回显当前运行全部任务示例 |
| cancel_all_jobs.py | 取消所有任务示例 |
| tags.py | 标签任务示例 |
| deadline.py | 任务截止时间示例 |
| run_by_force.py | 强制运行任务示例 |
| threading_job.py | 并行运行示例 |
| handle_exception.py | 异常处理示例 |
