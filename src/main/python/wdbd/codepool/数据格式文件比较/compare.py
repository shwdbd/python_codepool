#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   compare.py
@Time    :   2021/09/27 14:25:58
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   文件比较

文件性能比较

重复N次操作；
数据容量为M；
以csv文件为基准；
比较文件大小、从文件读速度、写文件速度。
结果导出为csv文件

'''
# import pyarrow.feather as feather
import numpy as np
import pandas as pd
from datetime import datetime
import os
import sys


def get_dataframe(df_size: int = 100) -> pd.DataFrame:
    """生成数据框
    """
    np.random.seed = 42
    df_size = df_size

    df = pd.DataFrame({
        '甲': np.random.rand(df_size),
        '乙': np.random.rand(df_size),
        '丙': np.random.rand(df_size),
        '丁': np.random.rand(df_size),
        'e': np.random.rand(df_size)
    })
    return df


def runtest_csv(df: pd.DataFrame):
    data_file = "src/wdbd/codepool/文件格式比较/csv格式.csv"
    res = {}    # 返回值

    # = csv = 格式
    # 写入到当地文件
    start_dt = datetime.now()
    df.to_csv(data_file)
    end_dt = datetime.now()
    write_time = (end_dt - start_dt).microseconds / 100
    res["写入时间"] = write_time

    # 取得文件大小
    size_file = os.path.getsize(data_file)
    res["文件大小"] = size_file

    # 读文件到内存
    start_dt = datetime.now()
    pd.read_csv(data_file)
    end_dt = datetime.now()
    read_time = (end_dt - start_dt).microseconds / 100
    res["读文件时间"] = read_time

    return res


def runtest_pickle(df: pd.DataFrame):
    data_file = "src/wdbd/codepool/文件格式比较/pickle格式.data"
    res = {}    # 返回值

    # = csv = 格式
    # 写入到当地文件
    start_dt = datetime.now()
    df.to_pickle(data_file)
    end_dt = datetime.now()
    write_time = (end_dt - start_dt).microseconds / 100
    res["写入时间"] = write_time

    # 取得文件大小
    size_file = os.path.getsize(data_file)
    res["文件大小"] = size_file

    # 读文件到内存
    start_dt = datetime.now()
    pd.read_pickle(data_file)
    end_dt = datetime.now()
    read_time = (end_dt - start_dt).microseconds / 100
    res["读文件时间"] = read_time

    return res


def runtest_feather(df: pd.DataFrame):
    data_file = "src/wdbd/codepool/文件格式比较/feather格式.feather"
    res = {}    # 返回值

    # = csv = 格式
    # 写入到当地文件
    start_dt = datetime.now()
    df.to_feather(data_file)
    end_dt = datetime.now()
    write_time = (end_dt - start_dt).microseconds / 100
    res["写入时间"] = write_time

    # 取得文件大小
    size_file = os.path.getsize(data_file)
    res["文件大小"] = size_file

    # 读文件到内存
    start_dt = datetime.now()
    pd.read_feather(data_file)
    end_dt = datetime.now()
    read_time = (end_dt - start_dt).microseconds / 100
    res["读文件时间"] = read_time

    return res


def compare():
    """文件比较，并输出结果
    """
    # 取得数据
    df_size = 10000 * 10
    df = get_dataframe(df_size=df_size)
    print("数据记录数:{0} 字节".format(df_size))
    size_ram = sys.getsizeof(df)
    print("内存大小:{0} 字节".format(size_ram))
    print("=" * 20)

    test_time = 10
    for i in range(1, test_time):
        res_csv = runtest_csv(df)
        # print(res_csv)
        res_pickle = runtest_pickle(df)
        # print(res_pickle)
        res_feather = runtest_feather(df)
        # print(res_feather)
        print("写入时间, pickle: {p:0.2f}倍, feather: {fe:0.2f}倍".format(
            p=res_csv["写入时间"] / res_pickle["写入时间"], fe=res_csv["写入时间"] / res_feather["写入时间"]))
        print("读文件时间, pickle: {p:0.2f}倍, feather: {fe:0.2f}倍".format(
            p=res_csv["读文件时间"] / res_pickle["读文件时间"], fe=res_csv["读文件时间"] / res_feather["读文件时间"]))
        print("文件大小, pickle: {p:0.2f}倍, feather: {fe:0.2f}倍".format(
            p=res_csv["文件大小"] / res_pickle["文件大小"], fe=res_csv["文件大小"] / res_feather["文件大小"]))
        print("-" * 20)

    # TODO 结果汇总，绘图
    # TODO 删除临时生成的文件


if __name__ == "__main__":
    # df = get_dataframe()
    # print(df)

    compare()
