import pandas as pd
import altair as alt

# Load data prices_sales.csv as a Pandas dataframe
df = pd.read_csv('prices_sales.csv', parse_dates=['date'])

base = alt.Chart(df).encode(
).properties(
    width=600,
    height=300
)

chart1 = base.mark_line(
    color='#c01e95'
).encode(
    x=alt.X('date:T',
            axis=alt.Axis(title=None)
    ),
    y=alt.Y('price:Q', 
            title='Price', 
            axis=alt.Axis(titleColor='#c01e95',
                          labelColor='#c01e95'))
)

chart2 = base.mark_line(
    color='#81c01e'
).encode(
    x=alt.X('date:T',
            axis=alt.Axis(title=None)
    ),
    y=alt.Y('sales:Q', 
            title='Sales', 
            axis=alt.Axis(titleColor='#81c01e',
                          labelColor='#81c01e'))
)

chart = chart1 + chart2

chart = chart.configure_view(
    strokeWidth=0
).configure_axis(
    grid=False
).resolve_scale(
    y='independent'
)

chart.save('contradictions.html')

