import pandas as pd
import altair as alt

# Load data
data = {
    'percentage': [0.7,0.3],
    'label'     : ['70%','30%'],
    'color'     : ['#81c01e','lightgray']
}

df = pd.DataFrame(data)

# Draw a donut chart in Altair with the following options:
# - Use the `percentage` column for theta channel
# - Use the `label` column for tooltip
# - Use the `color` column for color
# Save chart to `chart` variable
# Save chart as 'donut-chart.html'

chart = alt.Chart(df).mark_arc(
    innerRadius=100,
    outerRadius=150
).encode( 
    theta='percentage',
    color=alt.Color('color', scale=None),
    tooltip='label'
).properties(
    width=300,
    height=300
)

# Add text to the center of the donut chart
# - Use df.head(1) to get the first row of the dataframe
# - Use the `label` column for text channel
# - Use the `color` column for color

text = alt.Chart(df.head(1)).mark_text(
    align='center',
    baseline='middle',
    fontSize=60,
    fontWeight='bold'
).encode(
    text='label',
    color=alt.Color('color', scale=None)
).properties(
    width=300,
    height=300
) 

# Combine the donut chart and the text chart
# - Use `+` operator to combine the charts
# - Save the combined chart to `chart` variable

chart = (chart + text
).configure_view(
    strokeWidth=0
)


chart.save('donut-chart.html')