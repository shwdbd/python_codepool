# Python Mock 笔记

Mock就是模拟代码，可以Mock一个类、一个函数、一个属性，设置一套体系。

Python在unittest.mock中提供了Mock的机制。

本文对Mock的简单使用进行的示例，并通过数据库的Mock，解决数据库类应用单元测试的问题。

## 简单Mock

Mock对象可以模拟接口代码，因为Mock对象的return_value和side_effect两个特征。

### return_value

### side_effect

## 使用patch

## 数据库Mock

示例代码：

- dbconn.py 数据库连接
- db_app.py 应用代码，使用到dbconn.py
- test_db 单元测试代码，使用到monogomock组件
