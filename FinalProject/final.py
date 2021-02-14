
import pandas as pd
import pycountry
import dash
from dash.dependencies import Input, Output
import plotly.express as px
import dash_core_components as dcc
import dash_html_components as html
import plotly
import plotly.graph_objs as go
import numpy as np
import datetime
import dash_bootstrap_components as dbc
import pandas_datareader.data as web
from pandas import DataFrame
import dash_table

df=pd.read_csv("file_name1.csv")
comp = df.Name.unique() 
opt = []
for i in comp:
    opt.append(i)
    
st = datetime.datetime(2017,1,1)
en = datetime.datetime.now()
df_cip = web.DataReader('CIPLA.NS','yahoo',st,en)
df_hero = web.DataReader('HEROMOTOCO.NS','yahoo',st,en)
df_rel = web.DataReader('RELIANCE.NS','yahoo',st,en)

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=df_hero.index,
    y = ((df_hero.High - df_hero.Low)/(df_hero.High))*100,
    name = 'Hero',
))
fig.add_trace(go.Scatter(
    x = df_rel.index,
    y = ((df_rel.High - df_rel.Low)/(df_rel.High))*100,
    name='Reliance',
))
fig.add_trace(go.Scatter(
    x=df_hero.index,
    y = ((df_cip.High - df_cip.Low)/(df_cip.High))*100,
    name='CIPLA',
))

fig.update_layout(
    title_text="<b><i>Precentage (%) profit of Each Day</i></b>."
)
fig.update_xaxes(title_text="<b>Date</b>")
fig.update_yaxes(title_text="<b>% Proft</b>")



fig1 = go.Figure()

fig1.add_trace(go.Scatter(
    x=df_hero.index,
    y = df_hero.Volume,
    name = 'Hero',
))
fig1.add_trace(go.Scatter(
    x = df_rel.index,
    y = df_rel.Volume,
    name='Reliance',
))
fig1.add_trace(go.Scatter(
    x=df_hero.index,
    y = df_cip.Volume,
    name='CIPLA',
))
fig1.update_layout(
    title_text="<b><i>Volume Chnage Each Day</i></b>."
)
fig1.update_xaxes(title_text="<b>Date</b>")
fig1.update_yaxes(title_text="<b>Volume</b>")

fig2 = go.Figure()

fig2.add_trace(go.Scatter(
    x=df_hero.index,
    y = df_hero["Adj Close"],
    name = 'Hero',
))
fig2.add_trace(go.Scatter(
    x = df_rel.index,
    y = df_rel["Adj Close"],
    name='Reliance',
))
fig2.add_trace(go.Scatter(
    x=df_hero.index,
    y = df_cip["Adj Close"],
    name='CIPLA',
))
fig2.update_layout(
    title_text="<b><i>Adj Close Each Day</i></b>."
)
fig2.update_xaxes(title_text="<b>Date</b>")
fig2.update_yaxes(title_text="<b>Adj Close</b>")

#app = dash.Dash(__name__,external_stylesheets=[dbc.themes.CYBORG])

tab1 = html.Div([
    
    html.Br(),
    html.Div([
        html.H2("General Stock Market Analysis", style={"textAlign": "center"}),
    ], className="cls"),

    html.Br(),
        
    html.Label("Select Stock Company : "),
    html.Br(),
    
    dcc.Dropdown(
        id='dropdown',
        options=[
            {'label': 'CIPLA', 'value': 'CIPLA.NS'},
            {'label': 'Hero MotoCop', 'value': 'HEROMOTOCO.NS'},
            {'label': 'Reliance', 'value': 'RELIANCE.NS'}
        ],
        value='RELIANCE.NS'
    ),
    html.Br(),
    html.Label("Enter Date you want to get stock analysis from, here :   "),
    dcc.Input(id='input',value='2017-01-01',type='text'),
    
    html.Div(id='output-graph'),
    html.Hr(className="abc"),
    
   html.Div(         

        dcc.Graph(
        id='example-graph-2',
        figure=fig
        )
   ),
    html.Hr(className="abc"),
    
    html.Div(         

        dcc.Graph(
        id='example-graph-3',
        figure=fig1
        )
   ),
    html.Hr(className="abc"),
    html.Div(         

        dcc.Graph(
        id='example-graph-4',
        figure=fig2
        )
   )
    
])

            


