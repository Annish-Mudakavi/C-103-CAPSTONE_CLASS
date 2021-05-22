import pandas as pd;
import plotly.express as px;

## We are reading the data from line_chart.csv files.
df = pd.read_csv("line_chart.csv")
fig = px.bar(df, x="Year", y="Per capita income")
fig.show()