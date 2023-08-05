import pandas as pd
import altair as alt

# Load data data/meals.csv as a Pandas dataframe
df = pd.read_csv('data/meals.csv')

# Draw a bar chart in Altair with the following options:
# - Use the `Number of Likes` column for x channel
# - Use the `Meal Type` column for y channel and sort by the number of likes
# - Set the color of the bars to '#81c01e'
# Save chart to `chart` variable
# Save chart as 'bar-chart.html'

chart = alt.Chart(df).mark_bar(
    color='#81c01e'
).encode(
    y=alt.Y('Meal Type', sort='-x', title=None),
    x=alt.X('Number of Likes',axis=None)
).properties(
    width=300,
    height=300
)

# Add text to the end of each bar
# - Use the `Number of Likes` column for text channel
# - Use the `Meal Type` column for y channel and sort by the number of likes
# - Set the color of the text to '#81c01'
# - Set the text alignment to 'left'
# - Set the text baseline to 'middle'
# - Set font size to 14

text = chart.mark_text(
    align='left',
    baseline='middle',
    dx=3,
    color='#81c01',
    fontSize=14
).encode(
    text='Number of Likes',
    y=alt.Y('Meal Type', sort='-x', title=None)
)

# Add five vertical lines to the chart
# - Use alt.Chart(pd.DataFrame({'x': [20, 40, 60, 80, 100]})) to create a dataframe with six rows
# - Use alt.Chart().mark_rule() to draw vertical lines
# - Set the color of the lines to 'white'
# - Set the line width to 1
# - Set opacity to 0.5

lines = alt.Chart(pd.DataFrame({'x': [20, 40, 60, 80, 100]})).mark_rule(
    color='white',
    strokeWidth=1,
    opacity=0.5
).encode(
    x='x:Q'
)


# Combine the bar chart, the text and the line chart
# - Use `+` operator to combine the charts
# - Save the combined chart to `chart` variable

chart = (chart + text + lines
).configure_view(
    strokeWidth=0
).configure_axis(
    grid=False
)


chart.save('bar-chart.html')

