# Mongodb常用命令集

本文档做为Mongodb shell命令的索引查询工具

## 常用指令

### INSERT

### FIND


```shell
# 
```


#### 查询条件

#### 子文档查询

#### 数组搜索

#### 控制返回字段

### UPDATE

### DELETE

- remove 命令需要配合查询条件使用
- 可以指定{}空条件，删除全部记录

shell示例：

```mongodb
# remove语法
# db.<集合>.remove(<条件>)

# 删除全部
db.order.remove({})

# 删除a=1的记录
db.order.remove({a, 1})

```

### 表Drop

### 索引

- 新建索引
- 查询索引

## 聚合查询

与SQL的对照：

1. where - $match
2. as - $project
3. order by - $sort
4. group by - $group
5. skip/limit - $skip/$limit
6. left join out 左外连接 - $lookup

### 运算符

$unwind 数组展开操作
$bucket 数值分组
$facet 多维度分组
