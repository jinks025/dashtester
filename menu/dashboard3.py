from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import dash
from dash.dependencies import Input, Output, State
from menu.style import *
from app import app, server
from yahoo_fin import stock_info as si
import datetime
from datetime import date
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pandas_datareader.data as web
import pandas_ta as ta
import yfinance as yf
pd.options.display.max_columns = None
yf.pdr_override()
import cufflinks as cf
cf.go_offline()
from dash import dash_table
import plotly.graph_objects as go
import plotly.express as px
from yahoo_fin import stock_info as si
from plotly.subplots import make_subplots
from menu.dataframes import *


###########Currency indices##########################


dol = dftotal.loc[dftotal.stock.str.contains('DX-Y')]
cny = dftotal.loc[dftotal.stock.str.contains('CNY')]
euro = dftotal.loc[dftotal.stock.str.contains('EURUSD')]

fig8 = make_subplots(rows = 1, cols = 1, shared_xaxes = True)
fig8.add_trace(go.Scatter(x = d_df1.index, y = d_df1['Close'], mode = 'lines', name = 'Copper'))
fig8.add_trace(go.Scatter(x = cny.index, y = cny['Close'], mode = 'lines', name = 'Chinese Renminbi exchange', yaxis = 'y2'))
fig8.add_trace(go.Scatter(x = dol.index, y = dol['Close'], mode = 'lines', name = 'Dollar index', yaxis = 'y3'))
fig8.add_trace(go.Scatter(x = euro.index, y = euro['Close'], mode = 'lines', name = 'Euro USD exchange rate', yaxis = 'y4'))
fig8.update_layout(xaxis = dict(title = 'Dates',  gridcolor = 'lightgrey'),
                  yaxis1 = dict(title = 'Copper COMEX prices'),
                  yaxis2 = dict(title = 'Chinese Renminbi', anchor = 'x', overlaying = 'y', side = 'right',
                               position =0.85),
                  yaxis3 = dict(title = 'Dollar Index', anchor = 'free', overlaying = 'y', side = 'right', position = 0.98),
                  yaxis4 = dict(title = 'Euro USD exchange rate', anchor = 'free', overlaying = 'y', side = 'left', position = 0.05),
                  title_text = 'Copper vs Dollar strength',
                  #paper_bgcolor = 'rgba(0,0,0,0)',
                  #plot_bgcolor = 'rgba(0,0,0,0)',
                  autosize = False,
                  width = 1000,
                  height = 500,
                 margin = dict(l = 100, r =20, b = 50, t = 60, pad = 60),
                 legend = dict(yanchor = 'bottom', y = 0.99, xanchor ='right', x = 0.99))

fig8.add_vrect(x0 = '2020-02-01', x1 = '2020-04-01', annotation_text= 'COVID recession', annotation_position = 'top left',
             fillcolor = 'green', opacity=0.25, line_width=0)

fig8.add_vrect(x0 = '2021-10-01', x1 = '2021-10-01', annotation_text = 'Infrastructure Bill Passed', annotation_position = 'bottom right',
              fillcolor = 'red', line_width=1)
fig8.add_vrect(x0 = '2021-07-29', x1 = '2021-10-08', annotation_text = 'China metal release', annotation_position = 'top left',
             fillcolor = 'red', line_width = 0, opacity = 0.25)
fig8.add_vrect(x0 = '2021-09-27', x1 = '2021-10-27', annotation_text = 'China energy crisis', annotation_position = 'top right',
             fillcolor = 'blue', line_width = 0, opacity = 0.25)
fig8.add_vrect(x0 = '2021-10-20', x1 = '2021-10-20', annotation_text = 'China increase coal production', annotation_position = 'bottom right',
              fillcolor = 'red', line_width=1)
fig8.add_vrect(x0 = '2021-10-18', x1 = '2021-10-18', annotation_text = 'China power cuts', annotation_position = 'top right',
              fillcolor = 'red', line_width=1)
