#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   conn.py
@Time    :   2022/06/15 14:46:28
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   连接SQlite3数据库


'''
import sqlite3


def conn_to():
    """
    连接数据库
    """
    db_path = r'src\main\sqlite3_dbs\test.db'

    try:
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        # 准备数据
        cur.execute("DROP TABLE tb_test")
        cur.execute("CREATE TABLE tb_test ( id   VARCHAR      PRIMARY KEY, name VARCHAR (20) )")
        cur.execute("INSERT INTO tb_test (id, name) values ('001', 'Jack')")
        cur.execute("INSERT INTO tb_test (id, name) values ('002', 'Mick')")
        conn.commit()
        cur.close()

        # 查询数据
        cur = conn.cursor()
        rs = cur.execute("select id, name from tb_test").fetchall()
        # [('001', 'Jack'), ('002', 'Mick')]
        print(rs)

        rowDict = dict(zip([c[0] for c in cur.description], rs))
        print(rowDict)
        # {'id': ('001', 'Jack'), 'name': ('002', 'Mick')}

        cur.close()
    except Exception as err:
        print('Something went wrong: ', str(err))
        conn.rollback()
        print('事务已回滚')
    finally:
        conn.close()


if __name__ == "__main__":
    conn_to()
