#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   pd_60ask.py
@Time    :   2019/10/31 10:58:03
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   pandas 60问


答案：
https://aistudio.baidu.com/aistudio/projectDetail/118930

'''
import pandas as pd
import numpy as np


data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']


def qz_4():
    """
    用data创建一个DataFramedf，索引是labels
    """
    df = pd.DataFrame(data=data, index=labels)
    return df


def qz_5():
    """
    显示此DataFrame及其数据的基本信息摘要。
    """
    # TODO 待实现
    pass


def qz_6():
    """
    返回DataFrame df的前三行.
    """
    # TODO 待实现
    pass


def qz_7():
    """
    从DataFramedf中选择animal和age列
    """
    # TODO 待实现
    pass


def qz_8():
    """
    8. 选择行[3, 4, 8] 与 列 ['animal', 'age']中的数据.
    """
    # TODO 待实现
    pass


def qz_9():
    """
    9. 把visits>3的行的内容筛出来.
    """
    # TODO 待实现
    pass


def qz_10():
    """
    10. 把age 缺失的行(例如age为 NaN)筛出来.
    """
    # TODO 待实现
    pass


def qz_11():
    """
    11. 把animal为cat 且 age小于3的行筛出来.
    """
    # TODO 待实现
    pass


def qz_12():
    """
    12. 把age大于2, 小于等于4的行都筛出来.
    """
    # TODO 待实现
    pass


def qz_13():
    """
    13. 把'f'行里的age改成1.5.
    """
    # TODO 待实现
    pass


def qz_14():
    """
    14. 把所有行的visits进行加总.
    """
    # TODO 待实现
    pass


def qz_15():
    """
    15. 计算df中每种动物的平均年龄.
    """
    # TODO 待实现
    pass


def qz_16():
    """
    16. 在df中新增一行, 名为k, 每列的值你随便填. 完成后, 再把k行删除.
    """
    # TODO 待实现
    pass


def qz_17():
    """
    17. 计算df中每种动物的个数.
    """
    # TODO 待实现
    pass


def qz_17():
    """
    18. 对df进行排序, 第一次使用age进行降序排序, 然后按照visits进行升序排序.
    """
    # TODO 待实现
    pass


def qz_18():
    """
    18. 对df进行排序, 第一次使用age进行降序排序, 然后按照visits进行升序排序.
    """
    # TODO 待实现
    pass


def qz_19():
    """
    19. 当前'priority'列包含值'yes'和'no'。 用布尔值替换此列内容：'yes'替换为'True'而'no'替换为'False'。
    """
    # TODO 待实现
    pass


def qz_20():
    """
    20. 在'animal'一列中, 将'snake'改为'python'.
    """
    # TODO 待实现
    pass


def qz_21():
    """
    21. 相同访问量(visits)的不同种类动物, 计算其age的平均值. 换言之, 每行是一种动物, 有一列是visits, 一列是平均年龄. (小提示: 使用透视表).
    """
    # TODO 待实现
    pass

# --------------------------------------------------------
# 中等难度：


def qz_22():
    """
    22. 设有一个DataFrame df, 其中列 'A'为整型. 例如:

    df = pd.DataFrame({'A': [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 7]})
    如何筛选出与上一行包含相同整数的行？
    """
    # TODO 待实现
    pass


def qz_23():
    """
    23. 设有一个数值型的DataFrame:

    df = pd.DataFrame(np.random.random(size=(5, 3))) # 一个 5x3 浮点型的frame
    把行中每个元素都减去本行平均值？
    """
    # TODO 待实现
    pass


def qz_24():
    """
    24. 假设您有一个10列实数的DataFrame，例如：

    df = pd.DataFrame(np.random.random(size=(5, 10)), columns=list('abcdefghij'))
    哪一列数字的总和最小？ （找到该列的标签。）
    """
    # TODO 待实现
    pass


def qz_25():
    """
    25. 计算DataFrame有多少个唯一行（即忽略所有重复的行）？
    """
    # TODO 待实现
    pass


def qz_26():
    """
    26. 你有一个由10列浮点数组成的DataFrame。 假设每行中恰好有5个条目是NaN值。 那么于DataFrame的每一行，找到第三个NaN值的那一列列名。
    （您应该返回一串列标签。）
    """
    # TODO 待实现
    pass

def qz_27():
    """
    27. 设某DataFrame, 有一列为group类型的'grps'和一数值类型的列'vals'。 例如：


    df = pd.DataFrame({'grps': list('aaabbcaabcccbbc'),
    'vals': [12,345,3,1,45,14,4,52,54,23,235,21,57,3,87]})
    对于每个group，找到三个最大值的总和。
    """
    # TODO 待实现
    pass


def qz_28():
    """
    28. DataFrame有两个整数列'A'和'B'。 A中的值介于1和100之间（含100）。 对于'A'中的每组10个连续整数（即(0,10)，(10,20)，...），计算列'B'中相应值的总和。
    """
    # TODO 待实现
    pass


# --------------------------------------------------------
# 难：


def qz_29():
    """
    29. 假设有一个DataFramedf，其中有一个整数列'X':

    df = pd.DataFrame({'X': [7, 2, 0, 3, 4, 2, 5, 0, 3, 4]})
    然后每个值向前数, 数到开头或数到0, 这么一个数, 组成新数列.
    """
    # TODO 待实现
    pass


def qz_30():
    """
    30. 假设有一个所有行和列都为纯数字的DataFrame。 将其3个最大值的行列索引位置组成一个新列表。
    """
    # TODO 待实现
    pass


if __name__ == "__main__":
    df = qz_4()
    print(df)
    # print(df.to_dict())
    # print(df.index)
    train_data = np.array(df)
    print(train_data.tolist())
