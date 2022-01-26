import numpy as np 
import pandas as pd 
import pandas_datareader.data as web
import pandas_ta as ta
import datetime
from datetime import date
import yfinance as yf
from yahoo_fin import stock_info as si 
#########TIME FRAMES#############
start_date = date(2017, 8, 4)
end_date = date.today()
###################Data Frames################### only placing on each script for now. unsure how to refresh automatically 
def get_port(stocks, start=start_date, end=end_date):
    data = web.get_data_yahoo(stocks, data_source='yahoo', start=start, end=end, progress=True)
    return data
#### Separate dataset.

## Copper futures COMEX
d_df1 = get_port('HG=F')
d_df1['stock'] = 'Copper'
## Copper co Symbols
d_df4 = get_port('FCX')
d_df4['stock'] = 'Freeport copper'

d_df17 = get_port('BHP.AX')
d_df17['stock'] = 'BHP Group copper'

d_df5 = get_port('COPX')
d_df5['stock'] = 'COPX ETF'
## Aluminum futures
d_df2 = get_port('ALIX21.CMX')
d_df2['stock'] = 'ALu'
## Crude Oil
d_df3 = get_port('CL=F')
d_df3['stock'] = 'Crude oil'
## Natural Gas
d_df6 = get_port('NG=F')
d_df6['stock'] = 'Natural Gas'
##Currency Index
d_df7 = get_port('DX-Y.NYB')
d_df7['stock'] = 'Dollar Index'
d_df8 = get_port('JPY=X')
d_df8['stock'] = 'Japan Yen'
## Gold
d_df9 = get_port('GOLD')
d_df9['stock'] = 'Gold'
## Bitcoin
d_df10 = get_port('BTC-USD')
d_df10['stock'] = 'Bitcoin'
## Precious Metals
d_df11 = get_port('^DJGSP')
d_df11['stock'] = 'Precious Metals Index'
## Vehicle stocks
d_df12 = get_port('CAT')
d_df12['stock'] = 'Caterpillar'
d_df13 = get_port('TSLA')
d_df13['stock'] = 'Tesla'
d_df14 = get_port('VWAGY')
d_df14['stock'] = 'Volkswagen AG'
d_df15 = get_port('F')
d_df15['stock'] = 'Ford Motor Co'
d_df16 = get_port('GM')
d_df16['stock'] = ('General Motors Co')
## VIX indicator
d_df17 = get_port('^VIX') 
d_df17['stock'] = 'VIX' 

curlist = ['EURUSD=X', 'JPY=X', 'GBPUSD=X', 'AUDUSD=X', 'NZDUSD=X', 'EURJPY=X', 'GBPJPY=X', 'EURGBP=X',
          'EURCAD=X', 'EURSEK=X', 'EURCHF=X', 'EURHUF=X', 'EURJPY=X', 'CNY=X', 'HKD=X', 'SGD=X', 'INR=X',
          'MXN=X', 'PHP=X', 'IDR=X', 'THB=X', 'MYR=X', 'ZAR=X', 'RUB=X', 'DX-Y.NYB']

#curlist = ['EURUSD=X', 'CNY=X', 'DX-Y.NYB']

def exchange_index(stock):
    lst = []
    for x in stock:
        df = yf.download(x, groupby= 'Ticker', start = '2018-01-01', end = date.today())
        df['stock'] = x
        lst.append(df)
    dfer = pd.concat(lst)
    return dfer

dftotal = exchange_index(curlist)


dfs = [d_df1, d_df2, d_df3, d_df4, d_df5, d_df6, d_df7, d_df8, d_df9, d_df10, d_df11, d_df12, d_df13, d_df14, d_df16, d_df15, d_df17]
df = pd.concat(dfs, join = 'outer')

df = pd.concat([df, dftotal])

dfer = pd.pivot_table(df, index = ['Date'], columns = 'stock', values = 'Close')
dffer = dfer.reset_index()

stock_average = df.groupby(by='stock').mean().reset_index()
			   
plastic = pd.read_excel('plastic info.xlsx', sheet_name='plastics exchange')
plastics = plastic.loc[plastic['Date'] >= '01/05/2018']
plastic1 = plastics.loc[plastics.Resin.str.contains('HDPE - In', na = False)]

coal = pd.read_excel('plastic info.xlsx', sheet_name='coal')	
cpi = pd.read_excel('plastic info.xlsx', sheet_name='CPI')
