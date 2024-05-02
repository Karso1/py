import ccxt
import backtrader as bt
import pandas as pd


#初始化交易所
exchange = ccxt.binance({
    'proxies': {'http': '127.0.0.1:7890', 'https': '127.0.0.1:7890'},
    'rateLimit':1000,
    'enableRateLimit':True,
})

# 获取历史数据
bars = exchange.fetch_ohlcv('DOGE/USDT', timeframe='1m', since=exchange.parse8601('2024-05-01T00:00:00Z'))


# 转换为Pandas DataFrame
df = pd.DataFrame(bars, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
df.set_index('timestamp', inplace=True)

# 创建Backtrader数据源
class CCXTData(bt.feeds.PandasData):
    params = (
        ('datetime', None),
        ('open', 'open'),
        ('high', 'high'),
        ('low', 'low'),
        ('close', 'close'),
        ('volume', 'volume'),
        ('openinterest', None),
    )

data_feed = CCXTData(dataname=df)

# 创建Cerebro实例
cerebro = bt.Cerebro()

#rsi
# RSI策略定义
class RsiStrategy(bt.Strategy):
    params = (
        ('rsi_period', 7),
        ('rsi_overbought', 60),
        ('rsi_oversold', 40),
        ('order_percentage', 1),#下单所占比例
        ('stop_loss_perc',0.01),#止损
        ('take_profit_perc',0.025),
        ('ticker', 'DOGE')
    )

    def __init__(self):
        # 初始化RSI指标
        self.rsi = bt.indicators.RSI(self.data.close, period=self.params.rsi_period)
        self.order = None
        # 初始化交易统计信息
        self.total_trades = 0

    def next(self):
        if self.order:
            return #如果有挂单，不进行新的交易

        if not self.position:   #如果没有持仓
            if self.rsi<self.params.rsi_oversold:   #rsi小于超卖，买入
                self.order = self.buy()
                print(f"多：价格={self.data.close[0]},时间={self.data.datetime.datetiem()}")
            elif self.rsi>self.params.rsi_overbought:#rsi大于超买，卖出
                self.order = self.sell()
                print(f"空：价格={self.data.close[0]},时间={self.data.datetime.datetime()}")

        else:#如果有持仓
            if self.position.size > 0 and self.rsi>self.params.rsi_overbought:#多头持仓且超买
                self.order = self.close()
                print(f"平多：价格={self.data.close[0]},时间={self.data.datetime.datetime()}")
            elif self.position.size < 0 and self.rsi <self.params.rsi_oversold:#空头持仓且rsi超卖
                self.order = self.close()
                print(f"平空：价格={self.data.close[0]},时间={self.data.datetime.datetime()}")

# 添加策略
cerebro.addstrategy(RsiStrategy)

# 添加数据
cerebro.adddata(data_feed)

# 设置初始资金
cerebro.broker.setcash(100)

#设置合约交易的手续费和杠杆
#cerebro.broker.setcommission(commission=0.02,leverage=20)

# 添加Sizer，以便自动决定买卖数量
cerebro.addsizer(bt.sizers.FixedSize, stake=10)

# 运行策略
cerebro.run()

# 获取最终资产总值
print(f'Final Portfolio Value: {cerebro.broker.getvalue():.2f}')

# 绘图
cerebro.plot()