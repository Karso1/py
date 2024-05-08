import backtrader as bt
import ccxt
import pandas as pd
from datetime import datetime
import backtrader.indicators as btind

exchange = ccxt.okx({
    'proxies': {'http': '127.0.0.1:7890', 'https': '127.0.0.1:7890' },
    'enableRateLimit': True,
    'options': {
        'defaultType': 'swap'
    }
})

# 定义一个函数来下载OKX的数据
def download_okx_data(symbol, timeframe, since, limit):
    exchange = ccxt.okx()
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe, since, limit)
    df = pd.DataFrame(ohlcv, columns=['datetime', 'open', 'high', 'low', 'close', 'volume'])
    df['datetime'] = pd.to_datetime(df['datetime'], unit='ms')
    return df

# 下载PEPE代币的数据
symbol = 'PEPE/USDT'  # 请根据实际交易对进行修改
timeframe = '1m'  # 时间间隔
since = exchange.parse8601('2024-05-07T00:00:00Z')  # 开始日期
limit = 1440  # 获取的数据点数量

df = download_okx_data(symbol, timeframe, since, limit)

# 转换为Backtrader的数据格式
data = bt.feeds.PandasData(dataname=df)

# 创建Cerebro引擎
cerebro = bt.Cerebro()

# 添加数据到Cerebro
cerebro.adddata(data)

#策略
'''''''''
class Strategy(bt.Strategy):
    params = (
        ('rsi_period', 14),
        ('bollinger_period', 20),
        ('bollinger_dev', 2),
        ('printlog', False),
    )

    def log(self, txt, dt=None):
        #日志函数，用于记录策略的执行情况
        if self.params.printlog:
            dt = dt or self.datas[0].datetime.date(0)
            print(f'{dt.isoformat()}, {txt}')

    def __init__(self):
        # 初始化指标
        self.rsi = btind.RSI(self.data.close, period=self.params.rsi_period)
        self.bollinger = btind.BollingerBands(self.data.close, period=self.params.bollinger_period,
                                              devfactor=self.params.bollinger_dev)

    def next(self):
        # 检查是否存在未完成的订单
        if self.order:
            return

        # 检查是否持有仓位
        if not self.position:
            if self.rsi < 30 and self.data.close < self.bollinger.lines.bot:
                # RSI 小于 30 且收盘价低于布林带下轨，买入信号
                self.order = self.buy()
                self.log('买入单执行, %.2f' % self.data.close[0])
        else:
            if self.rsi > 70 and self.data.close > self.bollinger.lines.top:
                # RSI 大于 70 且收盘价高于布林带上轨，卖出信号
                self.order = self.sell()
                self.log('卖出单执行, %.2f' % self.data.close[0])

    def stop(self):
        self.log('(RSI Period %2d, Bollinger Period %2d, Bollinger Deviation %2d) 最终资产价值: %.2f' %
                 (self.params.rsi_period, self.params.bollinger_period, self.params.bollinger_dev,
                  self.broker.getvalue()), dt=self.datas[0].datetime.date(0))
'''''''''
class RSIStrategy(bt.Strategy):
    params = (
        ('rsi_period', 14),
        ('lowerband', 30),
        ('upperband', 70),
    )

    def __init__(self):
        # 初始化指标
        self.rsi = btind.RSI(self.data.close, period=self.params.rsi_period)

    def next(self):
        # 检查是否持有仓位
        if not self.position:
            if self.rsi < self.params.lowerband:
                # RSI 小于 30，买入信号
                self.buy()
        else:
            if self.rsi > self.params.upperband:
                self.sel()
                #000RSI 大于 70
# 添加策略到Cerebro
cerebro.addstrategy(Strategy)

# 设置初始资本
cerebro.broker.setcash(100)

# 设置交易单位大小为账户总资金的100%
cerebro.addsizer(bt.sizers.PercentSizer, percents=100)

# 假设杠杆比例为20倍
leverage = 20
# 设置保证金要求。如果杠杆是10倍，保证金就是头寸价值的1/10。
cerebro.broker.set_margin(margin=1 / leverage)

# 假设基础手续费率为0.05%
commission_rate = 0.0005
# 设置手续费，这里假设买卖手续费相同
cerebro.broker.setcommission(commission=commission_rate, margin=1 / leverage, mult=leverage)

# 如果手续费会随着杠杆放大，可以在计算手续费时加上杠杆比例
# 例如，如果手续费是基于杠杆后的头寸价值计算的，可以不设置mult参数，因为Backtrader默认就是基于整个头寸计算手续费

if __name__ == '__main__':
    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())
    cerebro.run()  # 运行策略
    print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
    cerebro.plot()  # 绘制图表