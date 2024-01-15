import pandas as pd
import altair as alt

# Load the dataset data/fakenews.csv
df = pd.read_csv('data/fakenews.csv')

# Create a column chart of the number of articles per category
# - Use the `Category` column for x channel
# - Use the `Number of Articles` for y channel

chart = alt.Chart(df).mark_bar(
    color='#81c01e'
).encode(
    x=alt.X('Category:N', 
            sort='-y',
            title=None,
            axis=alt.Axis(labelFontSize=14)
            ),
    y=alt.Y('Percentage of Fake Articles:Q',
            axis=alt.Axis(labelFontSize=14, titleFontSize=14)
            )
).properties(
    width=400,
    height=300
).configure_axis(
    grid=False
).configure_view(
    strokeWidth=0
).transform_calculate(
    'Percentage of Fake Articles', alt.datum['Number of Fake Articles']/alt.datum['Number of Articles']*100
)

chart.save('raw-chart.html')
