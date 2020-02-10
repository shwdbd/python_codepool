#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   connect_demo.py
@Time    :   2020/02/09 13:35:23
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   连接阿里云Mysql数据库示范
'''
from sqlalchemy import create_engine
import wdbd.codepool.sqlalchemy.conn as conn


def get_conn():
    """返回数据库连接引擎
    """
    # mysql+mysqlconnector://root:password@localhost:3306/test
    server_url = 'rm-bp13oao7f763scs44yo.mysql.rds.aliyuncs.com'
    server_port = 3306
    user_id = 'dev'
    user_password = 'dev_61875707'
    db_name = 'fdata_dev'
    conn_str = 'mysql+mysqlconnector://{user_id}:{user_password}@{server_url}:{server_port}/{db_name}'.format(
        server_url=server_url,
        user_id=user_id,
        user_password=user_password,
        server_port=server_port,
        db_name=db_name)
    engine = create_engine(conn_str)
    return engine


if __name__ == "__main__":
    con = get_conn()
    print('连接数据库 : {0}'.format(con))
    print(conn.get_conn_engine())
