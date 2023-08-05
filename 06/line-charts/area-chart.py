import pandas as pd
import altair as alt

# Load data data/orders.csv as a Pandas dataframe
df = pd.read_csv('data/orders.csv')

df = df.melt(id_vars=['Month'],var_name='Meal Type',value_name='Number of Orders')

# Build a list of months
months = ['January','February','March','April','May','June','July','August','September','October','November','December']

base = alt.Chart(df).encode(
    x=alt.X('Month:N',
            axis=alt.Axis(title=None,
                            labelAngle=0,
                            
            ),
            sort=months
    ),
    y=alt.Y('Number of Orders',axis=alt.Axis(offset=-25)),
    color=alt.Color('Meal Type',scale=alt.Scale(range=['#81c01e','gray']),legend=None)
).properties(
    width=600,
    height=300
)

chart = base.mark_area(line=True)
    
text = base.mark_text(
    fontSize=14,
    baseline='middle',
    align='left',
    dx=10
).encode(
    text=alt.Text('Meal Type:N'),
).transform_filter(
    alt.datum['Month'] == 'December'
)

# Combine the line chart and text mark into a single chart
chart = chart + text

chart = chart.configure_view(
    strokeWidth=0
).configure_axis(
    grid=False
)
chart.save('area-chart.html')
