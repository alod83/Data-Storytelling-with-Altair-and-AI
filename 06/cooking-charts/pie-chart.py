import pandas as pd
import altair as alt

# Load data
data = {
    'percentage': [0.7,0.3],
    'label'     : ['70%','30%'],
    'color'     : ['#81c01e','lightgray']
}

df = pd.DataFrame(data)

# Draw a pie chart in Altair with the following options:
# - Use the `percentage` column for theta channel
# - Use the `label` column for tooltip
# - Use the `color` column for color
# Save chart to `chart` variable
# Save chart as 'pie-chart.html'

chart = alt.Chart(df).mark_arc(
).encode(
    theta=alt.Theta('percentage', stack=True),
    color=alt.Color('color', scale=None),
    tooltip='label'
).properties(
    width=300,
    height=300
)

# Add text near to each slice of the pie chart
# - Use the `label` column for text channel
# - Use the `color` column for color

text = chart.mark_text(
    size = 20,
    radius=180
).encode(
    text='label',
    color=alt.Color('color', scale=None)
).properties(
    width=300,
    height=300
)

# Combine the pie chart and the text chart
# - Use `+` operator to combine the charts
# - Save the combined chart to `chart` variable

chart = (chart + text
).configure_view(
    strokeWidth=0
)

chart.save('pie-chart.html')




