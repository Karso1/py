# -*- coding: utf-8 -*-
"""
Created on Wed May  1 16:11:16 2024

@author: Administrator
"""

'''
rsi = 100 - 100/(1+rs)

1st rs = (average gain/average loss)

average gain = total gains /n
average loss = total loss  /n


smoothed rs = [previous average gain * (n-1) + current gain]/n
             /[previous average loss *(n-1)   + current loss]/n

n = 14



'''

from catalyst.api import order,record,symbol

def initialize(context):
    #初始化
    
    
    context.asset = symbol('btc_usdt')
    
def handle_data(context,data):
        #循环策略
        
        #每个周期买入一个btc
        order(context.asset, 1)
    
        #记录每个交易周期的比特币价格
        record(btc=data.current(context.asset,'price'))
        
        
if __name__ == '__main__':
    run_algorithm(
        capital_base=10000,
        data_frequency='daily',
        initialize=initialize,
        handle_data=handle_data,
        exchange_name='biannce',
        quote_currency='usdt',
        start=pd.to_datetime('2018-01-01',utc=True),)
    
    
    
    
    
    
    
    
    
    
    
    
    