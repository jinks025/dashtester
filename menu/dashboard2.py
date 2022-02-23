from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import dash
from dash.dependencies import Input, Output, State
from menu.style import *
from app import app, server
		   
			   

#####################################

BOX_STYLE2 = KOTAK_UTAMA_STYLE
SIDEBAR_STYLE2 = SIDEBAR_STYLE

#content
kolom_kiri2 = html.Div(children = [])
kolom_tengah2 = html.Div(children = [])
kolom_kanan2 = html.Div(children = [])
kolom_peta2 = html.Div(children = [])

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

