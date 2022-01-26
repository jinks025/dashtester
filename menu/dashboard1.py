from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash import dash_table
import dash
from menu.style import *
from app import app, server
import datetime
from datetime import date
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pandas_datareader.data as web
import pandas_ta as ta
import yfinance as yf
import seaborn as sns
yf.pdr_override()
import cufflinks as cf
import plotly.graph_objects as go
from datetime import date
import plotly.express as px
from yahoo_fin import stock_info as si
from plotly.subplots import make_subplots

##########TIMEFRAME###########
start = datetime.datetime.now() - datetime.timedelta(30)
start1 = '2018-01-01'
end = date.today()
#######Dataframes##########
sp = yf.download('^GSPC', start=start, end=end)
nas = yf.download('^IXIC', start=start, end=end)

dow1 = yf.download('DOW', start=start1, end=end)
dow1['stock'] = 'Dow Jones'
dow = dow1.loc[dow1.index >=start]

cop1 = yf.download('HG=F', start=start1, end=end)    #, period = '1d', interval = '5m')
cop1['stock'] = 'Copper'
cop = cop1.loc[cop1.index >= start]

oil1 = yf.download('CL=F', start=start1, end=end) 
oil1['stock'] = 'Oil'
oil = oil1.loc[oil1.index >= start]

al1 = yf.download('ALI=F', start=start1, end=end)
al1['stock'] = 'Aluminum'
al = al1.loc[al1.index >= start]

ng1 = yf.download('NG=F', start=start, end=end)
ng1['stock'] = 'Natural Gas'
ng = ng1.loc[ng1.index>=start]

dol1 = yf.download('DX-Y.NYB', start=start1, end=end)
dol1['stock'] = 'USD'
dol = dol1.loc[dol1.index >=start]

cpi = pd.read_excel('plastic info.xlsx', sheet_name = 'CPI')

####### Graphs #########
fig = make_subplots(rows = 2, cols = 2, 
                   subplot_titles = ('S&P 500', 'NASDAQ', 'DOW JONES Ind Avg', 'Copper COMEX'))
fig['layout']['margin'] = {'l':30, 'r':10, 'b':50, 't':25}
fig.append_trace(go.Candlestick(x = sp.index, open=sp.Open, high=sp.High, low=sp.Low, close=sp.Close), 1, 1) 
fig.append_trace(go.Candlestick(x=nas.index,open=nas.Open, high=nas.High, low=nas.Low, close=nas.Close), 2,1) 
fig.append_trace(go.Candlestick(x=dow.index,open=dow.Open, high=dow.High, low=dow.Low, close=dow.Close), 1,2) 
fig.append_trace(go.Candlestick(x=cop.index,open=cop.Open, high=cop.High, low=cop.Low, close=cop.Close), 2,2) 
fig.update_xaxes(rangeslider_visible = False)

######
fig1 = make_subplots(specs = [[{'secondary_y':True}]])
fig1.add_trace(go.Scatter(x = cop1.index, y = cop1.Close, mode = 'lines', name = 'Copper prices / lbs COMEX'), secondary_y = False)
fig1.add_trace(go.Scatter(x = cpi.Date, y = cpi.Inflation, mode = 'lines', name = 'U.S. Inflation Rate'), secondary_y=True)
fig1.update_layout(title_text = 'Copper prices vs Inflation') 
fig1.update_layout(yaxis1 = dict(title = '<b>Copper<b> Comex price per lbs'), 
                   yaxis2 = dict(title = '<b>Inflation<b> rate'))
####
snsmap = pd.concat([cop1,dol1, dow1, ng1, oil1])
snsp = pd.pivot_table(snsmap, index = 'Date', columns = 'stock', values = ['Close', 'Open', 'Low'])
snsp.columns = snsp.columns.map(lambda x: '|'.join([str(i) for i in x]))
fig2 = px.imshow(snsp.corr(), color_continuous_scale='Jet') #, annot = True)
####
fig3 = make_subplots(specs = [[{'secondary_y':True}]])
fig3.add_trace(go.Scatter(x = al1.index, y = al1.Close, mode = 'lines', name = 'Aluminum Prices per ton'), secondary_y = False)
fig3.add_trace(go.Scatter(x = cpi.Date, y = cpi.Inflation, mode = 'lines', name = 'U.S. Inflation Rate'), secondary_y=True)
fig3.update_layout(title_text = 'Aluminum prices vs Inflation') 
fig3.update_layout(yaxis1 = dict(title = '<b>Copper<b> Comex price per lbs'), 
                   yaxis2 = dict(title = '<b>Inflation<b> rate'))
