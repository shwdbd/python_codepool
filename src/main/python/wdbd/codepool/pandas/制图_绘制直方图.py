#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   制图_绘制直方图.py
@Time    :   2022/01/25 11:06:45
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   绘制直方图
'''
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']


def get_data() -> pd.DataFrame:
    data = {
        'id': np.arange(5),
        'menMeans': [20, 35, 30, 35, -27],
        'womenMeans': [25, 32, 34, 20, -25],
        'menStd': [2, 3, 4, 1, 2],
        'womenStd': [3, 5, 2, 3, 3]
    }
    df = pd.DataFrame(data)
    return df


def show_simple_bar():
    df = get_data()
    plt.bar(x=df['id'], height=df['menMeans'], color='orange')
    plt.xticks(x=df['id'], rotation=90)
    plt.xlabel("序号")
    plt.ylabel("男性平均年龄")
    plt.title("男性平均年龄分布", fontsize=16)

    plt.show()


def show_bar():
    df = get_data()
    fig, ax = plt.subplots()

    p1 = ax.bar(df['id'], df['menMeans'], width=0.35, label='Men')
    p2 = ax.bar(df['id'], df['womenMeans'], width=0.35, bottom=df['menMeans'], label='Women')

    ax.axhline(0, color='grey', linewidth=0.8)
    ax.set_ylabel('Scores')
    ax.set_title('Scores by group and gender')
    # ax.set_xticks(df['id'], labels=['G1', 'G2', 'G3', 'G4', 'G5'])
    ax.legend()

    # Label with label_type 'center' instead of the default 'edge'
    # ax.bar_label(p1, label_type='center')
    # ax.bar_label(p2, label_type='center')
    # ax.bar_label(p2)

    plt.show()


if __name__ == "__main__":
    df = get_data()
    print(df)
    # show_bar()
    show_simple_bar()
