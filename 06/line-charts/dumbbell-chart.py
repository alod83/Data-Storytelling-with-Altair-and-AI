import pandas as pd
import altair as alt

# Load data data/orders.csv as a Pandas dataframe
df = pd.read_csv('data/orders.csv')

df = df.melt(id_vars=['Month'],var_name='Meal Type',value_name='Number of Orders')

# Build a list of months
months = ['January','February','March','April','May','June','July','August','September','October','November','December']

chart = alt.Chart(df).encode(
    y=alt.Y('Meal Type:N',
            axis=alt.Axis(title=None)
    ),
    x=alt.X('Number of Orders'),
    color=alt.Color('Meal Type',scale=alt.Scale(range=['#81c01e','gray']),legend=None)
).properties(
    width=600,
    height=300
).transform_filter(
    (alt.datum['Month'] == 'December') | (alt.datum['Month'] == 'January')
).mark_line(
    point=True,
    strokeWidth=4
).configure_view(
    strokeWidth=0
).configure_point(
    size=100
)

chart.save('dumbbell-chart.html')
