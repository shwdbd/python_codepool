#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test_pd_60ask.py
@Time    :   2019/10/31 14:30:31
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   Pandas 60问 单元测试
'''
import unittest
import pandas as pd
import numpy as np
from pandas.util.testing import assert_frame_equal
import wdbd.pandas_60ask.pd_60ask as impl


class Test_qz_4(unittest.TestCase):

    def test_qz_4(self):
        data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
                'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
                'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
                'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
        labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
        df_sample = pd.DataFrame(data=data, index=labels)
        df = impl.qz_4()
        assert_frame_equal(df_sample, df)
