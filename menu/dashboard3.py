from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import dash
from dash.dependencies import Input, Output, State
from menu.style import *
from app import app, server

########Layout###########

BOX_STYLE3 = KOTAK_UTAMA_STYLE
SIDEBAR_STYLE3 = SIDEBAR_STYLE

#content
kolom_kiri3 = html.Div([])
kolom_tengah3 = html.Div()
kolom_kanan3 = html.Div([])
kolom_peta3 = html.Div()

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
