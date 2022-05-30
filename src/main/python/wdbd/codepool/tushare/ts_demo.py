import tushare as ts
import pandas as pd


token = "341d66d4586929fa56f3f987e6c0d5bd23fb2a88f5a48b83904d134b"


def get_api():
    """ tushare连接，失败返回None """
    try:
        ts.set_token(token)
        return ts.pro_api()
    except Exception as err:
        print("Tuhare访问错误, {0}".format(err))
        return None


def print_result(df: pd.DataFrame):
    """ 回显结果 """
    if df is None:
        print("未取到数据")
        return

    print(df.shape)
    print(df.head())


def test_trade_cal():
    """ 交易日历 """
    # 26.trade_cal 交易日历
    # df = get_api().trade_cal(exchange='SZSE', start_date='20211118', end_date='20211122')
    # df = get_api().trade_cal(exchange='CFFEX').head(1)
    # print(df)
    # df = get_api().trade_cal(exchange='CFFEX').tail(1)
    # df = get_api().trade_cal(exchange='SZSE').tail()
    df = get_api().trade_cal(exchange='SZSE')
    print(df.head(1))
    print(df.tail(1))


def test_stock_basic():
    """ 股票列表 """
    
    # 全数量
    df = get_api().stock_basic()
    print(df.shape)
    
    # 是否有北交所数据
    print(df["market"].unique())    # ['主板' '中小板' '创业板' '北交所' '科创板' 'CDR']
    print(df[df["market"]=='北交所'])
    
    # 市场类别（market）区分不同板块
    

if __name__ == "__main__":
    # api = get_api()
    # print(api)

    # api接口尝试

    # # 25.stock_basic 股票列表
    # df = get_api().stock_basic()

    # # 100.namechange 股票曾用名
    # df = get_api().namechange(ts_code='600016.SH')

    # # 104.hs_const 沪深股通成份股
    # df = get_api().hs_const(hs_type='SH', is_new='0')

    # 回显
    print_result(test_stock_basic())
