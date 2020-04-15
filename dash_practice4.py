import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_renderer
import plotly.graph_objs as go
import plotly
import numpy as np
import pandas as pd
from dash.dependencies import Input,Output
from datetime import datetime as dt
app = dash.Dash()

np.random.seed(50)
x_rand = np.random.randint(1,61,60)
y_rand = np.random.randint(1,61,60)

colors = {
    'background': '#111111',
    'text': '#DFE8E8'
}
app.layout = html.Div([
    html.H1("Brain Tumor Detection",
            style= {
                'textAlign' : 'center',
                'color' : colors['text']
            }),
    html.Div("Final Yeat Project",
             style={'backgroundColor': colors['background'],'color':colors['text'],'textAlign' : 'center'}),
    html.Label("Dropdown"),
    html.Br(),
    dcc.Dropdown(
        options= [
            {'label' :'Pakistan', 'value': 'Pak'},
            {'label' :'England', 'value' : 'Eng'},
            {'label' : 'Korea', 'value': 'Kor'}
        ],
        value= 'Pak',
    ),
    html.Br(),
    dcc.Graph(
        id = 'sample graph',
        figure= {
            "data" : [
                {'x' : [1,3,5], 'y': [2,4,5], 'type' : 'bar', 'name' : 'mirza107'},
                {'x' : [2,3,4], 'y' : [3,4,5], 'type': 'bar', 'name': 'usama'}
            ],
            'layout': {
                'title' : 'Sample Graph',
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': 'grey',
                'font': {
                    'color': colors['text']
                }
            }
        },

    ),
    html.Br(),
    dcc.Graph(
        id = 'Scatter Plot',
        figure= {
            'data' : [
                go.Scatter(
                    x = x_rand,
                    y = y_rand,
                    mode = 'markers'
                )
            ],
            'layout' : go.Layout(
                title = 'Scatterplot of random 60 points',
                xaxis = {'title' : 'Random X Values'},
                yaxis = {'title' : 'Random Y Values'}
            )
        }
    ),
    html.Br(),
    html.Div([
        dcc.Input(id = 'my-id', value = 'enter anything here', type = 'text'),
        html.Div(id = 'my-div')
    ]),
    html.Br(),
    html.Label("Slider....."),
    dcc.Slider(
        min = 1,
        max = 10,
        value = 5,
        step= .5,
        marks={i: 'Label {}'.format(i) if i == 1 else str(i) for i in range(1, 10)}
    ),
    html.Label('Checkboxes'),
    dcc.Checklist(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value =['MTL', 'SF']
    ),

    html.Label('Radio items'),
    dcc.RadioItems(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value ='MTL'
    ),
    html.Div(
        dcc.Textarea(
            placeholder= " likho jo likhna",
            value = "placeholder for text",
            style= {'width' : '100%'}
        )
    ),
    html.Br(),
    html.Br(),
    dcc.DatePickerSingle(
        id= "date-picker",
        date= dt(2020,2,2)
    ),
    html.Br(),
    html.Br(),
    dcc.DatePickerRange(
        id= "id-r-picker",
        start_date= dt(1997,6,20),
        end_date_placeholder_text= "select end date"
    )
])

@app.callback(
    Output(component_id= 'my-div', component_property= 'children' ),
    [Input(component_id= 'my-id', component_property= 'value')]
)
def update_output_div(input_value):
    return 'You\'ve entered "{}"'.format(input_value)

if __name__ == '__main__':
    app.run_server(debug= True)