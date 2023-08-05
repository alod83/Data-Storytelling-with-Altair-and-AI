import pandas as pd
import altair as alt

# Load data data/sales_reviews.csv as a Pandas dataframe
df = pd.read_csv('data/sales_reviews.csv')

width = 300
height = 300

# Build a scatter plot with the following options:
# - Use the `Sales` column for x channel
# - Use the `Ranking` column for y channel
# - Use the `Product` column for color channel

chart = alt.Chart(df).mark_point(
).encode(
    x=alt.X('Sales:Q'),
    y=alt.Y('Reviews:Q'),
    color=alt.Color('Product:N', 
                    scale=alt.Scale(range=['black','lightgray']),
                    legend=alt.Legend(
                        orient='none',
                        legendX=width/2 - 50, legendY=height + 50,
                        direction='horizontal',
                        title=None)
                    ),
    tooltip=alt.Tooltip(['Product:N','Sales:Q','Reviews:Q', 'Ranking:Q']),
    fill=alt.Fill('Product:N',scale=alt.Scale(range=['black','lightgray'])),
    size=alt.Size('Ranking:Q',scale=alt.Scale(range=[1,200]),legend=None)
).properties(
    width=width,
    height=height
).configure_view(
    strokeWidth=0
).configure_axis(
    grid=False
)

chart.save('blubble-chart.html')