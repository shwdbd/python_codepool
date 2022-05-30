import mplfinance as mpf
import matplotlib as mpl
from cycler import cycler
import pandas as pd
import matplotlib.pyplot as plt


def load_data() -> pd.DataFrame:
    """读取股票数据文件
    """
    data_file = "c:/temp/stock - all/000001.SZ.csv"

    try:
        # 用pandas组件读取
        use_cols = ['trade_date', 'open', 'high', 'low', 'close', 'vol']
        df = pd.read_csv(data_file, encoding="UTF-8",
                         dtype={'trade_date': str}, usecols=use_cols)
        df.rename(
            columns={
                'trade_date': 'Date', 'open': 'Open',
                'high': 'High', 'low': 'Low',
                'close': 'Close', 'vol': 'Volume'},
            inplace=True)
        df['Date'] = pd.to_datetime(df['Date'])

        # 日期过滤
        df = df[df["Date"] >= '20200101']
        df = df[df["Date"] <= '20200131']

        # 排序
        df.sort_values(by="Date", inplace=True,
                       ascending=True, ignore_index=True)

        # 设置index
        df.set_index("Date", inplace=True)

        return df
    except Exception as err:
        raise IOError("读取股价csv文件失败， {0}".format(str(err)))


def draw():
    """绘制K线图
    """
    df = load_data()

    # 设置基本参数
    # type:绘制图形的类型，有candle, renko, ohlc, line等
    # 此处选择candle,即K线图
    # mav(moving average):均线类型,此处设置7,30,60日线
    # volume:布尔类型，设置是否显示成交量，默认False
    # title:设置标题
    # y_label:设置纵轴主标题
    # y_label_lower:设置成交量图一栏的标题
    # figratio:设置图形纵横比
    # figscale:设置图形尺寸(数值越大图像质量越高)
    kwargs = dict(
        type='candle',
        mav=(7, 30, 60),
        volume=True,
        title='\nA_stock candle_line',
        ylabel='OHLC Candles',
        ylabel_lower='Shares\nTraded Volume',
        figratio=(15, 10),
        figscale=5)

    # 设置marketcolors
    # up:设置K线线柱颜色，up意为收盘价大于等于开盘价
    # down:与up相反，这样设置与国内K线颜色标准相符
    # edge:K线线柱边缘颜色(i代表继承自up和down的颜色)，下同。详见官方文档)
    # wick:灯芯(上下影线)颜色
    # volume:成交量直方图的颜色
    # inherit:是否继承，选填
    mc = mpf.make_marketcolors(
        up='red',
        down='green',
        edge='i',
        wick='i',
        volume='in',
        inherit=True)

    # 设置图形风格
    # gridaxis:设置网格线位置
    # gridstyle:设置网格线线型
    # y_on_right:设置y轴位置是否在右
    s = mpf.make_mpf_style(
        gridaxis='both',
        gridstyle='-.',
        y_on_right=False,
        marketcolors=mc)

    # 设置均线颜色，配色表可见下图
    # 建议设置较深的颜色且与红色、绿色形成对比
    # 此处设置七条均线的颜色，也可应用默认设置
    mpl.rcParams['axes.prop_cycle'] = cycler(
        color=['dodgerblue', 'deeppink',
               'navy', 'teal', 'maroon', 'darkorange',
               'indigo'])

    # 设置线宽
    mpl.rcParams['lines.linewidth'] = .5

    # 图形绘制
    # show_nontrading:是否显示非交易日，默认False
    # savefig:导出图片，填写文件名及后缀
    # mpf.plot(df,
    #          **kwargs,
    #          style=s,
    #          show_nontrading=False,
    #          savefig='A_stock-_candle_line.jpg')
    mpf.plot(df,
             **kwargs,
             style=s,
             show_nontrading=False)
    plt.show()


if __name__ == "__main__":
    df = load_data()
    print(df.head())

    draw()