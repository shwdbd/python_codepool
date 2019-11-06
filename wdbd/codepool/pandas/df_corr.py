#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   df_corr.py
@Time    :   2019/11/06 13:28:37
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   corr 统计数据相关性函数

计算相关系数，返回不同列数值之间相关系数的矩阵

如果 相关系数 == 1，则两者绝对相关（自己和自己的相关系统等于1）
如果 相关系数 <> 1，则abs(相关系数)越小越相关，越大越不相关
相关系数>0，则两者正相关 y= 3x +2；
相关系数<0，则两者负相关 y=-6x+2;

'''
import pandas as pd
import numpy as np


def demo_corr():
    """
    计算 三组数据之间的两两相关性
    """
    sample_size = 200  # 样本空间
    rdn_data = np.random.randint(low=1, high=10, size=(sample_size, 3))
    # print(rdn_data)
    df = pd.DataFrame(rdn_data, columns=['A', 'B', 'C'])
    # print(df.head())
    # 显示三组数据之间的一致性
    print(df.corr().round(2))


if __name__ == "__main__":
    demo_corr()
