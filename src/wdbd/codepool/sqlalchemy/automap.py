#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   automap.py
@Time    :   2020/02/10 20:20:27
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   根据数据库现有表结构，反向形成Class Mapping
'''
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import wdbd.codepool.sqlalchemy.conn as conn
from sqlalchemy.orm import relationship


Base = automap_base()

engine = conn.get_conn_engine()


# reflect the tables
Base.prepare(engine, reflect=True)

# mapped classes are now created with names by default
# matching that of the table name.
Address = Base.classes.addresses
User = Base.classes.users
User.address_collection = relationship("address", collection_class=set)


session = Session(engine)

mark = User(name='mark')
# for i in User.__dict__.items():
#     print(i)

# print('   ')
# for i in Address.__dict__.items():
#     print(i)

# print(User.__dict__.items())
# mark.address_collection([Address(email_address='foo1@bar.com'), Address(email_address='foo2@bar.com')])

# session.add(Address(email_address="foo@bar.com", users=User(name="foo")))
# session.add(mark)
session.commit()



