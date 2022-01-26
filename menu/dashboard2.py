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
			   

################# Figures ##############
d_df1 = df.loc[df.stock.str.contains('HG=F')]
figure1 = cf.QuantFig(d_df1, title='Copper COMEX', name='HG=F')
figure1.add_bollinger_bands()
figure1.add_macd(fast_period=12, slow_period=26, signal_period=9)
figure1.add_rsi(periods=20, rsi_upper=70, rsi_lower=30, showbands=True)
figure1.add_sma()
figure1.add_cci()

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

###########################################################
cpi = pd.read_excel('plastic info.xlsx', sheet_name='CPI')

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

###########################################################

fig12 = make_subplots(specs = [[{'secondary_y':True}]])
fig12.add_trace(go.Scatter(x = plastic1.Date, y = plastic1['Total lbs'], mode = 'lines', name = 'HDPE - Inj lbs offered'))
fig12.add_trace(go.Scatter(x = cpi.Date, y = cpi['Inflation'], mode = 'lines', name = 'Inflation'), secondary_y = True)
fig12.update_layout(title_text = 'Inflation rate vs Plastic resin HDPE-Inj lbs offered',
                  yaxis1 = dict(title = "HDPE Inj Total lbs offered"),
                  yaxis2 = dict(title = 'Inflation rate in %', anchor = 'x', overlaying = 'y', side = 'right'),
                  xaxis = dict(title='Dates', gridcolor='lightgrey'))

###########################################################

fig13 = make_subplots(specs = [[{'secondary_y':True}]])
fig13.add_trace(go.Scatter(x = plastic1.Date, y = plastic1['Total lbs'], mode = 'lines', name = 'HDPE - Inj lbs offered'))
fig13.add_trace(go.Scatter(x = plastic1.Date, y = plastic1['High'], mode = 'lines', name = 'High prices'), secondary_y = True)
fig13.update_layout(title_text = 'Inflation rate vs Plastic resin HDPE-Inj lbs offered',
                  yaxis1 = dict(title = "HDPE Inj Total lbs offered"),
                  yaxis2 = dict(title = 'HDPE Inj High prices ', anchor = 'x', overlaying = 'y', side = 'right'),
                  xaxis = dict(title='Dates', gridcolor='lightgrey'))

###########################################################
europlast = pd.read_excel('plastic info.xlsx', sheet_name= 'Euro plastics')
europlast1 = europlast.loc[europlast.Resin.str.contains('HDPE inj')]
europlast1 = europlast1.loc[europlast1.Date >= '01/08/2018']

fig14 = make_subplots(shared_xaxes = True)
fig14.add_trace(go.Scatter(x = plastic1.Date, y = plastic1['High'], mode = 'lines', name = 'HDPE - Inj High prices'))
fig14.add_trace(go.Scatter(x = d_df6.index, y = d_df6['Close'], mode = 'lines', name = 'Natural Gas spot prices', yaxis = 'y2'))
fig14.add_trace(go.Scatter(x = plastic1.Date, y = plastic1['Total lbs'], mode = 'lines', name = 'HDPE - Inj total pounds offered', yaxis = 'y3'))
fig14.update_layout(xaxis = dict(title = 'Dates',  gridcolor = 'lightgrey'),
                  yaxis1 = dict(title = 'HDPE - Inj Resin Prices'),
                  yaxis2 = dict(title = 'Natural Gas prices', anchor = 'x', overlaying = 'y', side = 'right', position = 0.98),
                  yaxis3 = dict(title = 'HDPE - Inj lbs offered', anchor = 'free', overlaying = 'y', side = 'left', position = 0.1),
                  title_text = 'Plastics - HDPE-INJ',
                  paper_bgcolor = 'rgba(0,0,0,0)',
                  plot_bgcolor = 'rgba(0,0,0,0)',
                  autosize = False,
                  width = 1000,
                  height = 500,
                 #margin = dict(l = 50, r =20, b = 50, t = 60, pad = 10),
                 legend = dict(yanchor = 'bottom', y = 0.99, xanchor ='right', x = 0.99))

###########################################################