tab2 = html.Div([
    
    html.Br(),
    html.H2("Specific info here", style={'text-align': 'center'}),

    dcc.Dropdown(id = 'menu_select11',
    options =[
        {'label': '1 months', 'value': '1 month'},
        {'label': '3 months', 'value': '3 months'},
        {'label': '6 months', 'value': '6 months'},
        {'label': '9 months', 'value': '9 months'},
        {'label': '12 months', 'value': '12 months'},
       
    ],
        multi=False,
        value="",
        style={'width': "40%"}
    ),
    dcc.Input(id='input11', value='5000', type='number'),

    html.Div(id='output_container',children=[]),
    html.Br(),
    html.Div(id='output-graph1'),
   

    #dcc.Graph(id='my_bee_map',figure={}),
    ])


tab3= html.Div(children=[
    
        html.Br(),
        html.H2("Find out how long should u invest in a particular stock..", style={'text-align': 'center'}),
        
        html.Br(),
        dcc.Dropdown(id = 'slct_st2',
            options = [{'label':name, 'value':name} for name in opt],
            multi=False,
            value="RELIANCE.NS",
            style={'width': "40%"}
        ),
        
        html.Br(),
        html.Div(id='tab2_container',children=[],style={'text-align': 'center'}),
        html.Br(),
        
         html.Div(
                id='cx1'
                )        
        ])


app = dash.Dash(__name__,external_stylesheets=[dbc.themes.SOLAR])
theme =  {
    'dark': True,
    'detail': '#007439',
    'primary': '#00EA64',
    'secondary': '#6E6E6E',
}

app.layout = html.Div([
    html.H2('Interactive Stock Market Analysis',style={'text-align': 'center'}),
    html.H5('- Aman Agarwal(18BIT0256), Aman Goel(18BCE0895) & Paras(18BCE0906)',style={'text-align': 'center'}),
    html.Br(),
    dcc.Tabs(id="tabs-example", value='tab-1-example', children=[
        dcc.Tab(id="tab-1", label='General Analysis', value='tab-1-example'),
        dcc.Tab(id="tab-2", label='Specific Analysis', value='tab-2-example'),
        dcc.Tab(id="tab-3", label='How long to invest ?', value='tab-3-example'),
    ]),
    html.Div(id='tabs-content-example',
             children = tab1)
])


@app.callback(Output('tabs-content-example', 'children'),
             [Input('tabs-example', 'value')])
def render_content(tab):
    if tab == 'tab-1-example':
        return tab1
    elif tab == 'tab-2-example':
        return tab2
    elif tab == 'tab-3-example':
        return tab3
    
@app.callback(
    Output(component_id='output-graph',component_property='children'),
    [Input('dropdown', 'value')], 
    [Input(component_id='input',component_property='value')])

def update_output1(value,date):
    
    l = date.split('-')
    print(l)
    year = int(l[0])
    month = int(l[1])
    day = int(l[2])
    start = datetime.datetime(year,month,day)
    end = datetime.datetime.now()
    df = web.DataReader(value,'yahoo',start,end)
    
    return dcc.Graph(
                id='example-graph',
                figure={
                        'data': [
                                    {'x': df.index,'y':df.Close,'type':'line','name':value},
                                ],
                        'layout':{
                                'title':value,                        
                                'xaxis':{
                                'title':'<b>Date</b>'
                                },
                                'yaxis':{
                                    'title':'<b>Value of the Stock</b>'
                                }
                        }
                }
        )

