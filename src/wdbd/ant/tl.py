#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   tl.py
@Time    :   2020/02/03 16:23:44
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   爬虫通用工具

目前提供的是：

- 日志, 使用方式：log.info('xxxx')

'''
import logging.config


# =============================================
# 日志
# 使用方式：log.info('xxxx')

def get_logger(config_file_path=None):
    """
    返回一个日志器
    :rtype:
    :param config_file_path: str 配置文件路径
    :return: logger日志器
    """
    config_file_path = r'src\wdbd\ant\log.cfg'

    logging.config.fileConfig(config_file_path)
    return logging.getLogger('ant')


log = get_logger()
# =============================================

if __name__ == "__main__":
    log.info('fda 中文')
