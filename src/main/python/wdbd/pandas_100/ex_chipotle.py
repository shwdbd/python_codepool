#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   ex_chipotle.py
@Time    :   2021/03/23 16:49:47
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   探索Chipotle快餐数据
'''
import pandas as pd


if __name__ == "__main__":
    url = "src/wdbd/pandas_100/data/chipotle.tsv"

    # 加载数据
    chipo = pd.read_csv(url, sep='\t')

    # 查看前10行内容
    print("前10行数据：")
    print(chipo.head(10))

    # 数据集中有多少个列(columns)
    print("数据集中有多少个列 = {0}".format(chipo.shape[1]))

    # 打印出全部的列名称
    print("打印出全部的列名称 = {0}".format(list(chipo)))

    # 数据集的索引是怎样的
    print(chipo.index)      # RangeIndex(start=0, stop=4622, step=1)

    # 被下单数最多商品(item)是什么?
    df = chipo[['item_name', 'quantity']].groupby(['item_name']).agg({'quantity': sum})
    df.sort_values(["quantity"], inplace=True, ascending=False)
    print(df.iloc[0:1])

    # 在item_name这一列中，一共有多少种商品被下单？
    print("下单商品数量 = {0}".format(chipo.item_name.nunique()))

    # 在choice_description中，下单次数最多的商品是什么？
    df = chipo[['choice_description', 'quantity']].groupby(['choice_description']).count()
    df.sort_values(['quantity'], ascending=False, inplace=True)
    print(df.iloc[0:1])
    # print(chipo['choice_description'].value_counts().head())

    # 一共有多少商品被下单？
    print("下单的商品数量 = {0}".format(chipo.quantity.sum()))

    # 将item_price转换为浮点数
    change_to_float = lambda x: float(x[1:-1])  # $2.39
    chipo.item_price = chipo.item_price.apply(change_to_float)
    print(chipo.item_price.head())

    # 在该数据集对应的时期内，收入(revenue)是多少
    chipo["revenue"] = round(chipo["item_price"] * chipo["quantity"], 2)
    print("总收益 = {0}".format(chipo.revenue.sum()))

    # 在该数据集对应的时期内，一共有多少订单
    print("总订单数量 = {0}".format(chipo.order_id.nunique()))

    # 每一单(order)对应的平均总价是多少？
    chipo['sub_total'] = round(chipo['item_price'] * chipo['quantity'], 2)
    df = chipo[['order_id', 'sub_total']].groupby(['order_id']).agg({'sub_total': sum})
    print("每一单(order)对应的平均总价 = {0}".format(df.sub_total.mean()))

    # 一共有多少种不同的商品被售出？
    # df = chipo['item_name'].groupby(['item_name'])
    print("总共销售的商品种类 = {0}".format(chipo.item_name.nunique()))

    print("END")