@app.callback(
    Output(component_id='output-graph1', component_property='children'),
    [Input(component_id='menu_select11',component_property='value'),
    Input(component_id='input11', component_property='value')]
)
def update_output2(option_slctd,input1):
    
    df=pd.read_csv("file_name1.csv")
    dfff=df.copy()
    i1=float(input1)
    
    if(option_slctd=='1 month'):
        
        dfff =df[['Name','month1']].copy()
        dfff=dfff.sort_values(by=['month1'], ascending=False)
        dfff['returns'] =  df['month1'].map(lambda a: i1+(a*int(i1)/100))
        print(dfff)
        return [dash_table.DataTable(
        id='table',
        columns=[{"name": i, "id": i} for i in dfff.columns],
        data=dfff.to_dict('records'),
        ),
        dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': dfff.Name, 'y': df.month1, 'type': 'bar', 'name': 'input_data'},
            ],
            'layout': {
                'title': "Analysis of different companies"
            }
        }
    )
    
    ]
   
    if(option_slctd=='3 months'):
        dfff =df[['Name','months3']].copy()
        dfff=dfff.sort_values(by=['months3'], ascending=False)
        dfff['returns'] =  df['months3'].map(lambda a: i1+(a*int(i1)/100))
        print(dfff)
        return [dash_table.DataTable(
        id='table',
        columns=[{"name": i, "id": i} for i in dfff.columns],
        data=dfff.to_dict('records'),
        ),
        dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': dfff.Name, 'y': df.months3, 'type': 'bar', 'name': 'input_data'},
            ],
            'layout': {
                'title': "Analysis of different companies"
            }
        }
    )
    
    ]
  
    if(option_slctd=='6 months'):
        dfff =df[['Name','months6']].copy()

        dfff=dfff.sort_values(by=['months6'],ascending=False)
        dfff['returns'] =  df['months6'].map(lambda a: i1+(a*int(i1)/100))
        print(dfff)
        return [dash_table.DataTable(
        id='table',
        columns=[{"name": i, "id": i} for i in dfff.columns],
        data=dfff.to_dict('records'),
        ),
        dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': dfff.Name, 'y': df.months6, 'type': 'bar', 'name': 'input_data'},
            ],
            'layout': {
                'title': "Analysis of different companies"
            }
        }
    )
    
    ]
      
    if(option_slctd=='9 months'):
        dfff =df[['Name','months9']].copy()

        dfff=dfff.sort_values(by=['months9'], ascending=False)
        dfff['returns'] =  df['months9'].map(lambda a: i1+(a*(i1)/100))
        print(dfff)
        return [dash_table.DataTable(
        id='table',
        columns=[{"name": i, "id": i} for i in dfff.columns],
        data=dfff.to_dict('records'),
        ),
        dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': dfff.Name, 'y': df.months9, 'type': 'bar', 'name': 'input_data'},
            ],
            'layout': {
                'title': "Analysis of different companies"
            }
        }
    )
    
    ]
        
    if(option_slctd=='12 months'):
        dfff =df[['Name','months12']].copy()

        dfff=dfff.sort_values(by=['months12'], ascending=False)
        dfff['returns'] =  df['months12'].map(lambda a: i1+(a*int(i1)/100))
        print(dfff)
        return [dash_table.DataTable(
        id='table',
        columns=[{"name": i, "id": i} for i in dfff.columns],
        data=dfff.to_dict('records'),
        ),
        dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': dfff.Name, 'y': df.months12, 'type': 'bar', 'name': 'input_data'},
            ],
            'layout': {
                'title': "Analysis of different companies"
            }
        }
    )
    
    ]
      
@app.callback(
    [Output(component_id = 'tab2_container',component_property='children'),
    Output(component_id='cx1',component_property = 'children')],
    [Input(component_id='slct_st2',component_property='value')]
)

def update_output3(value):
    
    df=pd.read_csv("file_name1.csv")
    
    df1 = df[df["Name"]==value]
    ind = list(np.where(df["Name"]==value))
    ind = ind[0][0] 
    x1 = ['One','Three','Six','Nine','Twelvew']
    y1 = [df1['month1'][ind],df1['months3'][ind],df1['months6'][ind],df1['months9'][ind],df1['months12'][ind]]
    #print(df1['month1'])

    
    x1 = DataFrame(x1,columns=['Months'])
    y1 = DataFrame(y1,columns=['Profit'])
       
    df_new = pd.concat([x1,y1],axis=1)

       
    df_new = pd.concat([x1,y1],axis=1)
    
    temp3 = px.bar(df_new, x='Months', y='Profit')
    
    fig3 = html.Div(
            dcc.Graph(
                id='bar chart',
                figure=temp3,
            )
    ) 
    

    maxi = max(y1.values)
    cnt=1
    for i in y1:
        if maxi[0]==i:
            break
        else:
            if cnt==1:
                cnt=3
            else:
                cnt = cnt+3
    
    container1 = "Maxinum expected profit is {} %".format(maxi[0])
 
   # container1 = "Suggested invest duration is {} & esmtimated profit is {} %".format(10,value)
    return container1, fig3




    
if __name__ == '__main__':
    app.run_server(debug=True,port=8074)

