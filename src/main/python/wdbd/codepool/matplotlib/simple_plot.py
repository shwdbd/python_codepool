#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   simple_plot.py
@Time    :   2020/08/11 14:24:38
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   最简单的图形

展示 y=3x, y=3x^2, y=3x^3三条函数线


# 按点画出x、y的一次函数曲线
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16])

# 样式：
# 颜色：
# r红，g绿，b蓝
# 点样式：
# --， ^, s方块， o 圆点， +十字符


'''
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']


def draw():
    # 绘图

    x = np.linspace(0, 50, 10)   # 0-2中间50个点
    # print(x)

    fig, ax = plt.subplots()
    # 绘图
    ax.plot(x, x, label='linear')
    ax.plot(x, x**2, "y-", label='x^2')
    ax.plot(x, 3*x, "g^", label='x*3')

    # 标注xy轴：
    ax.set_xlabel('x 标签', fontsize=14, color='red')  # Add an x-label to the axes.
    ax.set_ylabel('y 标签')  # Add a y-label to the axes.
    ax.set_title("简单绘图")  # Add a title to the axes.

    # 设定x、y轴刻度
    plt.axis([0, 60, 0, 200])       # x轴0-60，y轴0-200

    ax.legend()  # Add a legend.

    plt.show()


if __name__ == "__main__":
    draw()
