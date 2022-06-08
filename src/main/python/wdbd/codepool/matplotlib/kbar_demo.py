#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   kbar_demo.py
@Time    :   2020/08/11 21:27:34
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   绘制K线图的示例
'''
import matplotlib.pyplot as plt             # 导入画图模块
from matplotlib.pylab import date2num       # 导入日期到数值一一对应的转换工具
from dateutil.parser import parse           # 导入转换到指定格式日期的工具
# import mpl_finance as mpf                   # 导入 mpl_finance 模块
import mplfinance as mpf

plt.rcParams['font.family'] = 'SimHei'      # 设置字体
fig, ax = plt.subplots()                    # 创建图片和坐标轴
fig.subplots_adjust(bottom=0.2)             # 调整底部距离
ax.xaxis_date()                             # 设置X轴刻度为日期时间
plt.xticks(rotation=45)                     # 设置X轴刻度线并旋转45度
plt.yticks()                                # 设置Y轴刻度线
plt.title("股票代码 ** K线图")               # 设置图片标题
plt.xlabel("时间")                          # 设置X轴标题
plt.ylabel("股价（元）")                        # 设置Y轴标题
plt.grid(True, 'major', 'both', ls='--', lw=.5, c='k', alpha=.3)  # 设置网格线
data_list_ = [(date2num(parse(str(20181110))), 10, 20, 5, 15)]
# 股票数据，格式是往列表里添加元组, 每个元组代表一个股票信息。其中元组的格式是（日期，开盘价，最高价，最低价，收盘价）
# mpf.candlestick_ohlc(ax, data_list, width=1.0,
#                      colorup='r', colordown='green', alpha=1)

mpf.plot(data_list_)

# 设置利用mpf画股票K线图
plt.show()  # 显示图片
# plt.savefig("K线.png") # 保存图片
plt.close()  # 关闭plt，释放内存
