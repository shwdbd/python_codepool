#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test_girlant_down.py
@Time    :   2020/02/03 19:50:02
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   影集下载功能单元测试
'''
import unittest
import src.wdbd.ant.girl_picture_ant as girl_ant
import src.wdbd.ant.girl_ci as ci
import os
import shutil


class Test_Download_SingleListPage(unittest.TestCase):
    """测试 下载单个列表页面
    """

    url = 'https://www.meitulu.com/t/1386/'     # 共5个
    down_dir = r'temp_files\girl\\'

    def tearDown(self):
        if os.path.exists(self.down_dir):
            shutil.rmtree(self.down_dir)
            # os.removedir(self.down_dir)
        return super().tearDown()

    # 耗时太长，谨慎测试
    def test_success(self):
        """
        测试下载整个集合的情况
        """
        count_of_set = 5
        r = girl_ant.download_single_listpage(self.url, self.down_dir)
        self.assertEqual(count_of_set, r)
        # 检查下载的目录数量
        self.assertEqual(count_of_set, len(os.listdir(self.down_dir)))

    def test_fail(self):
        """测试 下载失败的情况
        """
        err_url = 'xxxx'
        err_dir = 'z:\\xxx\\'

        # 测试，文件夹不存在的情况
        r = girl_ant.download_single_listpage(self.url, err_dir)
        self.assertEqual(0, r)

        # 测试，url不存在的情况
        r = girl_ant.download_single_listpage(err_url, self.down_dir)
        self.assertEqual(0, r)


class Test_Download_SinglePage(unittest.TestCase):
    """测试下载单个影集
    """

    down_dir = ci.DOWN_DIR

    def tearDown(self):
        if os.path.exists(self.down_dir):
            shutil.rmtree(self.down_dir)
        return super().tearDown()

    def test_download_single(self):
        """测试 单个页面下载
        """
        url = 'https://www.meitulu.com/item/15267.html'
        name = '[YOUWU尤物馆] VOL.099 木木hanna - 性感黑丝吊袜写真'
        r = girl_ant.download_single(url)
        self.assertEqual(38, r)     # 下载文件数
        dw_dir = ci.DOWN_DIR + name + '\\'
        self.assertTrue(os.path.exists(dw_dir))     # 生成的文件夹
