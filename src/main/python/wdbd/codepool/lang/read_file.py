#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   read_file.py
@Time    :   2020/08/04 20:41:46
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   读文本文件代码示例

函数 read_file_with 展示了使用with语句读取
函数 read_file_try  展示了使用try...exception模式读取

'''

# 示例文件位置
DEMO_FILE = "src/wdbd/codepool/lang/600016.SH.csv"


def read_file_try():
    """使用try...exception模式读取
    """

    try:
        f = open(DEMO_FILE, mode="r")
        # 读取所有的行
        print("所有行数据：")
        for line in f.readlines():
            print(line.rstrip())    # 从第一行顺序读取，去除最后的回车符
    except IOError as ioerr:
        print("【读取失败】" + str(ioerr))
    finally:
        f.close()



def read_file_with():
    """使用with指令读取文件
    """
    with open(DEMO_FILE, mode="r") as f:
        first_line = f.readline(10)  # 读取第一行，前10个字符
        print("第一行前10个字符：{0}".format(first_line))   # ts_code,tr

        # 读取所有的行
        print("所有行数据：")
        for line in f.readlines():
            # print(line)           # 从第一行顺序读取，每一行都有一个回车符
            print(line.rstrip())    # 从第一行顺序读取，去除最后的回车符

    print("End!")


if __name__ == "__main__":
    # # 展示了使用with语句读取
    # read_file_with()

    # 展示了使用try...exception模式读取
    read_file_try()
