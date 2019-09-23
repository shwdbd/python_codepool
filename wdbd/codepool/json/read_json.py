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

# here put the import lib
if __name__ == "__main__":
    file = os.getcwd() + "\\wdbd\\codepool\\json\\demo_json.json"
    f = open(file,encoding='utf-8')

    content=f.read()    #使用loads()方法，需要先读文件
    user_dic=json.loads(content)
    print(user_dic)


# TODO 将 对象object 变为 json
# TODO 修改json文件内容（格式化输出）
# https://www.runoob.com/python/python-json.html


