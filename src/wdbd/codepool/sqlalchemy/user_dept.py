#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   user_dept.py
@Time    :   2020/02/09 14:03:54
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   用 员工、部门 为例子，实现ORM基本操作
'''
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import wdbd.codepool.sqlalchemy.conn as conn
from sqlalchemy.orm import aliased
from sqlalchemy import text
from sqlalchemy import func


Session = sessionmaker(bind=conn.get_conn_engine())

# 创建对象的基类:
Base = declarative_base()


# 定义User对象:
class Employee(Base):
    # 表的名字:
    __tablename__ = 'employee'

    # 表的结构:
    # id = Column('id', String(20), primary_key=True)
    name = Column('name', String(20), primary_key=True)
    age = Column('age', Integer())

    def __repr__(self):
        return "<Employee(name='%s', age='%i')>" % (
                        self.name, self.age)


class EmployeeManager:

    def __init__(self):
        # session = Session()
        # session.execute('delete from employee')
        # session.commit()
        pass

    def create_db_structor(self):
        # 建立表结构:
        engine = conn.get_conn_engine()
        Base.metadata.create_all(engine)
        print('数据库表结构 新建完毕!')

    def add(self, new_emplpoyee):
        # 新添加记录
        # new_emplpoyee 是 Employee or list
        # pk重复的情况，会抛出异常
        try:
            session = Session()

            if type(new_emplpoyee) is Employee:
                session.add(new_emplpoyee)
            elif type(new_emplpoyee) is list:
                session.add_all(new_emplpoyee)
            else:
                print('新增员工，参数类型错误！')
                raise Exception('新增员工，参数类型错误！')

            session.commit()
        except Exception as err:
            print('Exp:' + str(err))
            session.rollback()
        finally:
            pass

    def query(self):
        session = Session()

        # # 所有：
        # for instance in session.query(Employee).order_by(Employee.age):
        #     print(instance)

        # # 所有，按字段
        # for name, age in session.query(Employee.name, Employee.age):
        #     print("{0} , {1}".format(name, age))

        # # 查询所有，对象和字段混用， KeyedTuple
        # for row in session.query(Employee, Employee.age).all():
        #     print("{0} , {1}".format(row.Employee, row.age))
        # # <Employee(name='U1', age='1')> , 1
        
        # 列可以取别名
        for row in session.query(Employee, Employee.age.label('suishu')).all():
            print("{0} , {1}".format(row.Employee, row.suishu))
        # <Employee(name='U1', age='1')> , 1

    def query_all_by_aliased(self):
        # 整个表对象都用别名
        session = Session()
        user_alias = aliased(Employee, name='user_alias')
        for row in session.query(user_alias, user_alias.name).all():
            print(row.user_alias)

    def query_limit(self):
        """查询，使用LIMIT和OFFSET

        类似于SQL中: TOP 10, LIMIT 10
        """
        session = Session()
        # 仅查前3个(含第三个)，age逆序排序
        for row in session.query(Employee).order_by(-Employee.age)[:3]:
            print(row)
        
    def query_by_filter(self):
        # 条件查询
        session = Session()

        # 单一条件：
        print('单一条件 = 年龄小于等于5：')
        print('使用filter_by:')
        for row in session.query(Employee).filter_by(age=5):
            print(row)
        print('使用filter:')
        for row in session.query(Employee).filter(Employee.age <= 5)[:3]:
            print(row)
        

    def query_by_filter_text(self):
        """使用SQL语句进行过滤查询
        """
        session = Session()
        # 直接的SQL语句
        # for row in session.query(Employee).filter(text(' AGE<3 and name like "U%" ')).all():
        #     print(row)
        # 含参数的SQL：使用:字段的形式
        # sql = 'AGE<:age and name like ":name_pre%"'
        sql = 'AGE<:age and name=:name_pre'
        for row in session.query(Employee).filter(text(sql)).params(age=5, name_pre='U1').all():
            print(row)

    def query_count(self):
        """查询，使用COUNT
        """
        session = Session()
        count = session.query(Employee).filter(Employee.name.like('U%')).count()
        print(count)

    def query_group_count(self):
        """查询，GROUP和COUNT配合
        """
        session = Session()
        result = session.query(func.count(Employee.age), Employee.age).group_by(Employee.age).all()
        print(result)
        # [(1, 1), (1, 2), (1, 3), (1, 4), (2, 5), (1, 6), (1, 7), (1, 8), (1, 9)]
        # SELECT count(employee.age) AS count_1, employee.age AS employee_age FROM employee GROUP BY employee.age

    def query_count_star(self):
        # SELECT count(*) FROM table
        session = Session()
        result = session.query(func.count('*')).select_from(Employee).scalar()
        print(result)


if __name__ == "__main__":
    # dirty数据无Demo

    mgr = EmployeeManager()
    # mgr.create_db_structor()
    
    # print(Employee.__table__)

    # e1 = Employee(name='JACK', age=33)
    # e2 = Employee(name='Mike', age=55)
    # lst_employee = [e1, e2]
    # # mgr.add(lst_employee)
    # mgr.add(e1)

    # lst_em = []
    # for i in range(1, 10):
    #     lst_em.append(Employee(name='U'+str(i), age=i))
    # mgr.add(lst_em)

    # query:
    # mgr.query()
    # mgr.query_all_by_aliased()
    # mgr.query_limit()
    # mgr.query_by_filter()
    # mgr.query_by_filter_text()
    # mgr.query_count()
    # mgr.query_group_count()
    mgr.query_count_star()
