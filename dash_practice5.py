import dash
import dash_renderer
import dash_html_components
import dash_core_components
import dash_auth
import plotly

VALID_USERNAME_PASSWORD_PAIRS = [
    ['hello', 'world']
]
app = dash.Dash('auth')
auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)

if __name__ == '__main__':
    app.run_server(port = 2020)
    #app.run_server(debug= True)


