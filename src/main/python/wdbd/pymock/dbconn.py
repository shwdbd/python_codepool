#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   dbconn.py
@Time    :   2021/12/24 10:55:30
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   测试用组件，返回mongodb.client
'''
import pymongo


def get_mg_client() -> pymongo.mongo_client.MongoClient:
    """返回mongoddb数据库客户端
    """
    try:
        user = "fd_rw"
        password = "fd1234"
        db_host = "localhost"
        db_port = 28001
        db_name = "fdb"
        url = "mongodb://{user}:{pwd}@{host}:{port}/?authSource={dbname}&ssl=false".format(
            user=user, pwd=password, host=db_host, port=db_port, dbname=db_name)
        # print(url)
        # 建立连接
        client = pymongo.MongoClient(url)
        return client
    except Exception as err:
        print("连接失败!")
        print("连接mongo数据库出现问题。err = {0}".format(err))
        

def get_mg_db() -> pymongo.mongo_client.MongoClient:
    """返回mongoddb数据库客户端
    """
    try:
        user = "fd_rw"
        password = "fd1234"
        db_host = "localhost"
        db_port = 28001
        db_name = "fdb"
        url = "mongodb://{user}:{pwd}@{host}:{port}/?authSource={dbname}&ssl=false".format(
            user=user, pwd=password, host=db_host, port=db_port, dbname=db_name)
        # print(url)
        # 建立连接
        client = pymongo.MongoClient(url)
        return client[db_name]
    except Exception as err:
        print("连接失败!")
        print("连接mongo数据库出现问题。err = {0}".format(err))


if __name__ == "__main__":
    # print(get_mg_client())
    print(get_mg_db().list_collection_names())
