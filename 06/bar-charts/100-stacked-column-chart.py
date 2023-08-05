import pandas as pd
import altair as alt

# Load data data/orders.csv as a Pandas dataframe
df = pd.read_csv('data/orders.csv')

df = df.melt(id_vars=['Month'],var_name='Meal Type',value_name='Number of Orders')

# Build a list of months
months = ['January','February','March','April','May','June','July','August','September','October','November','December']

# Transform the following chart into a 100% stacked column chart:
#chart = alt.Chart(df).mark_bar(
#).encode(
#    x=alt.X('Month',
#            axis=alt.Axis(title=None,
#                          labelAngle=0,
#            ),
#            sort=months
#    ),
#    y=alt.Y('Number of Orders'),
#    color=alt.Color('Meal Type',scale=alt.Scale(range=['#81c01e','gray']))
#).properties(
#    width=600,
#    height=300
#).configure_view(
#    strokeWidth=0
#).configure_axis(
#    grid=False
#)

chart = alt.Chart(df).mark_bar(
).encode(
    x=alt.X('Month',
            axis=alt.Axis(title=None,
                            labelAngle=0,
            ),
            sort=months
    ),
    y=alt.Y('Number of Orders',stack='normalize'),
    color=alt.Color('Meal Type',scale=alt.Scale(range=['#81c01e','gray']))
).properties(
    width=600,
    height=300
).configure_view(
    strokeWidth=0
).configure_axis(
    grid=False
)

chart.save('100-stacked-column-chart.html')