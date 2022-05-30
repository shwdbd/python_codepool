# Tushare API 笔记

## 一、沪深股票 - 基础数据

### 25. 股票列表（stock_basic）

- 文档：[官方文档](https://www.tushare.pro/document/2?doc_id=25)
- 总数量大概在4633左右
- 

### 26.交易日历（trade_cal）

- 文档：[官方文档](https://www.tushare.pro/document/2?doc_id=26)
- 默认交易所：上交所
- 尚未有"北交所"数据（截止2021-11-22）
- 交易所代码，以及开始日期如下：
  - SSE上交所，19901219
  - SZSE深交所，19910703
  - CFFEX中金所,20060908
  - SHFE上期所,19910528
  - CZCE郑商所,19901012
  - DCE大商所,19930301
  - INE上能源,20170523
- 数据自1991-01-01开始，当当前年末12-31结束

### 100.namechange 股票曾用名

- 每个股票至少有一天记录
- 如果最后一次改名，则end_date、ann_date为None
