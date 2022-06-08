#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   使用apply执行条件查询.py
@Time    :   2022/01/25 10:53:35
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   使用DataFrame.apply执行条件查询

代码说明:
查询返回value为双数的记录

'''
import pandas as pd


def is_even_number(n: int) -> bool:
    """ 判断是否偶数 """
    if n % 2 == 0:
        return True
    else:
        return False


def get_data() -> pd.DataFrame:
    data = {
        'id': range(1, 10),
        'value': range(1, 10)
    }
    df = pd.DataFrame(data)
    return df


if __name__ == "__main__":
    df = get_data()
    print(df)
    # 过滤：
    df_1 = df.loc[df["value"].apply(is_even_number)]
    print(df_1)
