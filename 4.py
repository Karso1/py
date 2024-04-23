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
    'timeout':10000,
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

symbol = 'BTC/USDT'
#获取指定交易对市场信息
btc_usdt_market = bn_markets[symbol]


btc_usdt_market

#获取单个交易对ticker数据
ticker_data = bn_exchange.fetchTicker(symbol)
ticker_data

print('Ticker时刻：',ticker_data['datetime'])
print('Ticker价格：',ticker_data['last'])


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
print('买价：{：.2f}，卖价：{:.2f},价差：{：.2f}',format(bid,ask,spread))



#k line
if bn_exchange.has['fetchOHLCV']:
    print(bn_exchange.fetch_ohlcv(symbol,timeframe='1d'))
    
    

import pandas as pd
if bn_exchange.has['fetchOHLCV']:
    kline_data = pd.Daraframe(bn_exchange.fetch_ohlcv(symbol,timeframe='1m'))
    kline_data.columns = ['Datetime','Open','High','Low','close','vol']
    kline_data['']








































