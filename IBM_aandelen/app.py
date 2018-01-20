# from pandas_datareader import data
# import pandas_datareader.data as pdr
from pandas_datareader import data as pdr
import fix_yahoo_finance as yf
import matplotlib.pyplot as plt
import pandas as pd
import datetime

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2013, 1, 27)
# f = web.DataReader("F", 'google', start, end)

yf.pdr_override()  # <== that's all it takes :-)

# download dataframe
data = pdr.get_data_yahoo("AMZN", start="2017-01-01", end="2017-04-30")

# download Panel
# data = pdr.get_data_yahoo(["SPY", "IWM"], start="2017-01-01", end="2017-04-30")
# amzn = web.get_quote_yahoo('AMZN')
# amzn
print(" ")
data.set_option('display.width', 1000)
print(data.head())
