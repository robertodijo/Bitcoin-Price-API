import pandas as pd

filepath = "C:\\Users\\rober\\Desktop\\binance"
filename = "TradeHistory-16jan2018.xlsx"
file = filepath + "\\" + filename

data = pd.read_excel(file, sheetname=0)
# print(type(data))
pd.set_option('display.width', 1000)
print(data[:])
