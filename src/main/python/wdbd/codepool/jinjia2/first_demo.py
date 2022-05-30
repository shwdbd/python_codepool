#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   first_demo.py
@Time    :   2020/03/27 12:27:06
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   使用Jinja2渲染字符串示例
'''

from jinja2 import Template

tpl = Template('my name is : {{ name }}')
text = tpl.render(name='jack')

print(text)
# my name is : jack
