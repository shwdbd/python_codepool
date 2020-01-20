#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   np_sign.py
@Time    :   2019/11/05 17:22:14
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   np.sign 函数示例

返回给定数列值大于零或小于零的sign

API DOC:
https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.sign.html

'''

import numpy as np
import pandas as pd


def demo_sign_where():
    # 判断dataframe 大于零，小于零，和0
    df = pd.DataFrame([12, -45, 0, 13])
    print(np.sign(df))

    # 判断单个数字
    print(np.sign(12))


if __name__ == "__main__":
    demo_sign_where()
