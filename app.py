import dash
import dash_renderer
import dash_core_components as dcc
import dash_html_components as html
import plotly


from iexfinance.stocks import get_historical_data
import datetime
from dateutil.relativedelta import relativedelta
import plotly.graph_objects as go

start = datetime.datetime.today() - relativedelta(years= 5)
end = datetime.datetime.today()

df = get_historical_data("GE" , start= start, end= end, output_format= "pandas", token = "pk_53517bd9b48e4c41ac276a53dd47af06") #dataframe => df
print(df.head())

# app = dash.Dash()
#
# app.layout = html.Div(
#     html.H1(children="Ao g mirza sb ")
# )
#
# if __name__ == "__main__":
#     app.run_server(debug= True)