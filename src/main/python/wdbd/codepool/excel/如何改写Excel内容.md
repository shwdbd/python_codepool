# 如何改写Excel文件内容

工作中常有“改写现有Excel文件中部分内容”的需求场景，比如生成数据报表等。

目前有两个最常用的python类库：

- openpyxl 只能用于excel2003+版本（即.xlsx文件）
- xlrd/xlwr 多用于excel2003以下版本（即.xls文件）

我推荐使用openpyxl类库，理由如下：

- openpyxl适用于新版本的excel表；
- 有更丰富、功能强大的API；
- xlrd无法填充单元格，只能覆写单元格内容，这样就会丢失原有的单元格样式

## 代码示例

在 excel_fillin.py 中有两个示范函数，分别利用 openpyxl 和 xlrd 实现了对现有excel文件内容的修改
