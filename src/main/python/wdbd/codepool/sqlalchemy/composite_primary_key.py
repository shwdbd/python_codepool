#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   composite_primary_key.py
@Time    :   2020/02/12 15:26:49
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   联合主键代码示例

表 BookOwner 有两个主键字段：uid, bid

'''
from sqlalchemy import Column, String, Integer, and_
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import wdbd.codepool.sqlalchemy.conn as conn


Session = sessionmaker(bind=conn.get_conn_engine())

# 创建对象的基类:
Base = declarative_base()


# ---------------------------
# 定义Mapping对象：
class BookOwner(Base):
    # 表的名字:
    __tablename__ = 'book_owner'

    # 表的结构:
    uid = Column('uid', Integer, primary_key=True)
    bid = Column('bid', Integer, primary_key=True)
    name = Column('name', String(20))

    def __repr__(self):
        return "<BookOwner(uid='%s', bid='%s', name='%s')>" % (self.uid, self.bid, self.name)


# ---------------------------
# 业务处理程序：
class BookManager():

    def __init__(self):
        self.DB_session = sessionmaker(conn.get_conn_engine())

    def create_tables(self):
        # 重建数据库表
        Base.metadata.create_all(conn.get_conn_engine())
        print('重建数据库表结构')

    def add(self, uid, bid, name):
        # 新增对象
        db_session = self.DB_session()
        exsit_obj = db_session.query(BookOwner).filter(and_(BookOwner.uid == uid, BookOwner.bid == bid)).first()
        if exsit_obj:
            print('对象{0}已存在，无法新增！'.format(exsit_obj))
        else:
            bo = BookOwner(uid=uid, bid=bid, name=name)
            db_session.add(bo)
            db_session.commit()
            print('新增完成, {0}'.format(bo))


if __name__ == "__main__":
    mgr = BookManager()
    # mgr.create_tables()

    # 新增
    mgr.add(1, 1, '书1人1')
    mgr.add(1, 1, '书1人1')
    # 新增完成, <BookOwner(uid='1', bid='1', name='书1人1')>
    # 对象<BookOwner(uid='1', bid='1', name='书1人1')>已存在，无法新增！
