#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   df_apply_func.py
@Time    :   2019/10/15 17:39:01
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   apply函数

DOC:
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.apply.html#pandas.DataFrame.apply
'''
import pandas as pd


def demo_df_apply():
    # 简单apply函数，其中x是这列的值
    df = pd.DataFrame([[4, 9]] * 3, columns=['A', 'B'])
    print("原始数:")
    print(df)
    print("转换后:")
    print(df.apply(lambda x: x - 1))


def is_shanghai(custid, cust_name: str = ""):
    if "上海" in cust_name and custid == 1:
        return "是"
    else:
        return "否"


def set_shanghai():
    # 将 公司名字中含有上海的设置上海标识
    # 单列示例
    data = {
        "客户号": [11111, 222222],
        "户名": ["上海公司A", "南京公司A"]}
    df = pd.DataFrame(data)
    print(df)
    # 设置
    df["上海元素"] = df["户名"].apply(is_shanghai)
    print(df)
    df["上海元素2"] = df.apply(lambda x: is_shanghai(x['客户号'], x['户名']), axis=1)
    print(df)


if __name__ == "__main__":
    # demo_df_apply()
    set_shanghai()
