import plotly.express as px


df = px.data.gapminder()
df.head()

df2007 = df.query("year == 2007")
df2007.head()

px.histogram(df, x= 'lifeExp', color= 'continent', marginal= 'rug',
                   hover_name= 'country', hover_data= df2007.columns, y= "pop",
                   histfunc="sum")
px.sunburst(df2007, path= ["continent","country"], color= 'lifeExp',
                   hover_name= 'country', hover_data= df2007.columns, values= "pop",)
px.histogram(df2007, x= 'lifeExp', color= 'continent', marginal= 'rug',
                   hover_name= 'country', hover_data= df2007.columns, y= "pop",
                   histfunc="sum")
px.choropleth(df2007, locations = "iso_alpha", color= 'lifeExp',
                   hover_name= 'country', hover_data= df2007.columns)
px.scatter(df2007, x= 'gdpPercap',y= 'lifeExp', color= 'continent', log_x= True,
                 hover_data= df2007.columns,size= "pop", hover_name= "country")
px.scatter(df2007, x= 'gdpPercap',y= 'lifeExp', color= 'continent', log_x= True,
                 hover_data= df2007.columns,size= "pop", hover_name= "country",
                 size_max=45, facet_row="continent")
px.scatter(df2007, x= 'gdpPercap',y= 'lifeExp', color= 'continent', log_x= True,
                 hover_data= df2007.columns,size= "pop", hover_name= "country",
                 size_max=45, facet_col="continent", facet_col_wrap=3)