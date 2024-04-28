# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 15:43:15 2024

@author: Administrator
"""

#三角
'''
market A:amount_A
B:amount_A/Pp
?:(amount_A/P1)/P2
sell ? and buy A:(amount_A/P1)/P2*P3



'''

import ccxt
import pandas as pd
import time

pd.set_option('expand_frame_repr',False)

def main():
    
    
    
        #initial cex
        binance_exchange = ccxt.binance({
        'proxies': {'http': '127.0.0.1:7890', 'https': '127.0.0.1:7890' },
        'timeout':15000,
        'enableRatelimit':True
        })
        
        
        #loading the market
        markets = binance_exchange.load_markets()
        
        
        #step 1:choose two market A,B
        market_a = 'BTC'
        market_b = 'ETH'
        
        
        
        
        #step 2:找到所有同时以A和B都作为计价的货币
        #市场内的交易对
        symbols = list(markets.keys())
        
        #存放到DataFrame中
        symbols_df = pd.DataFrame(data=symbols,columns=['symbol'])
        
        #divend the string to get 基础货币/计价货币
        base_quote_df = symbols_df['symbols'].str.split(pat='/',expand=True)
        base_quote_df.columns = ['base','quote']
        
        
        #过滤得到以A，B计价的计价货币
        base_a_list = base_quote_df[base_quote_df['quote'] == market_a]['base'].values.tolist()
        base_b_list = base_quote_df[base_quote_df['quote'] == market_b]['base'].values.tolist()
        
        #获取相同的基础货币列表
        common_base_list = list(set(base_a_list).intersection(set(base_b_list)))
        print('{}和{}共有{}个相同的计价货币'.format(market_a,market_b,len(common_base_list)))
        
        
        
        
        #step 3:wrok
        
        #save the result in the DataFrame
        columns = ['Market A',
                   'Market B',
                   'Market C',
                   'P1',
                   'P2',
                   'P3',
                   'Profit(‰)']
        
        result_df = pd.DataFrame(columns=columns)
        
        #获取前一分钟的close价格
        last_min = binance_exchange.milliseconds() - 60*1000
        
        for base_coin in common_base_list:
            market_c = base_coin
            market_a2b_symbol = '{}/{}'.format(market_b,market_a)
            market_b2c_symbol = '{}/{}'.format(market_c,market_b)
            market_a2c_symbol = '{}/{}'.format(market_c,market_a)
            
            
        #获取前一分钟的k线数据
        market_a2b_kline = binance_exchange.fetch_ohlcv(market_a2b_symbol,since=last_min,limit=1,timeframe='1m')
        market_b2c_kline = binance_exchange.fetch_ohlcv(market_a2b_symbol,since=last_min,limit=1,timeframe='1m')
        market_a2c_kline = binance_exchange.fetch_ohlcv(market_a2b_symbol,since=last_min,limit=1,timeframe='1m')
        
        if len(market_a2b_kline) == 0 or len(market_b2c_kline) == 0 or market_a2c_kline == 0:
            continue
        
        #获取行情前一分钟的交易对价格
        #数组里的第四个是收盘价 
        p1 = market_a2b_kline[0][4]
        p2 = market_b2c_kline[0][4]
        p3 = market_a2c_kline[0][4]
        
        #价差
        profit = (p3/(p1*p2)-1)*1000
        
        result_df = result_df.append({
            'Market A':market_a,
            'Market B':market_b,
            'Market C':market_c,
            'P1':p1,
            'P2':p2,
            'P3':p3,
            'Profit(‰)':profit
            },ignore_index=True)
        
        
        #显示信息
        print(result_df.tail(1))
        
        #防止超过rate limit
        time.sleep(binance_exchange.ratelimit/1000)
        
        
        
        result_df.to_csv('./tri_arbitrage_results.csv',index=None)
        
        if __name__ == '__main__':
            main()
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        