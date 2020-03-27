#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   conn.py
@Time    :   2020/02/09 13:41:49
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   连接数据库组件

本程序默认是连接阿里云上开发测试库

'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_conn_engine():
    """返回数据库连接引擎
    """
    # '数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
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
    # engine = create_engine(conn_str, echo=True)
    engine = create_engine(conn_str)
    return engine


if __name__ == "__main__":
    engine = get_conn_engine()
    SessionFactory = sessionmaker(get_conn_engine())
    db_session = SessionFactory()
    # db_session.execute("delete from employee")
    db_session.execute("drop table employee")
    db_session.close()
