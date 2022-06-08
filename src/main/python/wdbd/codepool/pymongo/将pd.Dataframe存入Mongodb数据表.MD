# 将pd.Dataframe存入Mongodb数据表

由于pymongo提供InsertOne对象，其接受{'字段': 值, '字段2': 值}的dict类型参数

所以只要把dataframe转换成上面的dict类型就可以实现。通常这样实现：

```python
    data = {'col_1': [3, 2, 1, 0], 'col_2': ['a', 'b', 'c', 'd']}
    df = pd.DataFrame.from_dict(data)
    print(df)
    print(df.to_dict(orient='records'))
    # [{'col_1': 3, 'col_2': 'a'}, {'col_1': 2, 'col_2': 'b'}, {'col_1': 1, 'col_2': 'c'}, {'col_1': 0, 'col_2': 'd'}]
```

