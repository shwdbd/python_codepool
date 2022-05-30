# 使用matplotlib绘图

本文是python语言下使用matplotlib包绘图的整理笔记，适用于python开发者阅读。

本文尽量使用python代码说明matplotlib包的使用，所有代码都可执行。

[TOC]

## 第一个图形

本节用一个折线图的示例代码，说明matplotlib的简单用法。

```python
import numpy as np
from matplotlib import pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']


def draw():
    """绘制图形
    """
    # 准备画布
    plt.figure(figsize=(6, 6))
    plt.title('简单折线图')

    # 准备数据点
    x = np.linspace(0, 50, 10)   # 0-2中间50个点
    plt.plot(x, x, label="x")
    plt.plot(x, 3*x, label="3x")

    # 显示
    plt.show()
    # plt.savefig('demo_1.png')   # 保存成文件


if __name__ == "__main__":
    draw()
```

说明：

- np.linspace能生成一组数字
- plt.plot是绘制折线图的函数，第一个参数为x坐标，第二个参数为y坐标

## 基本概念

### matplob的安装

### 图形的主要部件

### 多个图形并列

每个画布（figure）都可以由若干个子图形(subplot)构成。
下面代码，展示了如何在一个figure上布局若干个subplot的代码：

```python
# 三个图标，在一行排列的情况
names = ['组A', '组B', '组C']
values = [1, 10, 100]

plt.subplot(131)            # 左
plt.bar(names, values)
plt.subplot(132)            # 中
plt.scatter(names, values)
plt.subplot(133)            # 右
plt.plot(names, values)
```

说明：

1. subplot由三个参数，plt.subplot(1, 3, 1) 和 plt.subplot(131) 是一样的，表示在第一排共有三列排在第一列；
2. 三个整数是行数、列数和索引值，子图将分布在行列的索引位置上。索引从1开始，从右上角增加到右下角
3. 需要注意的是所有的数字不能超过10。

### 线条的样式

### 图例

### 坐标轴

### 另存为图片

## 常用图形

### 折线图

### Bar柱状图

### Pie饼图

## 金融绘图

### mplfinance包介绍和安装

### 第一个K线图
