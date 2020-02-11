#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   tree_node_helloworld.py
@Time    :   2020/02/10 22:54:07
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   Tree and Node Demo

这个例子是"Tree - Node"的一个简单一对多数据库操作示范。其使用的是mysql数据库（基于阿里云）。代码实现的功能如下：

- 根据class的定义，创建数据库表结构
- 新增一个Tree，含有两个Node
- 按名称（单条件、多条件）查询
- 实现Count
- 修改Node内容
- 删除Tree（级联删除）

'''
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import wdbd.codepool.sqlalchemy.conn as conn
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


Session = sessionmaker(bind=conn.get_conn_engine())

# 创建对象的基类:
Base = declarative_base()


# ---------------------------
# 定义Mapping对象：
class Tree(Base):
    # 表的名字:
    __tablename__ = 'test_tree'

    # 表的结构:
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(20))

    # 配置引用关系 tree.nodes
    nodes = relationship("Node", backref='tree', cascade='all, delete-orphan')

    def __repr__(self):
        return "<Tree(id='%s', name='%s')>" % (self.id, self.name)


class Node(Base):
    __tablename__ = 'test_tree_nodes'

    id = Column(Integer, primary_key=True)
    node_name = Column('node_name', String(50), nullable=False)
    weight = Column('weight', Integer, default=5)

    # 外键，子表设置外键
    tree_id = Column(Integer, ForeignKey('test_tree.id'))   # 配置外键

    def __repr__(self):
        return "<Node(tree='{0}', name='{1}', weight='{2}')>".format(self.tree_id, self.node_name, self.weight)


# ---------------------------
# 业务处理程序：
class TreeManager():

    def __init__(self):
        self.DB_session = sessionmaker(conn.get_conn_engine())

    def create_tables(self):
        # 重建数据库表
        # db_session = self.DB_session()
        # db_session.create_tables
        Base.metadata.create_all(conn.get_conn_engine())
        print('重建数据库表结构')

    def print_tree(self, name):
        # 根据name打印tree
        db_session = self.DB_session()
        tree = db_session.query(Tree).filter(
            Tree.name == name).order_by(-Tree.id).first()
        if not tree:
            print('Tree Not Found')
        else:
            print('Tree obj is {0}'.format(tree))
            print('Tree.nodes is {0}'.format(tree.nodes))

    def addTree(self, tree_name):
        print('添加一个Tree，其下有左右两个Node ... ')
        db_session = self.DB_session()
        tree = Tree(name=tree_name)
        db_session.add(tree)
        tree = db_session.query(Tree).order_by(-Tree.id).first()
        nodes = [
            Node(node_name='Left for ' + str(tree.name), weight=1, tree=tree),
            Node(node_name='Right for ' + str(tree.name), weight=2, tree=tree),
        ]
        db_session.add_all(nodes)
        db_session.commit()

        print('新增完毕，新增内容是：')
        tree = db_session.query(Tree).order_by(-Tree.id).first()
        print('Tree obj is {0}'.format(tree))
        print('Tree.nodes is {0}'.format(tree.nodes))
        return tree

    def modify_node_weight(self, tree_name, node_name, new_wight):
        """修改某节点的权重数值
        node_name 是 模糊查询
        """
        db_session = self.DB_session()
        the_tree = db_session.query(Tree).filter(
            Tree.name == tree_name).first()
        print(the_tree)
        if the_tree:
            the_node = db_session.query(Node).filter(Node.tree_id == the_tree.id).filter(
                Node.node_name.like(node_name + '%')).first()
            print(the_node)
            the_node.weight = new_wight
            db_session.commit()
            print('更新完毕')

    def get_node_count(self, tree_name):
        """统计符合条件的节点数量
        """
        db_session = self.DB_session()
        the_tree = db_session.query(Tree).filter(
            Tree.name == tree_name).first()
        print(the_tree)
        print(len(the_tree.nodes))

        # 第二种方法：
        print(db_session.query(Node).filter(
            Node.tree_id == the_tree.id).count())
        print(db_session.query(Tree, Node).filter(Node.tree_id ==
                                                  Tree.id).filter(Tree.name == tree_name).count())

    def del_tree(self, tree_name):
        """
        删除Tree，并级联删除其下所有的Node

        在Tree.nodes关系中配置了 cascade='all, delete-orphan' 所以可以实现级联删除
        """
        db_session = self.DB_session()
        the_tree = db_session.query(Tree).filter(
            Tree.name == tree_name).first()
        if not the_tree:
            print('未找到Tree，删除失败')
        else:
            db_session.delete(the_tree)
            db_session.commit()


if __name__ == "__main__":
    mgr = TreeManager()
    mgr.create_tables()     # 创建数据库表

    # mgr.addTree('新建二叉树')   # 新建父子表内容
    # mgr.modify_node_weight('新建二叉树', 'Right', 100)   # 查询子表，并修改内容
    # mgr.get_node_count('新建二叉树')    # Count

    # 级联删除
    tree_name = 'ABC'
    mgr.addTree(tree_name)
    mgr.print_tree(tree_name)
    mgr.del_tree(tree_name)
    mgr.print_tree(tree_name)
