#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   dataframe_to_mgdb.py
@Time    :   2021/12/17 15:56:50
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   pandas.DataFrame存入mongodb数据库
'''
import pymongo
from pymongo import InsertOne, DeleteOne, ReplaceOne
import datetime
import pandas as pd


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
    

def insert_into():
    # 存入数据
    data = {'col_1': [3, 2, 1, 0], 'col_2': ['a', 'b', 'c', 'd']}
    df = pd.DataFrame.from_dict(data)
    print(df)


if __name__ == "__main__":
    # print(get_conn())
    # insert_into()

    # df 如何 变成一个 dict的list
    data = {'col_1': [3, 2, 1, 0], 'col_2': ['a', 'b', 'c', 'd']}
    df = pd.DataFrame.from_dict(data)
    print(df)
    print(df.to_dict(orient='records'))
