# Config配置文件读写

## 示例代码清单

|文件|说明|
|--|--|
|cfg_demo.py|按sestion读取配置文件|

## config配置文件的特征

- config是按“键值”配对存放信息的文本文件；
- 其内容由若干组option组成，option可组成section
- 当前目录下demo_config.cfg是典型的配置文件

## 读取config文件

- 可以使用 cf.read(FILE, encoding="UTF-8") 读取特定文件的内容，并返回一个cf对象
- cf.get(...)返回的是value的字符串，可以通过getint, getfloat, getboolean返回其他格式内容；
- cf.sections()返回所有section的名称list

## 更新config文件

- 通过read得到cf对象后，可以通过set函数设置option的值，包括新增option
- cf.add_section可以新增一个section
- 最后通过cf.write(open(new_file, mode="w", encoding="UTF-8"))写入（更新）到文件中
