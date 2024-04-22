# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 09:27:42 2024

@author: Administrator
"""

import ccxt

print(ccxt.exchanges)


exchange = ccxt.okcoin()#default id
okcoin1 = ccxt.okcoin({'id':'okcoin1'})
okcoin2 = ccxt.okcoin({'id':'okcoin2})
id = 'btcchina'
btcchina = eval('ccxt.%s()' % id)

coinbasepro = getattr(ccxt,'coinbasepro')()



#from variable id
exchange_id = 'binance'
exchange_class = getattr(ccxt,exchange_id)
exchange = exchange_class
    （{
      'apikey':'YOUR_API_KEY',
      'secret':'YOUR_SECRET',
      }
    ）
    

ex = ccxt.binance()
def my_overload(symbol,params = {}):
    #your codes go here
    
ex.fetch_ticker = my_overload
print(ex.fetch_ticker('BTC/USDT'))


exchange = ccxt.binance(config)
exchange.set_sandbox_mode(True)  #enable sandbox mode


{
 'id':'exchange'
 'name':'Exchange'
 'countries':['US','CN','EU'],
 'urls':{
     'api':'https://api.example.com/data',
     'www':'https://www.example.com',
     'doc':'https://docs.example.com/api',
     },
 'version': 'v1',
 'api':{}#dictionary of api endpionts
 'has':{
        'CORS': false,
        'cancelOrder': true,
        'createDepositAddress': false,
        'createOrder': true,
        'fetchBalance': true,
        'fetchCanceledOrders': false,
        'fetchClosedOrder': false,
        'fetchClosedOrders': false,
        'fetchCurrencies': false,
        'fetchDepositAddress': false,
        'fetchMarkets': true,
        'fetchMyTrades': false,
        'fetchOHLCV': false,
        'fetchOpenOrder': false,
        'fetchOpenOrders': false,
        'fetchOrder': false,
        'fetchOrderBook': true,
        'fetchOrders': false,
        'fetchStatus': 'emulated',
        'fetchTicker': true,
        'fetchTickers': false,
        'fetchBidsAsks': false,
        'fetchTrades': true,
        'withdraw': false,
        },

'timeframes:{
    '1m':'1minute',
    '1h':'1hour',
    '1d':'1day',
    '1M':'1month',
    '1y':'1year',
},

 },