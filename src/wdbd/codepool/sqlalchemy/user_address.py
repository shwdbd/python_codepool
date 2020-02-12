#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   user_address.py
@Time    :   2020/02/09 21:01:51
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   None
'''
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import wdbd.codepool.sqlalchemy.conn as conn
from sqlalchemy.orm import aliased
from sqlalchemy import text
from sqlalchemy import func
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


Session = sessionmaker(bind=conn.get_conn_engine())

# 创建对象的基类:
Base = declarative_base()


# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'users'

    # 表的结构:
    id = Column(Integer, primary_key=True)
    name = Column('name', String(20))
    fullname = Column('fullname', String(20))
    nickname = Column('nickname', String(20))

    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (
                        self.name, self.fullname, self.nickname)


class Address(Base):
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True)
    email_address = Column('email_address', String(50), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="addresses")

    def __repr__(self):
        return "<Address(email_address='%s')>" % self.email_address


User.addresses = relationship(
        "Address", order_by=Address.id, back_populates="user")


class UserManager():

    def create_tables(self):
        # 创建表结构
        Base.metadata.create_all(conn.get_conn_engine())



if __name__ == "__main__":
    mgr = UserManager()

    mgr.create_tables()