fig15 = make_subplots(shared_xaxes = True)
fig15.add_trace(go.Scatter(x = europlast1.Date, y = europlast1['Price'], mode = 'lines', name = 'HDPE - Inj High prices Europe Market'))
fig15.add_trace(go.Scatter(x = d_df6.index, y = d_df6['Close'], mode = 'lines', name = 'Natural Gas spot prices', yaxis = 'y2'))
fig15.add_trace(go.Scatter(x = plastic1.Date, y = plastic1['High'], mode = 'lines', name = 'HDPE - Inj US market', yaxis = 'y3'))
fig15.update_layout(xaxis = dict(title = 'Dates',  gridcolor = 'lightgrey'),
                  yaxis1 = dict(title = 'HDPE - europe market per ton'),
                  yaxis2 = dict(title = 'Natural Gas prices', anchor = 'x', overlaying = 'y', side = 'right', position = 0.98),
                  yaxis3 = dict(title = 'HDPE - US market per lbs', anchor = 'free', overlaying = 'y', side = 'left', position = 0.1),
                  title_text = 'Plastics - HDPE-INJ',
                  paper_bgcolor = 'rgba(0,0,0,0)',
                  plot_bgcolor = 'rgba(10,10,10)',
                  autosize = False,
                  width = 1000,
                  height = 500,
                 #margin = dict(l = 50, r =20, b = 50, t = 60, pad = 10),
                 legend = dict(yanchor = 'bottom', y = 0.99, xanchor ='right', x = 0.99))
####################### Setting Graphs as HTML Children ##############
graph1 = dcc.Graph(
    id='graph1',
    config={'autosizable': True, 'displayModeBar': False},
    animate=True
    # className="eight columns"
)

graph2 = dcc.Graph(
    id='graph2',
    # figure=afp,
    # className="five columns"
)

graph3 = dcc.Graph(
    id='graph3'
    # className="five columns"
)

#graph4 = dcc.Graph(
#    id='graph4',
#    figure=figure1.iplot(asFigure=True)
#)

#graph5 = dcc.Graph(
#    id='graph5',
#    figure=live
#    #style = {'width':'10vh', 'height':'10vh'}
#)

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
    figure = fig10
)

graph9 = dcc.Graph(
    id = 'graph9',
    figure = fig11
)

graph10 = dcc.Graph(
    id = 'graph10',
    figure = fig12
)

graph11 = dcc.Graph(
    id = 'graph11',
    figure = fig13
)

graph12 = dcc.Graph(
    id = 'graph12',
    figure = fig14
)

graph13 = dcc.Graph(
    id = 'graph13',
    figure = fig15
)
#########DATATABLES#################
dff = df.reset_index()

table1 = dash_table.DataTable(
    id = 'stock data',
    columns = [{'name': i, 'id': i} for i in dff.columns],
#    data = dff.head(20).to_dict('records'),
    page_current = 0,
    page_size = 20,
    page_action = 'custom',

    filter_action= 'custom',
    filter_query= '',

    sort_action= 'custom',
    sort_mode= 'multi',
    sort_by = []
)
#################Markdowns###################
markdown1 = '''
### Candlestick Graphs

Candlestick Graphs is a common standard to show changes in prices. Movements can be measured by color and size. This helps measure emotion on the market.
This graph is meant to be interactive and show market prices on possible influencers (crude oil, copper producers, etc). Select a ticker from the downdown.
Multiple tickers can be selected, a ticker can be deselected via the "x" next to the ticker. Click and drag on the slider or on the graph for a more detailed view.
Hover over each candle for more information on open, close, high, low prices.  
The logic behind this is to have a basis on market sentiment on basic influencers on material cost.'''

markdown2 = ''' ### Comparison Tables 
Graphs on the second row allows for comparisons on the subplots. You can compare historical prices of different stocks. Correlation graphs are also provided. 
Stock tickers can be selected from the dropdown box.''' 

markdown3 = ''' ### Data tables with interactive graphs 

This table is the data source for most of the graphs on this dashboard. It can be filtered through to see exact points of data as needed. 
You can filter the columns via highest to lowest, or search for what you want to see. The graphs to the right represents line graphs relating to the data on the datatable. 
Top: Close | Bottom: Volume'''
############### Creating Widgets For Each Graph #########################
multi_select_line_chart = dcc.Dropdown(
    id="multi_select_line_chart",
    options=[{"value": label, "label": label} for label in df.stock.unique()],
    value=["Copper"],
    multi=True,
    clearable=False
)

dropdown1_scatter_chart = dcc.Dropdown(
    id="dropdown1_scatter_chart",
    options=[{"value": label, "label": label} for label in dfer.columns],
    value=dfer.columns[0],
    className="six columns",
    clearable=False
)

