import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_renderer
import dash_table
import plotly

app = dash.Dash()
colors = {
    'background': '#111111',
    'text':'#7FDBFF',
    'bg' : '#593A31',
    'txt' : '#1F0903'
}
app.layout = html.Div(style={'backgroundColor':colors['background']}, children=[
    html.H1(children="Ao g mirza sb ",
            style= {'textAlign' : 'center',
                    'color': colors['text']}),
    html.Div(children= "Dash: A WEB Framework for Python.",
             style={'textAlign': 'center',
                    'color': colors['text']}),
    dcc.Graph(
        id = "Graph1",
        figure= {
            'data' : [
                {'x': [1,2,3], 'y': [4,1,2], 'type': 'bar', 'name':'SF'},
                {'x': [1,2,3], 'y': [2,4,5], 'type': 'bar', 'name': u'Monitréal'},
            ],
            'layout' : {
                'plot_bgcolor' : colors['bg'],
                'paper_bgcolor' : colors['bg'],
                'font' : {
                    'color' : colors['txt']
                }
            }
        }
    )
]
)

if __name__ == "__main__":
    app.run_server(debug= True)