import dash
import dash_renderer
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from iexfinance.stocks import get_historical_data
from dateutil.relativedelta import relativedelta
from dash.dependencies import Input, Output
import datetime
import pandas

start = datetime.datetime.today() - relativedelta(years = 5)
end = datetime.datetime.today()

inputStock = "YZ"
df = get_historical_data(inputStock, start = start, end= end, output_format= "pandas", token = 'pk_53517bd9b48e4c41ac276a53dd47af06')

trace_close = go.Scatter( x = list(df.index),
                          y = list(df.close),
                          name = "Close",
                          line = dict(color = "#f44242"))
trace_high = go.Scatter( x = list(df.index),
                          y = list(df.high),
                          name = "Close",
                          line = dict(color = "#f44242"))

app = dash.Dash()
app.layout = html.Div([

    html.Div([
        html.H2("Stock App Sample"),
        html.img(src= ""),

    ], className = "banner"),
    html.Div([
        html.Div([
            html.H3("Colunm 1"),
            dcc.Graph(
                id= "graph_close",
                figure= {
                    "date" : [trace_close],
                    "layout" : {
                        "title" : "Close Graph"
                    }
                }
            )
        ], className= "six columns"),
        html.Div([
            html.H3("Colunm 2"),
            dcc.Graph(
                id= "graph_high",
                figure= {
                    "date" : [trace_high],
                    "layout" : {
                        "title" : "High Graph"
                    }
                }
            )
        ], className= "six columns")
    ]),
app.css.append_css({
    'external_url' : 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})
])

@app.callback(dash.dependencies.Output("graph_close","figure"),
              [dash.dependencies.Input("stock-input", "value")])
def update_fig(input_value):
    df = get_historical_data(inputStock, start = start, end= end, output_format= "pandas", token = 'pk_53517bd9b48e4c41ac276a53dd47af06')

    data = []
    trace_close = go.Scatter( x = list(df.index),
                              y = list(df.close),
                              name = "Close",
                              line = dict(color = "#f44242"))
    data.append(trace_close)
    layout = {'title': 'classback Graph'}
    return{
        'data' : data,
        'layout' : layout
    }

if __name__ == '__main__':
    app.run_server(debug= True)