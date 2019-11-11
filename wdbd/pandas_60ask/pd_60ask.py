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

    有单元测试
    """
    df = pd.DataFrame(data=data, index=labels)
    return df


def qz_5():
    """
    显示此DataFrame及其数据的基本信息摘要。
    """
    df = qz_4()
    print(df.info())
    print(df.describe())


def qz_6():
    """
    返回DataFrame df的前三行.
    """
    df = qz_4()
    print(df.iloc[:3, :])   # iloc方式
    print(df.head(3))       # head方式


def qz_7():
    """
    从DataFramedf中选择animal和age列
    """
    df = qz_4()
    print(df.loc[:, ['animal', 'age']])
    print(df[['animal', 'age']])


def qz_8():
    """
    8. 选择行[3, 4, 8] 与 列 ['animal', 'age']中的数据.
    """
    # df.ix 已被废弃，只能用
    df = qz_4()
    print(df.loc[df.index[[3, 4, 8]], ['animal', 'age']])


def qz_9():
    """
    9. 把visits>3的行的内容筛出来.
    """
    df = qz_4()
    print(df)
    print(df[df['visits'] > 3])


def qz_10():
    """
    10. 把age 缺失的行(例如age为 NaN)筛出来.
    """
    df = qz_4()
    print(df)
    print(df[df['age'].isnull()])


def qz_11():
    """
    11. 把animal为cat 且 age小于3的行筛出来.
    """
    df = qz_4()
    print(df)
    print(df[(df['animal'] == 'cat') & (df['age'] < 3)])


def qz_12():
    """
    12. 把age大于2, 小于等于4的行都筛出来.
    """
    df = qz_4()
    print(df[(df['age'] <= 4) & (df['age'] >= 2)])
    print(df[df['age'].between(2, 4)])


def qz_13():
    """
    13. 把'f'行里的age改成1.5.
    """
    df = qz_4()
    print(df)
    df.loc['f', 'age'] = 1.5
    print(df)


def qz_14():
    """
    14. 把所有行的visits进行加总.
    """
    df = qz_4()
    print(df['visits'].sum())


def qz_15():
    """
    15. 计算df中每种动物的平均年龄.
    """
    df = qz_4()
    print(df[['animal', 'age']].groupby(by=['animal']).mean())
    print(df.groupby(by=['animal'])['age'].mean())


def qz_16():
    """
    16. 在df中新增一行, 名为k, 每列的值你随便填. 完成后, 再把k行删除.
    """
    df = qz_4()

    # TODO 待实现

    pass


def qz_17():
    """
    17. 计算df中每种动物的个数.
    """
    df = qz_4()
    print(df['animal'].value_counts())


def qz_18():
    """
    18. 对df进行排序, 第一次使用age进行降序排序, 然后按照visits进行升序排序.
    """
    df = qz_4()
    df.sort_values(by=['age', 'visits'], ascending=[False, True], inplace=True)
    print(df)


def qz_19():
    """
    19. 当前'priority'列包含值'yes'和'no'。 用布尔值替换此列内容：'yes'替换为'True'而'no'替换为'False'。
    """
    df = qz_4()
    df['priority'] = df['priority'].map({'yes': 'True', 'no': 'False'})
    print(df)




def qz_20():
    """
    20. 在'animal'一列中, 将'snake'改为'python'.
    """
    df = qz_4()
    # df['priority'] = df['priority'].map({'yes': 'True', 'no': 'False'})

    df.where(df['animal'] == 'snake', 'python', np.nan)


    print(df)


if __name__ == "__main__":
    qz_20()



def qz_21():
    """
    21. 相同访问量(visits)的不同种类动物, 计算其age的平均值. 换言之, 每行是一种动物, 有一列是visits, 一列是平均年龄. (小提示: 使用透视表).
    """
    # TODO 待实现
    pass

# --------------------------------------------------------
# 中等难度：


def qz_22():
    """    22. 设有一个DataFrame df, 其中列 'A'为整型. 例如:

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


def qz_31():
    """
    31. 给定一个DataFrame，其中包含一列group ID，列名为'grps'; 以及一列相应的整数值'vals'，将'vals'中的任何负值替换为对应group的平均值。
    """
    # TODO 待实现
    pass


