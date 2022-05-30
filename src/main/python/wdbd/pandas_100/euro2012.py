#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   euro2012.py
@Time    :   2021/03/24 13:54:04
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   探索2012欧洲杯数据
'''
import pandas as pd


if __name__ == "__main__":
    url = "src/wdbd/pandas_100/data/Euro2012_stats.csv"

    # 加载数据
    euro12 = pd.read_csv(url, sep=',')

    # 只选取 Goals 这一列
    print("Goals列数据：")
    print(euro12.Goals.head())

    # 有多少球队参与了2012欧洲杯？
    print("有多少球队参与了2012欧洲杯？ 答案 = {0}".format(euro12.Team.nunique()))

    # 该数据集中一共有多少列(columns)?
    print("数据集中一共有多少列 = {0}".format(len(list(euro12))))

    # 将数据集中的列Team, Yellow Cards和Red Cards单独存为一个名叫discipline的数据框
    discipline = euro12[['Team', 'Yellow Cards', 'Red Cards']]
    print(discipline.head())

    # 对数据框discipline按照先Red Cards再Yellow Cards进行排序
    discipline.sort_values(by=['Yellow Cards', 'Red Cards'], ascending=[False, False], inplace=True)
    print(discipline.head())

    # 计算每个球队拿到的黄牌数的平均值
    # count_of_ycard = discipline["Yellow Cards"].sum()
    # print("得黄牌平均值 = {0}".format(count_of_ycard / discipline.Team.nunique()))
    print("得黄牌平均值 = {0}".format(discipline["Yellow Cards"].mean()))

    #  找到进球数Goals超过6的球队数据
    print("进球数Goals超过6的球队 = {0}".format(euro12[euro12["Goals"] > 6]))

    # 选取以字母G开头的球队数据
    print("以字母G开头的球队数据 :\n{0}".format(euro12[euro12["Team"].str.startswith("G")]))

    # 选取前7列
    print("选取前7列：")
    print(euro12.iloc[:, 0:7].head())

    # 选取除了最后3列之外的全部列
    print("最后3列之外的全部列：")
    print(euro12.iloc[:, 0:-3].head())

    # 找到英格兰(England)、意大利(Italy)和俄罗斯(Russia)的射正率(Shooting Accuracy)
    print("英格兰(England)、意大利(Italy)和俄罗斯(Russia)的射正率(Shooting Accuracy)：")
    print(euro12[euro12["Team"].isin(['England', 'Italy', 'Russia'])][["Team", "Shooting Accuracy"]])