####
live = go.Figure()
live.add_trace(go.Indicator(
    mode='number+delta',
    value= si.get_live_price('HG=F'),
    number={'prefix': '$'},
    delta={'position': 'top', 'reference':cop.Close.iloc[-2], 'relative': True},
    title={'text': 'Price of Copper On COMEX<br><span style="font-size:0.8em;color:gray"> Current Price per lbs </span><br><span style="font-size:0.8em;color:gray"> (Change reflects previous close value)</span>'}))
live.update_layout(autosize = False, width=400, height =300)

####

live1 = go.Figure()
live1.add_trace(go.Indicator(
    mode='number+delta',
    value= si.get_live_price('CL=F'),
    number={'prefix': '$'},
    delta={'position': 'top', 'reference': oil.Close.iloc[-2], 'relative': True},
    title={'text': 'Price of Oil Futures<br><span style="font-size:0.8em;color:gray"> Current Price per barrel</span><br><span style="font-size:0.8em;color:gray"> (Change reflects previous close value)</span>'}))
live1.update_layout(autosize = False, width=400, height =300)

####

live2 = go.Figure()
live2.add_trace(go.Indicator(
    mode='number+delta',
    value=  si.get_live_price('ALI=F'),
    number={'prefix': '$'},
    delta={'position': 'top', 'reference': al.Close.iloc[-2], 'relative': True},
    title={'text': 'Price of Aluminum<br><span style="font-size:0.8em;color:gray"> Current Price per ton </span><br><span style="font-size:0.8em;color:gray"> (Change reflects previous close value)</span>'}))
live2.update_layout(autosize = False, width=400, height =300)

####

live3 = go.Figure()
live3.add_trace(go.Indicator(
    mode='number+delta',
    value= si.get_live_price('NG=F'),
    number={'prefix': '$'},
    delta={'position': 'top', 'reference': ng.Close.iloc[-2], 'relative': True},
    title={'text': 'Price of Natural Gas<br><span style="font-size:0.8em;color:gray"> Current Price $ per MMBtu </span><br><span style="font-size:0.8em;color:gray"> (Change reflects previous close value)</span>'}))
live3.update_layout(autosize = False, width=400, height =300)


####

live4 = go.Figure()
live4.add_trace(go.Indicator(
    mode='number+delta',
    value=si.get_live_price('DX-Y.NYB'),
    number={'prefix': '$'},
    delta={'position': 'top', 'reference': ng.Close.iloc[-2], 'relative': True},
    title={'text': 'Dollar Strength<br><span style="font-size:0.8em;color:gray"> Index</span><br><span style="font-size:0.8em;color:gray"> (Change reflects previous close value)</span>'}))
live4.update_layout(autosize = False, width=400, height =300)

######################Graph layout ###########################
graph1 = dcc.Graph(
    id = 'graph1',
    figure = fig
)

graph2 = dcc.Graph(
    id = 'graph2',
    figure = live, style={'display': 'inline-block'}
)

graph3 = dcc.Graph(
    id = 'graph3',
    figure = live1, style={'display': 'inline-block'}
)

graph4 = dcc.Graph(
    id = 'graph4',
    figure = fig1, style={'display': 'inline-block'}
)
                                  
graph5 = dcc.Graph(
    id = 'graph5',
    figure = live2, style={'display': 'inline-block'}
)

graph6 = dcc.Graph(
    id = 'graph6',
    figure = live3, style={'display': 'inline-block'}
)

graph7 = dcc.Graph(
    id = 'graph7',
    figure = live4, style={'display': 'inline-block'}
)

graph8 = dcc.Graph(
    id = 'graph8',
    figure = fig2, style={'display': 'inline-block'}
)

