# import the required libraries
# load 'data/competitions.csv' as a pandas dataframe
# select only the columns Training Type, Record Time (Seconds), Our Best Time
# calculate the percentage difference between columns Our Best Time and Record Time (Seconds)  and store it into a new column called Percentage Difference
# use the Altair library to plot the following chart:
# draw a single chart which contains a bar chart showing Percentage Difference on the Y axis and Training Type on the X axis, with the values sorted in descending order (-y)
# set the domain of the Y scale to [0,100], set the width of the chart to 300 pixels 

import pandas as pd
import altair as alt

df = pd.read_csv('data/competitions.csv')
df = df[['Training Type', 'Record Time (Seconds)', 'Our Best Time']]
df['Percentage Difference'] = (df['Our Best Time'] - df['Record Time (Seconds)']) / df['Record Time (Seconds)'] * 100
chart = alt.Chart(df).mark_bar().encode(
    x=alt.X('Training Type', sort='-y'),
    y=alt.Y('Percentage Difference', scale=alt.Scale(domain=[0,100]))
).properties(
    width=300
)

chart.save('competitions.html')