fig8.add_vrect(x0 = '2021-09-22', x1 = '2021-09-22', annotation_text = 'US Feds hold steady on interest rates, 2021 Forecast cut', annotation_position = 'top right',
              fillcolor = 'purple', line_width=1)
fig8.add_vrect(x0 = '2021-10-27', x1 = '2021-10-27', annotation_text = 'China no bailout on debts, Evergrande fears', annotation_position = 'bottom right',
              fillcolor = 'yellow', line_width=1)

##########################################################
fig9 = make_subplots(shared_xaxes = True)
fig9.add_trace(go.Scatter(x = plastic1.Date, y = plastic1['High'], mode = 'lines', name = 'Plastic resin'))
fig9.add_trace(go.Scatter(x = d_df6.index, y = d_df6['Close'], mode = 'lines', name = 'Natural Gas', yaxis = 'y2'))
fig9.add_trace(go.Scatter(x = dol.index, y = dol['Close'], mode = 'lines', name = 'Dollar index', yaxis = 'y3'))
fig9.add_trace(go.Scatter(x = coal.Date, y = coal['Price'], mode = 'lines', name = 'Coal futures', yaxis = 'y4'))
fig9.add_trace(go.Scatter(x = d_df3.index, y = d_df3['Close'], mode = 'lines', name = 'oil', yaxis = 'y5'))
fig9.add_trace(go.Scatter(x = d_df1.index, y = d_df1['Close'], mode = 'lines', name = 'copper', yaxis = 'y6'))
fig9.update_layout(xaxis = dict(title = 'Dates',  gridcolor = 'lightgrey'),
                  yaxis1 = dict(title = 'Plastic Resin Prices'),
                  yaxis2 = dict(title = 'Natural Gas prices', anchor = 'x', overlaying = 'y', side = 'right'),
                  yaxis3 = dict(title = 'Dollar Index', anchor = 'free', overlaying = 'y', side = 'right', position = 0.80),
                  yaxis4 = dict(title = 'Coal prices (Rotterdam Coal Futures)', anchor = 'free', overlaying = 'y', side = 'left', position = 0.10),
                  yaxis5 = dict(title = 'Oil', anchor = 'x2', overlaying = 'y', side = 'right', position = 0.91),
                  yaxis6 = dict(title = 'Copper', anchor = 'x2', overlaying = 'y', side = 'left', position = 0.20),
                  title_text = 'Plastics vs Dollar strength',
                  #paper_bgcolor = 'rgba(0,0,0,0)',
                  #plot_bgcolor = 'rgba(0,0,0,0)',
                  autosize = False,
                  width = 1000,
                  height = 500,
                 #margin = dict(l = 50, r =20, b = 50, t = 60, pad = 10),
                 legend = dict(yanchor = 'bottom', y = 0.99, xanchor ='right', x = 0.99))
fig9.add_vrect(x0 = '2020-02-01', x1 = '2020-04-01', annotation_text= 'COVID recession', annotation_position = 'top left',
             fillcolor = 'green', opacity=0.25, line_width=0)

fig9.add_vrect(x0 = '2021-10-01', x1 = '2021-10-01', annotation_text = 'Infrastructure Bill Passed', annotation_position = 'bottom right',
              fillcolor = 'red', line_width=1)
fig9.add_vrect(x0 = '2021-07-29', x1 = '2021-10-08', annotation_text = 'China metal release', annotation_position = 'top left',
             fillcolor = 'red', line_width = 0, opacity = 0.25)
fig9.add_vrect(x0 = '2021-09-27', x1 = '2021-10-27', annotation_text = 'China energy crisis', annotation_position = 'top right',
             fillcolor = 'blue', line_width = 0, opacity = 0.25)
fig9.add_vrect(x0 = '2021-10-20', x1 = '2021-10-20', annotation_text = 'China increase coal production', annotation_position = 'bottom right',
              fillcolor = 'red', line_width=1)
