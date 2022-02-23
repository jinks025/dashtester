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
import pandas as pd
import numpy as np 
import plotly.express as px

#######Dataframes##########
df = pd.read_csv('Netflix codes.csv')

ytz = df.sort_values(by = ['Price USD'], ascending = True).head(10) ## top 10 -- lowest
ytn = df.sort_values(by = ['Price USD'], ascending = False).head(10) ## bottom 10 -- highest

####### Graphs #########
fig = px.choropleth(df, locations="country code",
                    color="Price USD",
                    hover_name="Country",
                    hover_data = ['# of TV Shows', '# of Movies', 'Total Library Size'],
                    title = "Netflix prices per country",                 
                    color_continuous_scale='Portland',
                    range_color = (0,10), 
                    margin = dict(t = 0, b=0, l = 0, r = 0))

fig.update_traces(locationmode='Country', selector=dict(type='scattergeo'))

###########DashTable#############
table1 = dash_table.DataTable(ytz.to_dict('records'),
                             [{'name':i, 'id':i} for i in ytz.columns])  #### top 10

table2 = dash_table.DataTable(ytn.to_dict('records'),
                             [{'name':i, 'id':i} for i in ytn.columns])  #### bottom 10

######################Graph layout ###########################
graph1 = dcc.Graph(
    id = 'graph1',
    figure = fig, style = {'width':'40%', 'display':'inline-block'}
)

####################################################
s = html.H1('Netflix Subscription Prices By Country', 
            style = {'color':'white', 'fontSize':50, 'txtAlign':'center', 'background-color':'Black', 'font-family':'courier'})
####################################################
markdown_text = ''' ### Netflix bang for your buck 
\n #### This page shows the current subscription prices for Netflix by country.
\n The map and tables below shows where you get the best bang for your buck.''' 
first = html.Div([dcc.Markdown([markdown_text])],
                 style = {'color':'Black', 'fontSize':15, 'txtAlign':'center', 'background-color':'white', 'font-family':'courier'})

markdown_text1 = """ ### General Findings
##### Netflix is downright convenient. But where is it the best value?
\n Here we find some price disparity between countries. When prices are converted to USD, we can see that Liechtenstein and Switzerland have
the priciest subscription cost. Liechtenstien has it worse while having the smaller library size.
\n Turkey has the best value with the lower subscription cost.""" 
second = html.Div([dcc.Markdown([markdown_text1])], 
                  style = {'color':'Black', 'fontSize':15, 'txtAlign':'center', 'background-color':'white', 'font-family':'courier'})

markdown_text2 = ''' ### News
In January 2022, Netflix announced price hikes in the US and Canada. Netflix also announced that it was lowering prices in India to compete with Amazon Prime and Disney+.'''
thrid = html.Div([dcc.Markdown([markdown_text2])],
                style = {'color':'Black', 'fontSize':15, 'txtAlign':'center', 'background-color':'white', 'font-family':'courier'})

####################################################
BOX_STYLE1 = KOTAK_UTAMA_STYLE
SIDEBAR_STYLE1 = SIDEBAR_STYLE

# content
header = html.Div(children = [s])
graphshere = html.Div(children = [graph1, first])
indicators = html.Div(children = [second, thrid])
comgraph = html.Div(children = [table1, table2], style = {'width':'35%','display':'inline-block'})

kotak_utama1 = html.Div([
    header,
    graphshere,
    indicators,
    comgraph], id='main box1',
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
