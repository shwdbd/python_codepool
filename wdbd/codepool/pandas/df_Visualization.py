#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   df_Visualization.py
@Time    :   2019/10/21 15:02:25
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   pandas自带的可视化操作工具

- 图形的输出
- 常用样式调整
- 直方图等各类图形的示例

! 必须先装 pip install pyqt5


pd.DataFrame有一组绘图函数，DOC:
https://pandas.pydata.org/pandas-docs/stable/reference/frame.html#plotting

1. simple_plot      最简单的绘图


'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def simple_plot():
    """
    最简单的绘图
    """
    ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
    df = pd.DataFrame(np.random.randn(1000, 4),
                      index=ts.index, columns=list('ABCD'))
    print(df.head())

    df_ax = df.plot()
    plt.show()  # 窗口弹出

    # 文件另存为
    fig = df_ax.get_figure()
    fig.savefig(r'temp_files\fig.png')



def demo_stock():
    """
    用tushare股票数据绘制图形
    
    为避免泄露userid，使用模拟的数据
    """
    # 构建
    # 使用 date_range构建一个index，然后用 随机函数构建数据
    list_l = [[1, 3, 3, 5, 4], [11, 7, 15, 13, 9], [4, 2, 7, 9, 3], [15, 11, 12, 6, 11]]
    date_range = pd.date_range(start="20180701", periods=4)
    df = pd.DataFrame(list_l, index=date_range, columns=['a', 'b', 'c', 'd', 'e'])
    print(df)

    df_ax = df.plot(figsize=(8, 4))
    # print(type(df_ax))  # <class 'matplotlib.axes._subplots.AxesSubplot'>
    plt.xlabel("time")
    plt.ylabel("num")
    plt.legend(loc="best")
    plt.scatter(df.index, df["a"], c="red", marker="*")  # 这个例子中，散点图是在 plt.legend 命令之后画的，所以不会出现在图例中（对比下面的例子理解）。
    plt.show()


if __name__ == "__main__":
    demo_stock()

