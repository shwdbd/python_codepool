#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_1.py
@Time    :   2019/12/06 10:01:57
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   绘制多个图表Figure

多个图标需要顺序执行
title要写在plt.figure下

'''
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']

# 生成数据
df = pd.DataFrame({'x': np.arange(10)})
df['y1'] = 2*df['x'] + 1
df['y2'] = df['x']**2
print(df)

# 绘制图形

plt.figure(num=3, figsize=(6, 6))   # num是编号
plt.plot(df['x'], df['y1'])
plt.title('一次函数')
# plt.savefig('c:\\foo\\1.png')

plt.figure(figsize=(6, 6))
plt.plot(df['x'], df['y2'])
plt.title('二次函数')

plt.show()
