import dash
import dash_renderer
import dash_html_components as html
import dash_core_components as dcc
import json
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets)

styles = {
    'pre' : {
        'border' : 'thin lightgrey solid',
        'overflowX' : 'scroll'
    }
}

app.layout = html.Div([
    dcc.Graph(
        id = 'basic-interactions',
        figure= {
            'data' : [
                {
                    'x' : [1,2,3,4],
                    'y' : [4,1,3,5],
                    'text' : ['a','b','c','d'],
                    'customdata' : ['c.a', 'c.b', 'c.c','c.d'],
                    'name' : 'Trace 1',
                    'mode' : 'markers',
                    'markers' : {'size' : 12}
                },
                {
                    'x' : [1,2,3,4],
                    'y' : [9,4,1,4],
                    'text' : ['w','x','y','z'],
                    'customdata' : ['c.w', 'c.x', 'c.y','c.z'],
                    'name' : 'Trace 2',
                    'mode' : 'markers',
                    'markers' : {'size' : 12}
                }
            ],
            'layout' : {
                'clickmode' : 'event+select'
            }
        }
    ),

])