fig9.add_vrect(x0 = '2021-10-18', x1 = '2021-10-18', annotation_text = 'China power cuts', annotation_position = 'top right',
              fillcolor = 'red', line_width=1)
fig9.add_vrect(x0 = '2021-09-22', x1 = '2021-09-22', annotation_text = 'US Feds hold steady on interest rates, 2021 Forecast cut', annotation_position = 'top right',
              fillcolor = 'purple', line_width=1)
fig9.add_vrect(x0 = '2021-10-27', x1 = '2021-10-27', annotation_text = 'China no bailout on debts, Evergrande fears', annotation_position = 'bottom right',
              fillcolor = 'yellow', line_width=1)
##########################################################

fig10 = make_subplots(specs = [[{'secondary_y':True}]])
fig10.add_trace(go.Scatter(x = d_df1.index, y = d_df1['Close'], mode = 'lines', name = 'Copper COMEX price'))
fig10.add_trace(go.Scatter(x = cpi.Date, y = cpi['Inflation'], mode = 'lines', name = 'Inflation'), secondary_y = True)
fig10.update_layout(title_text = 'Inflation rate vs Copper Price on COMEX',
                  yaxis1 = dict(title = 'COMEX copper Prices per lbs'),
                  yaxis2 = dict(title = 'Inflation rate in %', anchor = 'x', overlaying = 'y', side = 'right'),
                  xaxis = dict(title = 'Dates',  gridcolor = 'lightgrey'))


###########################################################

fig11 = make_subplots(specs = [[{'secondary_y':True}]])
fig11.add_trace(go.Scatter(x = plastic1.Date, y = plastic1['High'], mode = 'lines', name = 'HDPE - Inj High price'))
fig11.add_trace(go.Scatter(x = cpi.Date, y = cpi['Inflation'], mode = 'lines', name = 'Inflation'), secondary_y = True)
fig11.update_layout(title_text = 'Inflation rate vs Plastic resin HDPE-Inj cost per lbs',
                  yaxis1 = dict(title = "HDPE Inj resin High's"),
                  yaxis2 = dict(title = 'Inflation rate in %', anchor = 'x', overlaying = 'y', side = 'right'),
                  xaxis = dict(title='Dates', gridcolor='lightgrey'))
#####Graph layout#### 
graph6 = dcc.Graph(
    id = 'graph6',
    config={'autosizable': True, 'displayModeBar': False},
    animate=True,
    figure = fig8,
    #style={'display': 'inline-block'}
)

graph7 = dcc.Graph(
    id = 'graph7',
    figure = fig9, 
    #style={'display': 'inline-block'}
)

graph8 = dcc.Graph(
    id = 'graph8',
    figure = fig10, style={'display': 'inline-block'}
)

graph9 = dcc.Graph(
    id = 'graph9',
    figure = fig11, style={'display': 'inline-block'}
)
######### MARKDOWN #########
markdown_text = '''
### USD Strength VS. Copper prices (COMEX) and other currencies

The dollar is considered strong when it rises in value against other currencies in the foreign exchange market. 
 A stronger dollar means for cheaper imports, which means exports cost more. More expensive exports may yield slower abroad business.
 This graph shows a relation between the COMEX copper price to Euro and Chinese Renminbi exchange rates. 
 The Euro is stronger, but has a similar path as copper. 
 The Chinese Renminbi follows the USD pattern, this may be happening because how much USD the chinese economy has purchased. 
 China purhcases USD to lower the value of their currency. This usually makes a favorable condition for their economy to keep growing as operating costs in the country 
 is lower/cheaper. 
 However, the Renminbi and USD shows an inverse relation to the price of copper, which follows the historical trend. 
 This correlation is not perfect (USD to Copper prices), but the observation is significant and pictured on the graph.
 Notes on significant dates are also noted to for outside/psychological factors on the market. '''

