#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo_1.py
@Time    :   2019/12/06 10:01:57
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   绘制最简单的y=2x+1的图形
'''
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']

# 生成数据
df = pd.DataFrame({'x': np.arange(10)})
df['y'] = 2*df['x'] + 1
print(df)

# 绘制图形
plt.figure(figsize=(6, 6))
plt.title('中文标题 Fig title')
plt.plot(df['x'], df['y'])
plt.show()
plt.savefig('demo_1.png')   # 保存成文件
