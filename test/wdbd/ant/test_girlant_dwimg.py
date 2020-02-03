#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test_girlant_dwimg.py
@Time    :   2020/02/01 10:30:48
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   单元测试，照片下载的函数
'''
import unittest
import src.wdbd.ant.girl_picture_ant as girl_ant


class Test_DownloadImg(unittest.TestCase):

    def test_success(self):
        # print( sys.path )
        # for path in sys.path:
        #     print(path)
        url = 'https://www.meitulu.com/t/beautyleg/23.html'
        girl_ant.download_list(url)

        self.assertTrue(self)