dropdown2_scatter_chart = dcc.Dropdown(
    id="dropdown2_scatter_chart",
    options=[{"value": label, "label": label} for label in dfer.columns],
    value=dfer.columns[1],
    className="six columns",
    clearable=False
)

dropdown_corrgraph = dcc.Dropdown(
    id="dropdown_corrgraph",
    options=[{"value": label, "label": label} for label in dfer.columns],
    value=dfer.columns[0],
    clearable=False
)

dropdown2_corrgraph = dcc.Dropdown(
    id="dropdown2_corrgraph",
    options=[{"value": label, "label": label} for label in dfer.columns],
    value=dfer.columns[1],
    clearable=False
)

######################### Laying out Charts & Widgets to Create App Layout ##########

row1 = html.Div(children=[multi_select_line_chart, graph1], className="eight columns")

scatter_div = html.Div(
    children=[html.Div(children=[dropdown1_scatter_chart, dropdown2_scatter_chart], className="row"), graph2],
    className="six columns")

bar_div = html.Div([html.Div(children=[dropdown_corrgraph, dropdown2_corrgraph], className="row2"), graph3],
    className = 'six columns')

row3 = html.Div(children=[scatter_div, bar_div], className="eight columns")

#cufflinker = html.Div(children=[graph4], className = 'six columns')

#row2 = html.Div(children=[cufflinker], className='eight columns')

row4 = html.Div(children = [graph6], className = 'eight columns')

row5 = html.Div(children = [graph7], className = 'eight columns')

cont = html.Div(id = 'table-paging-with-graph-container', className = 'five columns')

dastable = html.Div(children = [table1], className = 'six columns')

row6 = html.Div(children = [html.Div(children = [dastable]), cont])

row8 = html.Div(children = [graph8, graph9, graph10, graph11, graph12, graph13], className = 'eight columns')

marks = html.Div([dcc.Markdown(children = [markdown1, markdown2, markdown3])],
		style = {'color':'Black', 'fontSize':16, 'txtAlign':'center', 'background-color':'white', 'font-family':'courier'})

#####################################

BOX_STYLE2 = KOTAK_UTAMA_STYLE
SIDEBAR_STYLE2 = SIDEBAR_STYLE

#content
kolom_kiri2 = html.Div(children = [row1])
kolom_tengah2 = html.Div(children = [row3])
kolom_kanan2 = html.Div(children = [row6])
kolom_peta2 = html.Div(children = [marks])

mainbox2 = html.Div([
    kolom_kiri2,
    kolom_tengah2,
    kolom_kanan2,
    kolom_peta2],id='main box2',
      style=BOX_STYLE2
                      )

