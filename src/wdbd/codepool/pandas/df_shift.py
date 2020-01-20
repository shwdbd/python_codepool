#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   df_shift.py
@Time    :   2019/11/12 13:53:59
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   df.shift 序列升降函数


'''
import pandas as pd


def stock_price_shift():
    """
    股价收益率计算示例
    """
    data = pd.DataFrame(
        {'date': ['D1', 'D2', 'D3', 'D4', 'D5'],
         'price': [1, 2, 3, 4, 5],
         }
    )
    print(data)
    print(data.shift(1))    # 往下移动一行



if __name__ == "__main__":
    stock_price_shift()