def qz_32():
    """
    32. 在窗口大小为3的组上实现滚动均值，忽略NaN值。 例如，假设有如下DataFrame：


    >>> df = pd.DataFrame({'group': list('aabbabbbabab'),
    'value': [1, 2, 3, np.nan, 2, 3,
    np.nan, 1, 7, 3, np.nan, 8]})
    >>> df
    group value
    0 a 1.0
    1 a 2.0
    2 b 3.0
    3 b NaN
    4 a 2.0
    5 b 3.0
    6 b NaN
    7 b 1.0
    8 a 7.0
    9 b 3.0
    10 a NaN
    11 b 8.0
    目标就是算出这么一个数列


    0 1.000000
    1 1.500000
    2 3.000000
    3 3.000000
    4 1.666667
    5 3.000000
    6 3.000000
    7 2.000000
    8 3.666667
    9 2.000000
    10 4.500000
    11 4.000000
    例如: 组'b'的第一个大小为3的窗口具有值3.0，NaN和3.0 (分别是行2, 行3, 行5)，计算后新列中的值应为3.0, 因为只有两个非NaN值被用来计算平均值（3 + 3）/ 2
    """
    # TODO 待实现
    pass

# -----------------------------------------------------
# Series和DatetimeIndex使用日期时间创建和操作Series的练习


def qz_33():
    """
    33. 创建一个DatetimeIndex, 内容是2015年全部工作日. 然后用它来索引一列随机数。 我们称这个列为s。
    """
    # TODO 待实现
    pass


def qz_34():
    """
    34. 全部星期三对应s值的总和。
    """
    # TODO 待实现
    pass


def qz_35():
    """
    35. 求每个自然月s值的平均值.
    """
    # TODO 待实现
    pass


def qz_36():
    """
    36. 每4个连续自然月分成一组, 找到每组最大s值的对应日期.
    """
    # TODO 待实现
    pass


def qz_37():
    """
    37. 创建一个DateTimeIndex，包含2015年和2016年每个月的第三个星期四。
    """
    # TODO 待实现
    pass


# -------------------------------------
# 清理数据

# 假造的航班信息数据
df_fight = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm',
                                     'Budapest_PaRis', 'Brussels_londOn'],
                         'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
                         'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
                         'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
                                     '12. Air France', '"Swiss Air"']})


def qz_38():
    """
    38. FlightNumber列中的某些值丢失。 观察数字, 可知规律是逐行递增10，因此需要设置10055和10075。 填写这些缺失的数字，并使列成为整数列（而不是浮点数值列）。
    """
    # TODO 待实现
    pass


def qz_39():
    """
    39. From_To列如能拆成两个单独的列明显要更好！请使用下划线分隔符_来拆分每个字符串，并做成新的临时DataFrame。
    """
    # TODO 待实现
    pass


def qz_40():
    """
    40. 请注意, 在上一题中形成的临时DataFrame中, 城市名称的大小写是错乱的。请修改这些字符串, 保证只有第一个字母是大写的（例如“londON”应该变成“London”。）
    """
    # TODO 待实现
    pass


def qz_41():
    """
    41. 把df中的From_To一列删除, 然后把上一题生成的临时DataFrame添加到df里面去.
    """
    # TODO 待实现
    pass


def qz_42():
    """
    42. 在Airline一栏中，您可以看到航空公司名称前后出现了一些额外的标点符号。现在整理航空公司名称。例如 '(British Airways. )'应改为'British Airways'。
    """
    # TODO 待实现
    pass


def qz_43():
    """
    43.RecentDelays这一列的值, 在Dataframe里是一个列表. 问题来了, 我们希望第一个值自己有独立的一列, 第二个值也有自己的一列. 如果第N个值不存在, 则就写成NaN
这样扩展后的列表名叫delays, 放到DataFrame里面, 然后给每个列重新命名为 delay_1, delay_2, 等等. 然后把RecentDelays替换成delays
    """
    # TODO 待实现
    pass


# ---------------------------
# 多重索引

def qz_44():
    """
    44. 给定列表letters = ['A'，'B'，'C']和numbers = list（range（10）），用两个列表的乘积构造一个MultiIndex对象。然后使用它来索引一个随机数列。这个Series称为s。
    """
    # TODO 待实现
    pass


def qz_45():
    """
    45. 检查s的索引是否按字典顺序排序（这是MultiIndex正确工作的必要条件）。
    """
    # TODO 待实现
    pass


def qz_46():
    """
    45. 检查s的索引是否按字典顺序排序（这是MultiIndex正确工作的必要条件）。
    """
    # TODO 待实现
    pass


def qz_47():
    """
    47. 切分Seriess, 第一层级索引的切分点在B, 第二级索引的切分点是5.
    """
    # TODO 待实现
    pass


def qz_48():
    """
    48. s按第一级索引A, B, C进行分项求和, 结果如: [868, 110, 333].(分别对应A, B, C)
    """
    # TODO 待实现
    pass


