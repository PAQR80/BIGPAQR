import datetime as dt
import yfinance as yf
import pandas as pd

stocks = ["AMZN","MSFT","INTC","GOOG","INFY.NS","3988.HK"]
start = dt.datetime.today() - dt.timedelta(360)
end = dt.datetime.today()
cl_price = pd.DataFrame() # empty dataframe to be filled with closing prices 
ohlcv_data = {}

#looping over tickers and creating a dataframe with cl prices

for ticker in stocks:
    cl_price[ticker] = yf.download(ticker,start,end)["Adj Close"]

for ticker in stocks:
    ohlcv_data[ticker] = yf.download(ticker,start,end)

print(ohlcv_data["MSFT"]["Open"])
