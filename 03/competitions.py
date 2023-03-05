# import the required libraries
# load 'data/competitions.csv' as a pandas dataframe
# select only the columns Training Type, Record Time (Seconds), Our Best Time
# calculate the difference between columns Record Time (Seconds) and Our Best Time and store it into a new column called Difference
# order the dataset by the Difference column
# use the Altair library to plot the following chart:
# draw a single chart which contains a bar chart for the column Our Best Time and a line chart for the column Record Time (Seconds)


import pandas as pd
import altair as alt

df = pd.read_csv('data/competitions.csv')
df = df[['Training Type', 'Record Time (Seconds)', 'Our Best Time']]
df['Difference'] =  (df['Our Best Time'] - df['Record Time (Seconds)'])/df['Record Time (Seconds)']*100

df = df.sort_values('Difference')

print(df)

chart = alt.Chart(df).mark_bar().encode(
    x='Training Type',
    y='Our Best Time'
).properties(width=500)

line = alt.Chart(df).mark_line(color='red').encode(
    x='Training Type',
    y='Record Time (Seconds)'
)

(chart + line).save('chart.html')

