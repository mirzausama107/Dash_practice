import dash
import dash_core_components
import dash_html_components
import dash_renderer
import datetime
from dateutil.relativedelta import relativedelta
import plotly.graph_objs as go

start = datetime.datetime.today() - relativedelta(years=5)
end = datetime.datetime.today()

inputStock = "XY"
df = get_historical