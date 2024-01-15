from alpha_vantage.timeseries import TimeSeries
import pandas as pd
import time

'''
ts = TimeSeries(key='34SNLW7NIWB905UJ',output_format='pandas')
data = ts.get_daily(symbol='EURUSD',outputsize='full')[0]
data.columns = ["open","high","low","close","volume"]

print(data) 

'''

all_tickers = ["AAPL","MSFT","CSCO","AMZN","GOOG","FB"]
close_prices = pd.DataFrame()
api_call_count = 0
for ticker in all_tickers:
    starttime = time.time()
    ts = TimeSeries(key='34SNLW7NIWB905UJ',output_format='pandas')
    data = ts.get_intraday(symbol=ticker, interval='1min' ,outputsize='compact')[0]
    api_call_count = api_call_count+1
    data.columns = ["open","high","low","close","volume"]
    close_prices[ticker] = data["close"]
    if api_call_count == 5:
        api_call_count = 0
        print("espera")
        print(time.time()-starttime)
        time.sleep(60 - (time.time()-starttime))

print(close_prices)
