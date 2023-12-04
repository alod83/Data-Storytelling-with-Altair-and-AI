import pandas as pd
import altair as alt

# Load data data/meals.csv as a Pandas dataframe
df = pd.read_csv('data/meals.csv')

# Draw a bar chart in Altair with the following options:
# - Use the `Number of Likes` column for y channel
# - Use the `Meal Type` column for x channel and sort by the number of likes
# - Set the color of the bars to '#81c01e'
# Save chart to `chart` variable
# Save chart as 'bar-chart.html'

chart = alt.Chart(df).mark_bar(
    color='#81c01e'
).encode(
    x=alt.X('Meal Type', 
            sort='-y',
            # Rotate the labels by 0 degrees
            axis=alt.Axis(labelAngle=0,title=None),
    ),
    y=alt.Y('Number of Likes', axis=alt.Axis(grid=False))
).properties(
    width=600,
    height=300
)

# Add a text mark to the chart with the following options:
# - Use the `Number of Likes` column for y channel
# - Use the `Meal Type` column for x channel and sort by the number of likes
# - Set the color of the text to '#81c01e'
# - Set the text to the `Number of Likes` column
# - Set the font size to 14
# - Set the font weight to 600
# - Set the text baseline to 'center'
# - Set the text align to 'middle'
# - Set the y offset to 10

text = alt.Chart(df).mark_text(
    color='#81c01e',
    fontSize=14,
    fontWeight=600,
    baseline='middle',
    align='center',
    dy=-10
).encode(
    x=alt.X('Meal Type',
            sort='-y',
            axis=alt.Axis(labelAngle=0,title=None),
    ),
    y='Number of Likes',
    text='Number of Likes'
)

# Combine the bar chart and text mark into a single chart
chart = chart + text

chart = chart.configure_view(
    strokeWidth=0
)

chart.save('column-chart.html')