markdown_text2 = '''
### Plastic Resin price vs inputs 

The cost of plastic resin is taken from the plastics exchange. These prices will be on the lower side/competitive due to the nature of the site's business. 
Costs should reflect market sentiment, and relating back to the our costs, the price is not far off. The graph below takes a look at the cost of copper, coal (Rotterdam Coal Futures),
oil, natural gas, and the dollar index. From reading around, natural gas and crude oil should have a correlation with the cost of plastics.
The U.S. relies heavily on natural gas for ethylene production, which gets turned into polymers for plastic. Much like copper, the price of plastics increased due to supply issues. 
Recent news on energy shortages(10/2021) has fueled fears over lower demand and a slowing economy. We can see the price of energy (in form of oil, natural gas, and coal) rose significantly recently. 
This rise in energy costs lead to a slight decrease in the price of plastic resins in the plastic spot market. Plastics exchange report also mentions supply is growing and demand seems to have slowed. 
Combination causing a drop in prices. This is may be a corrective period. There is an anticipation of lower prices in spot and contract prices.'''

markdown_text4 = ''' 
### Inflation vs Dollar index vs Copper prices

This graph shows the relation with the dollar strength vs inflation and copper prices. We expect inflation rates to have an inverse relationship with the dollar index. 
As the cost of goods increases, the less we can buy. Causing the dollar to be weaker. Copper prices holds the same pattern as inflation rates. 
This leads to a possible confirmation the price of copper is likely tied to how strong the USD is. Smaller valleys, are likely from other international news. 
More recent, fears on energy shortage and falling demand for copper has caused the prices to fluctuate. '''

markdown_text5 = ''' 
### Inflation formula : 
*** % Inflation rate = (CPI Now -CPI Initial / Initial CPI Value) x 100 ***
* As noted above, inflation is due to a change/increase in consumer price index (average cost of items). 
Cyclic rise in costs pushing the cost of goods higher. -- Higher wages needed for higher rent. 
We are being told the current experience is transitory and that this will work itself out when everything is running back to normal. 
Feds mentioned nothing about rising cost of housing. Issues are likely to run well into 2022.
* [CPI link US BLS](https://www.bls.gov/cpi/)'''
########## LAYOUT #####################


BOX_STYLE3 = KOTAK_UTAMA_STYLE
SIDEBAR_STYLE3 = SIDEBAR_STYLE

#content
kolom_kiri3 = html.Div([dcc.Markdown(children = markdown_text), graph6])
kolom_tengah3 = html.Div(graph8)
kolom_kanan3 = html.Div([dcc.Markdown(children = markdown_text2), graph7])
kolom_peta3 = html.Div(graph9)

mainbox3 = html.Div([
    kolom_kiri3,
    kolom_tengah3,
    kolom_kanan3,
    kolom_peta3],id='main box3',
      style=BOX_STYLE3
                      )

#sidebar
sidebar3 = html.Div(
    [html.Img(src=app.get_asset_url('logo.png'),style={
                        'height':'116px', 
                        'width':'138px',
                        'margin-top': '-9px',
                        'background-color' : 'rgba(0,0,0,0.03)'}),
        #html.Hr(),
        html.P([
            "Cost for ", html.Br(),"Materials", html.Br(), "vs Economic signals"], className="lead", 
            style={
                'textAlign': 'center',
                'background-color' : 'rgba(0,0,0,0.03)',
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
    style=SIDEBAR_STYLE3,
)
content3 = html.Div([
            html.H1(['Materials cost vs Economic'],
              style={
              'margin-left': '340px',
              'margin-top': '20px',
              'color': 'rgba(255,255,255,1)',
              'fontSize': '18',
              }),     


             mainbox3,
            
              ],style={
              'margin-left': '0px',
              'margin-top': '0px',}
              )


layout3 = html.Div([dcc.Location(id="url"), sidebar3, content3])
