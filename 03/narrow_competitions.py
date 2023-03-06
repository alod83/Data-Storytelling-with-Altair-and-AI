# import the required libraries
# load 'data/competitions.csv' as a pandas dataframe
# select only the columns Training Type, Record Time (Seconds), Our Best Time
# use melt to transform the dataframe into a long format, with the parameter id_vars set to 'Training Type'
# use altair to plot the following chart:
# draw a bar chart showing the values of the column 'value' on the Y axis, the column 'Training Type' on the X axis, the column 'variable' as color
# save the chart as 'competitions.html'

import pandas as pd
import altair as alt

df = pd.read_csv('data/competitions.csv')
df = df[['Training Type', 'Record Time (Seconds)', 'Our Best Time']]
df = pd.melt(df, id_vars='Training Type')
chart = alt.Chart(df).mark_bar().encode(
    x='Training Type',
    y='value',
    color='variable'
)

chart.save('competitions.html')