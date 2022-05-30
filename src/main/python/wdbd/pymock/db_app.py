#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   db_app.py
@Time    :   2021/12/24 10:58:34
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   测试用组件，数据库应用
'''
import wdbd.pymock.dbconn as dbconn


def print_test_collection():
    """ 打印test_abc表内容 """
    client = dbconn.get_mg_client()
    db = client["fdb"]
    res = []
    for record in db["test_A"].find({}):
        print(record)
        res.append(record)
    return res


def get_tables():
    print(dbconn.get_mg_db())
    return dbconn.get_mg_db().list_collection_names()


if __name__ == "__main__":
    print(get_tables())
