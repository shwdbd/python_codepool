#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   first_plot.py
@Time    :   2020/08/13 09:36:15
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   matplotlib的简单用法示例

绘制一个最简单的折线图

'''
import numpy as np
from matplotlib import pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']


def draw():
    """绘制图形
    """
    # 准备画布
    plt.figure(figsize=(6, 6))
    plt.title('简单折线图')

    # 准备数据点
    x = np.linspace(0, 50, 10)   # 0-2中间50个点
    plt.plot(x, x, label="x")
    plt.plot(x, 3*x, label="3x")

    # 显示
    plt.show()
    # plt.savefig('demo_1.png')   # 保存成文件


if __name__ == "__main__":
    draw()
