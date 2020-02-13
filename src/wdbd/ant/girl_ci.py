#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   girl_ci.py
@Time    :   2020/02/03 20:00:15
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   影集下载全局变量
'''

# 默认下载文件夹：
# DOWN_DIR = r'c:\temp\girls\\心妍小公主(李妍曦)\\'
DOWN_DIR = r'temp_files\girls\\'

# 图片url格式
PIC_URL = 'https://mtl.gzhuibei.com/images/img/{girl_id}/{pic_id}.jpg'

# 临时json文件位置：
TEMP_JSON = r'temp_files\girls.json'
TEMP_HTML = r'temp_files\girls.html'

# 是否真正下载照片文件，测试用
DOWN_PIC = False
# DOWN_PIC = True
