import pandas as pd;
import plotly.express as px;

# We are plotting an line chart using data.csv file
df = pd.read_csv("line_chart.csv")
fig = px.line(df, x="Year", y= "Per capita income", color="Country", title= "Per capita income of some countries")
fig.show()