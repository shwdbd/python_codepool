#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   df_rolling.py
@Time    :   2019/10/29 15:01:08
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   移动窗口

DataFrame.rolling函数，多用于移动平均的计算

官方API：
https://pandas.pydata.org/pandas-docs/version/0.18.1/generated/pandas.DataFrame.rolling.html
https://pandas.pydata.org/pandas-docs/version/0.18.1/generated/pandas.Series.rolling.html#pandas.Series.rolling

参考文档：
https://baijiahao.baidu.com/s?id=1622798772654712959&wfr=spider&for=pc


1. demo_ma5    计算5日移动平均线
2. 

'''
import pandas as pd


def demo_m5():
    """计算5日移动平均线
    """
    data = pd.Series([1, 2, 3, 4, 5, 6])
    print(data)
    m5obj = data.rolling(window=5)
    print(m5obj.mean())     # NaN NaN NaN NaN 3 4
    m5obj = data.rolling(window=5, min_periods=1)
    print(m5obj.mean())     # 1 1.5 2 2.5 3 4



if __name__ == "__main__":
    demo_m5()

