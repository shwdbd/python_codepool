#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   conn_with.py
@Time    :   2022/06/15 15:21:13
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   数据库连接使用With Demo
'''
import sqlite3


class SQLiteDb:
    """SQlite3数据库访问上下文
    """

    def __init__(self):
        self.db_path = r'src\main\sqlite3_dbs\test.db'
        self.conn = sqlite3.connect(self.db_path)
        self.cur = self.conn.cursor()
        # 准备原始数据

    def __str__(self):
        return "py sqlite数据库上下文管理器"

    def __enter__(self):
        # 返回类对象本身
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cur.close()
        self.conn.close()
        print("连接已关闭")

    # 查询单条数据
    def query_one(self, sql):
        try:
            self.cur.execute(sql)
            res = self.cur.fetchone()
            return res
        except Exception as e:
            print(e)

    # TODO 查询多条
    # TODO 数据库执行，多条SQL

    # TODO 每次执行，要记录SQL语句


if __name__ == "__main__":
    with SQLiteDb() as db:
        print(db.query_one("select name from tb_test"))
