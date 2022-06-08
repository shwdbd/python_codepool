#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   multi_subplot.py
@Time    :   2020/08/11 20:43:26
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   在一个界面中展示多个图形的示例



'''
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']


def draw():
    # 准备数据
    names = ['组A', '组B', '组C']
    values = [1, 10, 100]

    # 总画布的尺寸
    plt.figure(figsize=(9, 3))

    # 3个子图，都排在第一列，由左到右排列
    # 子图1，Bar图
    plt.subplot(131)
    plt.bar(names, values)
    # 子图2，散点图
    plt.subplot(132)
    plt.scatter(names, values)
    # 子图3，折线图
    plt.subplot(133)
    plt.plot(names, values)

    plt.suptitle('Categorical Plotting')
    plt.show()


if __name__ == "__main__":
    draw()
