# Python读写sqlite3数据库

- 数据库连接
- 事务处理（手动提交、回滚）
- 用with访问

## 基本访问

sqlite3有内存和文件两种模式，使用sqlite3包可以进行访问。

```python
db_path = r'src\main\sqlite3_dbs\test.db'
conn = sqlite3.connect(db_path)     # 访问数据库
cur = conn.cursor()                 # 获得游标

# 查询型
rs = cur.execute("select id, name from tb_test").fetchall()
# 返回值：[('001', 'Jack'), ('002', 'Mick')]

# 指令型
cur.execute("INSERT INTO tb_test (id, name) values ('001', 'Jack')")
cur.execute("INSERT INTO tb_test (id, name) values (?, ?)", ('002', 'Tom'))

```

## sqlite3的事务处理

sqlite3的conn对象支持commit、rollback操作。

下面是示例：

```python

    db_path = r'src\main\sqlite3_dbs\test.db'

    try:
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        # 准备数据
        cur.execute("DROP TABLE tb_test")
        cur.execute("CREATE TABLE tb_test ( id   VARCHAR      PRIMARY KEY, name VARCHAR (20) )")
        cur.execute("INSERT INTO tb_test (id, name) values ('001', 'Jack')")
        cur.execute("INSERT INTO tb_test (id, name) values ('002', 'Mick')")
        conn.commit()

        cur.close()
    except Exception as err:
        print('Something went wrong: ', str(err))
        conn.rollback()
        print('事务已回滚')
    finally:
        conn.close()
```

## 使用With访问

为方便使用，可将常用操作封装在一个DB对象内，下面是示例代码和使用示例：

```python
class SQLiteDb:
    """SQlite3数据库访问上下文
    """

    def __init__(self):
        self.db_path = r'src\main\sqlite3_dbs\test.db'
        self.conn = sqlite3.connect(self.db_path)
        self.cur = self.conn.cursor()
        # 准备原始数据

    def __str__(self):
        return "py sqlite数据库上下文管理器"

    def __enter__(self):
        # 返回类对象本身
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cur.close()
        self.conn.close()
        print("连接已关闭")

    # 查询单条数据
    def query_one(self, sql):
        try:
            self.cur.execute(sql)
            res = self.cur.fetchone()
            return res
        except Exception as e:
            print("查询出错，", e)


if __name__ == "__main__":
    # 使用示例
    with SQLiteDb() as db:
        print(db.query_one("select name from tb_test"))
```
