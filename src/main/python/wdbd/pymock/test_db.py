#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test_db.py
@Time    :   2021/12/24 11:02:24
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   测试用组件，数据库应用测试
'''
import unittest
import wdbd.pymock.db_app as app
from unittest.mock import patch
# from mongomock import MongoClient
import mongomock


class TestDbApp(unittest.TestCase):

    def setUp(self) -> None:
        # 准备模拟数据
        # 模拟库
        self.mock_db = mongomock.MongoClient().db_test
        # 模拟数据
        self.mock_db.test_A.insert_one({"a": 1})

        return super().setUp()

    def test_read(self):
        # # 打印模拟库
        # print(self.mock_db.list_collection_names())
        # print(self.mock_db["test_A"].find_one({"a": 1}))

        with patch("wdbd.pymock.db_app.dbconn.get_mg_db") as db:
            db.return_value = self.mock_db
            self.mock_db.create_collection("TBs")
            print(app.get_tables())
            self.assertEqual(['test_A', 'TBs'], app.get_tables())


if __name__ == "__main__":
    unittest.main()
