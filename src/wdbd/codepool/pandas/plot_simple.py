#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   plot_simple.py
@Time    :   2019/11/06 20:14:41
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   pandas 绘图 基本功能示例

1. plot                 绘制折线图
2. plot_saveas          图片另存为



matplotlib.pyplot.figure 绘制一个新的图形


'''
import pandas as pd
import tushare as ts
import numpy as np
import matplotlib.pyplot as plt


def demo_plot():
    """
    绘制简单的折线图，弹出窗口显示
    """
    sample_size = 10
    data = np.random.randint(low=1, high=10, size=(sample_size, 1))
    print(data)

    plt.figure(figsize=(8, 6))  # 定义画布
    plt.plot(data)  # 绘制数据

    plt.show()


def demo_figure_axes():
    """
    建立1个包含4个Axes的空Figure
    """
    # 建立一个空的figure
    fig = plt.figure()  # an empty figure with no axes
    fig.suptitle('No axes on this figure')  # Add a title so we know which it is

    # 建立一个2*2的figure
    fig, ax_lst = plt.subplots(2, 2)  # a figure with a 2x2 grid of Axes
    plt.show()




if __name__ == "__main__":
    demo_figure_axes()
