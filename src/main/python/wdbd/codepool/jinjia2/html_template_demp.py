#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   html_template_demp.py
@Time    :   2020/03/27 12:51:20
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   渲染HTML文件
'''
from jinja2 import PackageLoader, Environment

# 配置路径：my_package包，templates目录下，找到模板
my_package = 'wdbd.codepool.jinjia2'
env = Environment(loader=PackageLoader(my_package, 'templates'))

template = env.get_template('my_template.tpl')   # 取得模板

# 准备数据
employee_table_header = ['编号', '姓名', '年龄']
employee_table_data = [
    {'id': '00001', 'name': '张三', 'age': '35'},
    {'id': '00002', 'name': '李四', 'age': '28'},
]

text = template.render(
    name='Jack',    # 普通变量 {{变量名}}
    age=66,
    employee_table_header=employee_table_header,
    employee_table_data=employee_table_data
    )
# print(text)
# 写文件
with open(r'src/wdbd/codepool/jinjia2/emplolyee.html', mode='w', encoding='utf-8') as f:
    f.write(text)
