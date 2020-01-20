#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   np_where.py
@Time    :   2019/11/05 17:09:24
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   np.where 函数示例

where(条件, 是的值, 否的值)

 API DOC:
 https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.where.html

'''
import numpy as np
import pandas as pd


def demo_np_where():
    # 示范：找出price大于0.5的数设置1， 否则设置-1
    dict_data = {
        'date': pd.date_range('20190101', periods=10),
        'price': np.random.rand(10)
    }
    data = pd.DataFrame(dict_data)
    data.set_index('date', inplace=True)
    # 使用:
    data['position'] = np.where(data['price'] > 0.5, 1, -1)
    print(data)


if __name__ == "__main__":
    demo_np_where()
