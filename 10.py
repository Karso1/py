import time
import ccxt
import pandas as pd
from datetime import datetime



def calculate_profit(open_order,close_order,is_long)
    open_price = open_order['average']#平均开仓价
    close_price = close_order['average']#评价平仓价
    qantity = open_order['filled']#成交数量

    #计算盈亏
    if is_long
        profit = (close_price - open_price)*quantity #做多
    else:
        profit = (open_price - close_price)*quantity #做空
    return profit