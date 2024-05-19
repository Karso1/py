import talib
import numpy as np

highs = np.array([120, 125, 120, 132, 140, 131], dtype=np.double)
lows = np.array([114, 114, 151, 151, 231, 414], dtype=np.double)
closes = np.array([119, 199, 414, 414, 414, 515], dtype=np.double)

atr = talib.ATR(highs,lows,closes,timeperiod = 14)
print(atr)

rsi = talib.RSI(closes,timeperiod = 14)
stochrsi = (rsi-np.min(rsi[-14:])) /(np.max(rsi[-14:]) - np.min(rsi[-14:]))
print(stochrsi)

upper_band,middle_band,lower_band = talib.BBANDS(closes,timeperiod=20,nbdevup=2,nbdevdn=2,matype=0)
print(upper_band,middle_band,lower_band)

