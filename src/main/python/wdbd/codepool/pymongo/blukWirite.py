#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   blukWirite.py
@Time    :   2021/12/10 16:36:09
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   批量操作程序示例

bluk_write 语法：https://pymongo.readthedocs.io/en/stable/api/pymongo/collection.html

- get_conn 数据库连接
- bluk_write 简单批量写示例
- compare_of_bulk_and_insert 批量写和单独写的比较

'''
import pymongo
from pymongo import InsertOne, DeleteOne, ReplaceOne
import datetime


def get_conn():
    """ 数据库连接 """
    try:
        user = "fd_rw"
        password = "fd1234"
        db_host = "localhost"
        db_port = "28001"
        db_name = "fdb"
        url = "mongodb://{user}:{pwd}@{host}:{port}/?authSource={dbname}&ssl=false".format(
            user=user, pwd=password, host=db_host, port=db_port, dbname=db_name)
        # 建立连接
        client = pymongo.MongoClient(url)
        return client
    except Exception as err:
        print("连接mongo数据库出现问题。err = {0}".format(err))
        return None


def bluk_write():
    """ 批量写库示例 """

    db = get_conn()["fdb"]

    print(db.list_collection_names())

    requests = [InsertOne({'y': 1}), DeleteOne(
        {'x': 1}), ReplaceOne({'w': 1}, {'z': 1}, upsert=True)]
    result = db["blck_test"].bulk_write(requests)
    print(result.inserted_count)
    print(result.deleted_count)
    print(result.modified_count)
    print(result.upserted_ids)

    for doc in db["blck_test"].find({}):
        print(doc)


def bulk_w_1K(n=1000):
    """ 快速插入1000条 统计时间 """

    db = get_conn()["fdb"]
    db["blck_test_1k"].drop()

    print("start bulk insert")
    requests = []
    for i in range(n):
        requests.append(InsertOne({'n': n}))
    start = datetime.datetime.now()
    result = db["blck_test_1k"].bulk_write(requests)
    end = datetime.datetime.now()

    print("insert record count = {0}".format(result.inserted_count))
    print("耗时 = {0}".format((end - start)))


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


if __name__ == "__main__":
    # client = get_conn()
    # print(client)

    # bluk_write()

    compare()
