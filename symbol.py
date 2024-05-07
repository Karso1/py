import ccxt

#全部交易所
'''
exchanges = ccxt.exchanges
for cexname in exchanges:
    print(cexname)
'''

'''''''''
# 创建OKX交易所的实例
exchange = ccxt.okx({
    'proxies': {'http': '127.0.0.1:7890', 'https': '127.0.0.1:7890' },
    #'apiKey': '您的API密钥',
    #'secret': '您的密钥',
    #'password': '您的交易所账户密码',
    'enableRateLimit': True,
    'options': {
        'defaultType': 'swap',  # 对于永续合约使用 'swap'
        # 'defaultType': 'futures',  # 对于期货合约使用 'futures'
    }
})
'''''''''


exchange = ccxt.binanceusdm({
    'proxies': {'http': '127.0.0.1:7890', 'https': '127.0.0.1:7890' },
    'timeout':15000,
    'rateLimit':50,
    'enableRatelimit':True
    })


'''''''''
exchange = ccxt.binance({
    'proxies': {'http': '127.0.0.1:7890', 'https': '127.0.0.1:7890' },
    'enableRateLimit': True,
    'rateLimit':1000,
    'options': {
        'defaultType': 'future'
    }
})
'''''''''

#cex data structer
'''''''''
print('cex id: ',exchange.id)
print('cex name: ',exchange.name)
print('是否有共有API： ',exchange.has['publicAPI'])
print('是否有私有API： ',exchange.has['privateAPI'])
print('支持的时间频率： ',exchange.timeframes)
print('最长的等待时间： ',exchange.timeout /1000)
print('访问频率（s）： ',exchange.rateLimit/1000)
print('交易所当前时间： ',exchange.iso8601(exchange.milliseconds()))
'''''''''

#加载市场数据 load_markets()
markets = exchange.load_markets()
# 打印所有支持的交易对
for symbol in markets.keys():
    print(symbol)

