# Import Pandas and Altair
import pandas as pd
import altair as alt

# Load data data/orders.csv as a Pandas dataframe
df = pd.read_csv('data/orders.csv')

months = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

left_base = alt.Chart(df).encode(
    y=alt.Y('Month:N', axis=None, sort=months),
    x=alt.X('Pizza:Q', title='',sort=alt.SortOrder('descending'), axis=None),
)

left =  left_base.mark_bar(
    size=20,
    color='#c01e95'
).properties(
    title='Pizza',
    width=300,
    height=300
)

# Add a text mark to the chart with the following options:
# - Use the `Month` column for y channel
# - Use the `Pizza` column for text channel
# - Set the text baseline to 'middle'
# - Set the text align to 'right'
# - Set the x offset to -10
# - Set the color of the text to '#c01e95'

left_text = left_base.encode(
    text=alt.Text('Pizza:N'),
).mark_text(
    color='#c01e95',
    baseline='middle',
    align='right',
    dx=-10,
)

middle = alt.Chart(df
).encode(
    y=alt.Y('Month:N', axis=None, sort=months),
    text=alt.Text('Month:N'),
).mark_text(
    size=15,
    color='#000000'
).properties(
    width=80,
    height=300,
    title='Number of orders in 2023'
)

right_base =  alt.Chart(df
).encode(
    y=alt.Y('Month:N', axis=None,sort=months),
    x=alt.X('Spaghetti:Q', title='',axis=None),
)

right = right_base.mark_bar(
    size=20,
    color='#81c01e'
).properties(
    title='Spaghetti',
    width=300,
    height=300
)

right_text = right_base.encode(
    text=alt.Text('Spaghetti:Q')
).mark_text(
    baseline='middle',
    align='left',
    dx=10,
    color='#81c01e'
)

chart = left + left_text | middle | right + right_text

chart = chart.configure_view(
    strokeWidth=0
)
# save chart as 'pyramid-chart.html'
chart.save('pyramid-chart.html')