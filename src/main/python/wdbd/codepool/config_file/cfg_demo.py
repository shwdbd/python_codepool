#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   cfg_demo.py
@Time    :   2020/12/30 19:39:20
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   按section读取配置文件 代码示例
'''
import configparser
import os


FILE = "src/wdbd/codepool/config_file/demo_config.cfg"


def read_file():
    cf = configparser.ConfigParser()
    cf.read(FILE, encoding="UTF-8")

    # 返回所有的section名称
    secs = cf.sections()
    print("sections:{0}".format(secs))

    # 读取section_a内容
    item1 = cf.getint(section="section_a", option="item1")
    print(type(item1))
    print("section_a.item1: {0}".format(item1))

    # 读取一个不存在的内容：
    try:
        item_unkown = cf.get(section="section_a", option="xxx")
        print("不存在的内容 : {0}".format(item_unkown))
    except configparser.NoSectionError:
        print("section 未找到")
    except configparser.NoOptionError:
        print("item 未找到")


def rewrite():
    """写入一个新的配置文件
    从FILE中读取内容，更新其内容后，写入一个新的配置文件
    """
    cf = configparser.ConfigParser()
    cf.read(FILE, encoding="UTF-8")

    # 增加item4
    cf.add_section("new_section")
    cf.set(section="new_section", option="new_item", value="1a2b甲兵")

    # 修改item2

    # 写入新文件
    new_file = "src/wdbd/codepool/config_file/new_config.cfg"
    cf.write(open(new_file, mode="w", encoding="UTF-8"))

    # 判断
    if os.path.exists(new_file):
        print("写入成功")
        os.remove(new_file)
    else:
        print("写入失败！")


if __name__ == "__main__":
    read_file()
    # rewrite()
