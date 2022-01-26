import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from menu.style import *
from app import app, server

# Add dashboard specific methods here

BOX_STYLE4 = KOTAK_UTAMA_STYLE
SIDEBAR_STYLE4 = SIDEBAR_STYLE

#content
kolom_kiri4 = html.Div([])
kolom_tengah4 = html.Div([])
kolom_kanan4 = html.Div([])
kolom_peta4 = html.Div([])

mainbox4 = html.Div([
    kolom_kiri4,
    kolom_tengah4,
    kolom_kanan4,
    kolom_peta4],id='main box4',
      style=BOX_STYLE4
                      )

#sidebar
sidebar4 = html.Div(
    [html.Img(src=app.get_asset_url('logo.png'),style={
                        'height':'116px', 
                        'width':'138px',
                        'margin-top': '-9px',
                        'background-color' : 'rgba(0,0,0,0.03)'}),
        #html.Hr(),
        html.P([
            "TEXT FOR LOGO", html.Br(),"ANOTHER TEXT LINE", html.Br(), "MORE TEXT LINE"], className="lead", 
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
    style=SIDEBAR_STYLE4,
)
content4 = html.Div([
            html.H1(['TITLE FOR DASHBOARD IV'],
              style={
              'margin-left': '340px',
              'margin-top': '20px',
              'color': 'rgba(255,255,255,1)',
              'fontSize': '18',
              }),     


             mainbox4,
            
              ],style={
              'margin-left': '0px',
              'margin-top': '0px',}
              )


layout4 = html.Div([dcc.Location(id="url"), sidebar4, content4])