graph9 = dcc.Graph(
    id = 'graph9',
    figure = fig3, style={'display': 'inline-block'}
)
####################################################
s = html.H1(date.today(), 
            style = {'color':'white', 'fontSize':50, 'txtAlign':'center', 'background-color':'Black', 'font-family':'courier'})
####################################################
markdown_text = ''' ### Copper Prices vs Inflation
This page shows the current state of the market for the past 30 days (today's market activity is not included). However, 
prices with the indicators, are live market prices with each time you refresh the page.''' 

markdown_text1 = """ ### General Findings
The cost of goods and services determines the value of the dollar. The Federal Reserve pursues a stable inflation rate (~2%) and maximum-employment. 
Unemployment usually has a natural rate at around 3%. Comparing commoditiy prices to the dollar strength, in history, they have an inverse relationship. 
Inventory of copper plays a role in the valuation as well. In the heat map above, (red and blue chart), shows the relationship bewteen the price of copper 
and the USD. A '1' value is expected when the values are highly correlated (in this case the prices are highly correlated with themselves), a '0' value 
means there is no relation between the variables, and a value in the negative (as shown on this graph) shows an inverse correlation. The value between copper
and the USE is -0.71, not 1.00, but the correlation is there.""" 

markdown_text2 = ''' ### News/speculations
Recent downturns in copper prices(10-20-2021:11-08-2021) would have to do with news out of China. Recent energy shortage and fears of a slowing Chinese economy
has slowed the rise in costs.
* 11/8/2021 - Aluminum prices fall from slowing auto sales in China last month. Alcola will restart an aluminum in Australia to increase supply.'''

markdown_text3 = '''### Economic 
A stronger dollar is correlated with lower priced copper. Looking at the graphs, this continues to hold true with the correlation being -0.7. 
We will need to keep an eye on inflation to keep up with costs. Federal Reserve is holding inflation is transitory.'''


####################################################
BOX_STYLE1 = KOTAK_UTAMA_STYLE
SIDEBAR_STYLE1 = SIDEBAR_STYLE

# content
header = html.Div(children = [s])
graphshere = html.Div(children = [graph1])
indicators = html.Div(children = [graph2, graph3, graph5, graph6, graph7])
markdowns = html.Div([dcc.Markdown(children = [markdown_text, markdown_text1, markdown_text2, markdown_text3])],
                    style = {'color':'Black', 'fontSize':20, 'txtAlign':'center', 'background-color':'white', 'font-family':'courier'})
comgraph = html.Div(children = [graph4,graph8, graph9])

kotak_utama1 = html.Div([
    header,
    graphshere,
    indicators,
    comgraph, 
    markdowns], id='main box1',
    style=BOX_STYLE1
)

# sidebar
sidebar1 = html.Div(
    [html.Img(src=app.get_asset_url('logo.png'), style={
        'height': '116px',
        'width': '138px',
        'margin-top': '-9px',
        'background-color': 'rgba(0,0,0,0.03)'}),
     # html.Hr(),
     html.P([
         "Dashboard", html.Br(), "Commodity Metals", html.Br(), "Correlation"], className="lead",
         style={
             'textAlign': 'center',
             'background-color': 'rgba(0,0,0,0.03)',
             'color': '#f1a633',
             'fontSize': '8',
             'margin-top': '-3px'
         }),
     html.Hr(),
     html.Div(children=[
         html.A(html.Button('DASHBOARD I', className='tab-button'),
                href='/dashboard1'),
         html.Hr(),
         html.A(html.Button('DASHBOARD II', className='tab-button'),
                href='/dashboard2'),
         html.Hr(),
         html.A(html.Button('DASHBOARD III', className='tab-button'),
                href='/dashboard3'),
         html.Hr(),
         html.A(html.Button('DASHBOARD IV', className='tab-button'),
                href='/dashboard4'),
         html.Hr(),
     ],

     ),
     ],
    style=SIDEBAR_STYLE1,
)
content1 = html.Div([
    html.H1(['Market Today'],
            style={
                'margin-left': '340px',
                'margin-top': '20px',
                'color': 'rgba(255,255,255,1)',
                'fontSize': '18',
            }),

    kotak_utama1,

], style={
    'margin-left': '0px',
    'margin-top': '0px', }
)

layout1 = html.Div([dcc.Location(id="url"), sidebar1, content1])
