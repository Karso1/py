# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 13:57:27 2024

@author: Administrator
"""

import ccxt


#get the cex list
exchange_list =ccxt.exchanges


print(exchange_list)

#initial cex
bn_exchange = ccxt.binance({
    'proxies': {'http': '127.0.0.1:7890', 'https': '127.0.0.1:7890' },
    'timeout':15000,
    'enableRatelimit':True
    })




#cex data structer
print('cex id: ',bn_exchange.id)
print('cex name: ',bn_exchange.name)
print('是否有共有API： ',bn_exchange.has['publicAPI'])
print('是否有私有API： ',bn_exchange.has['privateAPI'])
print('支持的时间频率： ',bn_exchange.timeframes)
print('最长的等待时间： ',bn_exchange.timeout /1000)
print('访问频率（s）： ',bn_exchange.rateLimit/1000)
print('交易所当前时间： ',bn_exchange.iso8601(bn_exchange.milliseconds()))

#加载市场数据 load_markets()
bn_markets = bn_exchange.load_markets()
#支持的交易对
list(bn_markets.keys())




print('------------')

print('------------')

print('------------')


symbol = 'SOL/USDT'
#获取指定交易对市场信息
sol_usdt_market = bn_markets[symbol]

sol_usdt_market

#获取单个交易对ticker数据
ticker_data = bn_exchange.fetchTicker(symbol)
ticker_data

print('Ticker时刻：',ticker_data['datetime'])
print('Ticker价格：',ticker_data['last'])


'''
#获取多个交易对ticker数据
tickers_data = bn_exchange.fetchTickers(['BTC/USDT','SOL/USDT'])
ticker_data
print('Tickers时刻：',ticker_data['datetime'])
print('Tickers价格：',ticker_data['last'])
'''


#时间转换
print('ticker数据开始时间：',bn_exchange.iso8601(ticker_data['info']['openTime']))
print('ticker数据结束时间：',bn_exchange.iso8601(ticker_data['info']['closeTime']))









#交易委托账本数据获取
bn_exchange.fetch_order_book(symbol)

#上一次访问cex的时间
bn_exchange.last_response_headers['Date']


orderbook = bn_exchange.fetch_order_book(symbol)

#最高买价
bid = orderbook['bids'][0][0] if len (orderbook['bids']) > 0 else None


#最高卖价
ask = orderbook['asks'][0][0] if len(orderbook['asks']) > 0 else None

#价差
spread = (ask-bid)if (bid and ask) else None

#市场行情
print('buy:{:.2f},sell:{:.2f},gap:{:.2f}'.format(bid,ask,spread))

print('-----------------------------')
print('-----------------------------')
print('-----------------------------')



#get  k line   data

'''
if bn_exchange.has['fetchOHLCV']:
    print(bn_exchange.fetch_ohlcv(symbol,timeframe='1d'))
'''
    
import pandas as pd
if bn_exchange.has['fetchOHLCV']:
    kline_data =pd.DataFrame(bn_exchange.fetch_ohlcv(symbol,timeframe='1m'))
    kline_data.columns = ['Datetime','Open','High','Low','Close','Vol']
    kline_data['Datetime'] = kline_data['Datetime'].apply(bn_exchange.iso8601)
    
kline_data.head()
kline_data.tail()


if bn_exchange.has['fetchOrders']:
    since = bn_exchange.parse8601('2024-04-23T00:00:00Z')
    end = bn_exchange.milliseconds() - 60*1000   #前一分钟
    all_kline_data = []
    while since<end:
        symbol = 'SOL/USDT'
        kline_data = bn_exchange.fetch_ohlcv(symbol,since=since,timeframe='1m')
        print(bn_exchange.iso8601(since))
        print(bn_exchange.iso8601(end))
        if len(kline_data):
            #更新获取时间
            since = kline_data[len(kline_data)-1][0]
            all_kline_data += kline_data
        else:
            break
        
all_kline_data_df = pd.DataFrame(all_kline_data)
all_kline_data_df.columns = ['Datetime','Open','High','Low','Close','Vol']
all_kline_data_df['Datetime'] = all_kline_data_df['Datetime'].apply(bn_exchange.iso8601)

all_kline_data_df.shape
all_kline_data_df.head()
all_kline_data_df.tail()

all_kline_data_df[all_kline_data_df['Datetime'].duplicated()]

all_kline_data_df.drop_duplicates(subset=['Datetime'],inplace=True)
all_kline_data_df['Datetime'] = pd.to_datetime(all_kline_data_df['Datetime'])
all_kline_data_df.set_index('Datetime',inplace=True)


#import os
import matplotlib.pyplot as plt
#%matplotlib inline
plt.show()
all_kline_data_df['Open'].plot(figsize=(15,8))












































