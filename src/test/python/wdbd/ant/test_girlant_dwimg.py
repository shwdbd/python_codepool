#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test_girlant_dwimg.py
@Time    :   2020/02/01 10:30:48
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   单元测试，单个照片下载的函数
'''
import unittest
import wdbd.ant.girl_picture_ant as girl_ant
import os


class Test_DownloadImg(unittest.TestCase):

    url = 'https://www.baidu.com/img/baidu_jgylogo3.gif'
    target_file = r'temp_files\dw_img.gif'

    def setUp(self):
        if os.path.exists(self.target_file):
            os.remove(self.target_file)
        return super().setUp()

    def tearDown(self):
        if os.path.exists(self.target_file):
            os.remove(self.target_file)
        return super().tearDown()

    def test_success(self):
        """测试下载照片成功
        """
        r = girl_ant.download_img(img_url=self.url, pic_file_path=self.target_file)
        self.assertEqual('success', r)

        # 检查下载的文件是否存在
        self.assertTrue(os.path.exists(self.target_file))

    def test_url_error(self):
        err_url = 'xxxx.html'
        r = girl_ant.download_img(img_url=err_url, pic_file_path=self.target_file)
        self.assertEqual('failed', r)

        # url = None
        r = girl_ant.download_img(img_url=None, pic_file_path=self.target_file)
        self.assertEqual('failed', r)
