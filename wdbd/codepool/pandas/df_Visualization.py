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
import tushare as ts


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
    """
    pass


if __name__ == "__main__":
    demo_stock()

