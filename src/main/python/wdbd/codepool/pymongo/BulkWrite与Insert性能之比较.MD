# BulkWrite与Insert性能之比较

## 1. 概述

由于写数据库操作最耗费时间的是数据库访问网路通讯，所以批量写操作（bulk write）实现一次连接批量写入，可以大大提升写性能。

Mongodb提供Bulk Write方式，本文通过一个试验看看性能提升的幅度。

### 1.1 试验环境

- win10 64 位操作系统
- mongodb 5.0.3
- Intel(R) Core(TM) i7-10710U CPU @ 1.10GHz   1.61 GHz
- RAM 16.0 GB

## 2. 试验过程与结果

试验拟通过不同数量规模下的Insert操作，看看bulk write和单次insert的时间性能差异。

试验中，BulkWrite全部采用 InsertOne，而单条写采用InsertOne方式实现。

### 结果呈现

试验选取了1000、10000和100000条数据的插入情况。结果发现总体性能稳定提升30倍左右。

```txt
记录数=1000, 批量耗时 = 0:00:00.013962，单条耗时 = 0:00:00.381997，性能提升27倍
记录数=10000, 批量耗时 = 0:00:00.116751，单条耗时 = 0:00:03.712907，性能提升32倍
记录数=100000, 批量耗时 = 0:00:01.236692，单条耗时 = 0:00:35.052055，性能提升28倍
```

## 附：源代码

```python
# 批量插入和单条插入比较
def compare():
    """ 批量插入和单条插入比较 """
    db = get_conn()["fdb"]
    db["bulk_compare"].drop()   # 删除测试表
    test_coll = db["bulk_compare"]

    ns = [1000, (1000 * 10), (1000 * 100)]
    for n in ns:
        # 批量插入
        requests = []
        for i in range(n):
            requests.append(InsertOne({'x': n}))
        start_dt = datetime.datetime.now()
        db["blck_test_1k"].bulk_write(requests)
        end_dt = datetime.datetime.now()
        time_bulk = (end_dt - start_dt)

        # 单条插入
        test_coll.drop()
        start_dt = datetime.datetime.now()
        for i in range(n):
            test_coll.insert_one({'x': n})
        end_dt = datetime.datetime.now()
        time_single = (end_dt - start_dt)

        print("记录数={0}, 批量耗时 = {1}，单条耗时 = {2}，性能提升{3:.0f}倍".format(
            n, time_bulk, time_single, (time_single / time_bulk)))
    test_coll.drop()
    print("比较结束")
```