def qz_49():
    """
    49. 假设sum() (或其他方法)压根儿没有level 这个参数, 那我们如何实现类似s.sum(level=1)的功能?
    """
    # TODO 待实现
    pass


def qz_50():
    """
    50. 问题: 交换MultiIndex的层级，所以我们有个索引（可能是字母，也可能是数字）。
    问题: 这个Series是否正确排序了: 如果没有正确排序, 请把它重排一下.
    """
    # TODO 待实现
    pass


# 扫雷
# 在扫雷网格中生成安全方块的数字难度：中等到高难
# 如果您曾经使用过旧版本的Windows，那么您很有可能玩过扫雷游戏。如果您不熟悉游戏，
# 那就想象有个一个个正方形格子：某些正方形下隐藏了一个地雷
# 如果点中一个地雷，你就立即输掉游戏。如果你点击一个安全的方块，则会看到一个数字，告诉你在该方块周围有多少个地雷。
# 获胜目标是点开网格中不包含地雷的所有方块。
# 在本节中，我们将制作一个DataFrame，其中包含扫雷游戏的必要数据：方块的坐标, 方块下是否有地雷以及相邻方块上的地雷数量。


def qz_51():
    """
    51. 假设我们开始玩扫雷, 地图是5行4列, 例如:
    X = 5
    Y = 4
    首先，生成一个包含两列的DataFramedf，'x'和'y'包含该网格的每个坐标。换句话说, DataFrame应该是这样：
    x y
    0 0 0
    1 0 1
    2 0 2
    """
    # TODO 待实现
    pass


def qz_52():
    """
    52. 在DataFramedf里创建一个新列, 其中是0（表示无雷）和1（表示地雷）。有地雷的概率大概是0.4。
    """
    # TODO 待实现
    pass


def qz_53():
    """
    53. 现在给这个名为'adjacent'(周边) 的DataFrame创建一个新列。该列内容就是每个格子相邻方块里的地雷数。
    """
    # TODO 待实现
    pass


def qz_54():
    """
    54. DataFrame里表示有地雷的那些行, 它们的'adjacent'列里面应该都是NaN值.
    """
    # TODO 待实现
    pass


def qz_55():
    """
    55. 最后，将DataFrame转换为一个网格, 里面都是周边方块地雷数：列是x坐标，行是y坐标。
    """
    # TODO 待实现
    pass


# -------------------------------
# 绘图

def qz_56():
    """
    56. Pandas与绘图库matplotlib高度集成，使得绘制DataFrames非常简便！在Notebook环境中绘图通常使用以下方式：
    import matplotlib.pyplot as plt
    %matplotlib inline
    plt.style.use('ggplot')
    matplotlib是绘图库，Pandas的绘图功能主要就靠它了，它通常别名为plt。
    ％matplotlib inline告诉Notebook这次绘图是内联图，而不用开个单独的窗口。
    ``plt.style.use（'ggplot'）''是一个流行的风格主题，它是基于R的ggplot包的样式。
    问题来了: 对于初学者，制作随机数据的散点图，但使用黑色X而不是默认标记。
    df = pd.DataFrame({"xs":[1,5,2,8,1], "ys":[4,2,1,9,6]})
    如果哪里被卡住了, 请查阅文档 !
    """
    # TODO 待实现
    pass


def qz_57():
    """
    57. DataFrame中的列也可修改颜色和大小.
    Bill一直在测算他的工作表现, 主要因素有工作时长, 心情好坏, 以及早上是否喝了咖啡。请使用下方dataFrame画出相关图。
    （提示：如果您觉得图看不清楚, 请尝试将那些Series乘以10）
    图表不一定非常漂亮：这不是数据可视化课程！

    df = pd.DataFrame({"productivity":[5,2,3,1,4,5,6,7,8,3,4,8,9],
    "hours_in" :[1,9,6,5,3,9,2,9,1,7,4,2,2],
    "happiness" :[2,1,3,2,3,1,2,3,1,2,2,1,3],
    "caffienated" :[0,0,1,1,0,0,0,0,1,1,0,1,0]})
    """
    # TODO 待实现
    pass


def qz_58():
    """
    58. 如果我们想要绘制多个内容怎么办？Pandas允许您传入matplotlib Axis对象，并且也返回一个Axis对象。

    具体要求，参考文档


    """
    # TODO 待实现
    pass


def qz_59():
    """
    59. 用随机数生成某天的股票交易数据，并汇总/重新格式化，然后统计每小时的开盘价，最高价，最低价和收盘价
    """
    # TODO 待实现
    pass


def qz_60():
    """
    60. 现在正确格式的数据已经有了，请使用上面的plot_candlestick（df）函数绘制对应的烛台图
    """
    # TODO 待实现
    pass
