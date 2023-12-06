# Import the required libraries
# Load '../data/competitions.csv' as pandas dataframe
# Select only the columns Training Type, Record Time (Seconds), Our Best Time
# Calculate the percentage difference between columns Our Best Time and Record Time (Seconds)  and store it into a new column called Percentage Difference
# Draw a bar chart with the following encodings:
# * The Percentage Difference on the y-axis with the following properties:
#   - The domain of the Y scale to [0,100]
# * Training Type on the x-axis with the following properties:
#   - The values sorted in descending order (-y)
# Set the following properties of the bar chart:
# * width to 300 pixels
# Save the chart as 'competitions.html'

import pandas as pd
import altair as alt

df = pd.read_csv('source/competitions.csv')
df = df[['Training Type', 'Record Time (Seconds)', 'Our Best Time']]
df['Percentage Difference'] = (df['Our Best Time'] - df['Record Time (Seconds)']) / df['Record Time (Seconds)'] * 100

chart = alt.Chart(df).mark_bar().encode(
    y=alt.Y('Percentage Difference', scale=alt.Scale(domain=[0, 100])),
    x=alt.X('Training Type', sort='-y')
).properties(
    width=300
)

chart.save('competitions.html')