#sidebar
sidebar2 = html.Div(
    [html.Img(src=app.get_asset_url('logo.png'),style={
                        'height':'116px', 
                        'width':'138px',
                        'margin-top': '-9px',
                        'background-color' : 'rgba(0,0,0,0.03)'}),
        #html.Hr(),
        html.P([
            "Price", html.Br(),"or factors", html.Br(), "into costs"], className="lead", 
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
    style=SIDEBAR_STYLE2,
)
content2 = html.Div([
					  html.H1(['Historical Data'],
					  	style={
					  	'margin-left': '340px',
					  	'margin-top': '20px',
					  	'color': 'rgba(255,255,255,1)',
					  	'fontSize': '18',
					  	}),			


					   mainbox2,
					  
					  	],style={
					  	'margin-left': '0px',
					  	'margin-top': '0px',}
					  	)


layout2 = html.Div([dcc.Location(id="url"), sidebar2, content2])

################## Creating Callbacks for Each Widget ############################
@app.callback(Output('graph1', 'figure'),
              [Input('multi_select_line_chart', 'value')])
def update_line(price_options):
    chart1 = []
    dmer = df

    for stock in price_options:
        chart1.append(go.Candlestick(x=dmer[dmer['stock'] == stock].index,
                                     open=dmer[dmer.stock == stock].Open,
                                     high=dmer[dmer.stock == stock].High,
                                     low=dmer[dmer.stock == stock].Low,
                                     close=dmer[dmer.stock == stock].Close,
                                     name=stock))

    traces = [chart1]
    data = [val for sublist in traces for val in sublist]
    can_fig = {'data': data,
               'layout': go.Layout(
                   margin={'b': 15},
                   hovermode='x',
                   autosize=True,
                   title={'text': 'Market Prices', 'x': 0.5},
                   xaxis={'range': [dmer.index.min(), dmer.index.max()]},
                   yaxis={'title': 'Price in USD $', 'autorange': True})}
    return can_fig


@app.callback(Output('graph2', 'figure'),
              [Input('dropdown1_scatter_chart', 'value'), Input('dropdown2_scatter_chart', 'value')])
def update_scatter(drop1, drop2):
    dfer1 = dffer.loc[:,['Date',drop1, drop2]]
    df12 = dfer1
    chart2 = make_subplots(specs = [[{'secondary_y':True}]])
    chart2.add_trace(go.Scatter(x = df12.Date, y = df12.loc[:,drop1], mode = 'lines', name = drop1))
    chart2.add_trace(go.Scatter(x = df12.Date, y = df12.loc[:,drop2], mode = 'lines', name = drop2), secondary_y=True)
    chart2.update_layout(title_text = '%s vs %s close price' %(drop1, drop2), height = 500)

    return chart2


@app.callback(Output('graph3', 'figure'),
              [Input('dropdown_corrgraph', 'value'), Input('dropdown2_corrgraph', 'value')])
def update_bar(bar_drop, bar_drop2):
    df3 = df.loc[df['stock']==bar_drop]
    df4 = df.loc[df['stock']==bar_drop2]
    df31 = pd.concat([df3,df4])
    chart3 = px.scatter_matrix(df31,
                               dimensions = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'],
                               color = 'stock', symbol = 'stock',
                               title = 'Scatter Correlation matrix in Market')

    return chart3

operators = [['ge ', '>='],
             ['le ', '<='],
             ['lt ', '<'],
             ['gt ', '>'],
             ['ne ', '!='],
             ['eq ', '='],
             ['contains '],
             ['datestartswith ']]

def split_filter_part(filter_part):
    for operator_type in operators:
        for operator in operator_type:
            if operator in filter_part:
                name_part, value_part = filter_part.split(operator, 1)
                name = name_part[name_part.find('{') + 1: name_part.rfind('}')]

                value_part = value_part.strip()
                v0 = value_part[0]
                if (v0 == value_part[-1] and v0 in ("'", '"', '`')):
                    value = value_part[1: -1].replace('\\' + v0, v0)
                else:
                    try:
                        value = float(value_part)
                    except ValueError:
                        value = value_part

                # word operators need spaces after them in the filter string,
                # but we don't want these later
                return name, operator_type[0].strip(), value

    return [None] * 3


@app.callback(
    Output('stock data', "data"),
    Input('stock data', "page_current"),
    Input('stock data', "page_size"),
    Input('stock data', "sort_by"),
    Input('stock data', "filter_query"))
def update_table(page_current, page_size, sort_by, filter):
    filtering_expressions = filter.split(' && ')
    dff = df.reset_index()
    dff['Date'] = dff['Date'].dt.date
    for filter_part in filtering_expressions:
        col_name, operator, filter_value = split_filter_part(filter_part)

        if operator in ('eq', 'ne', 'lt', 'le', 'gt', 'ge'):
            # these operators match pandas series operator method names
            dff = dff.loc[getattr(dff[col_name], operator)(filter_value)]
        elif operator == 'contains':
            dff = dff.loc[dff[col_name].str.contains(filter_value)]
        elif operator == 'datestartswith':
            # this is a simplification of the front-end filtering logic,
            # only works with complete fields in standard format
            dff = dff.loc[dff[col_name].str.startswith(filter_value)]

    if len(sort_by):
        dff = dff.sort_values(
            [col['column_id'] for col in sort_by],
            ascending=[
                col['direction'] == 'asc'
                for col in sort_by
            ],
            inplace=False
        )

    return dff.iloc[
        page_current*page_size: (page_current + 1)*page_size
    ].to_dict('records')


@app.callback(
    Output('table-paging-with-graph-container', "children"),
    Input('stock data', "data"))
def update_graph(rows):
    dff = pd.DataFrame(rows)
    return html.Div(
        [
            dcc.Graph(
                id=column,
                figure={
                    "data": [
                        {
                            "x": dff["Date"],
                            "y": dff[column] if column in dff else [],
                            "type": "line",
                            "marker": {"color": "#0074D9"},
                        }
                    ],
                    "layout": {
                        "xaxis": {"automargin": True},
                        "yaxis": {"automargin": True},
                        "height": 400,
                        "margin": {"t": 10, "l": 10, "r": 10},
                    },
                },
            )
            for column in ['Close', 'Volume'] #, 'Open']
        ]
    )




