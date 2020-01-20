#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   read_json.py
@Time    :   2019/09/23 17:00:35
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   Python 读取 Json文件示例
'''
import os
import json


def get_value_by_key():
    """
    用 key 取得值的示例程序
    """
    file = os.getcwd() + "\\wdbd\\codepool\\json\\demo_json.json"
    f = open(file, encoding='utf-8')
    json_obj = json.loads(f.read())

    print(type(json_obj))

    print(json_obj.get("error_code"))
    print(type(json_obj.get("error_code")))
    print(type(json_obj.get("stu_info")[0].get("name")))
    print(json_obj.get("stu_info")[0].get("name"))

    print(json_obj.get("stu_info")[0].get("xxx"))



if __name__ == "__main__":
    get_value_by_key()


# TODO 将 对象object 变为 json
# TODO 修改json文件内容（格式化输出）
# https://www.runoob.com/python/python-json.html


