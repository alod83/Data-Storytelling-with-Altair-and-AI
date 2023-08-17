import pandas as pd
import altair as alt

# Load data sales.csv as a Pandas dataframe
df = pd.read_csv('sales.csv', parse_dates=['date'])

df = df.melt(id_vars=['date'],var_name='product_category',value_name='number_of_orders')

base = alt.Chart(df).encode(
    color = alt.Color('product_category:N', 
        scale=alt.Scale(
            domain=['headphones','smartphone-covers','usb-cables'],
            range=['#81c01e','gray','gray']
        ),
        legend=None
    ),
    opacity = alt.condition(
        "datum.product_category == 'headphones'",
        alt.value(1),
        alt.value(0.6)
    )
).properties(
    width=600,
    height=300
)

chart = base.mark_line(
).encode(
    x=alt.X('date:T',
            axis=alt.Axis(title=None)
    ),
    y=alt.Y('number_of_orders:Q', title='Number of Orders'),
    strokeWidth=alt.condition(
        "datum.product_category == 'headphones'",
        alt.value(4),
        alt.value(1)
    )
)

text = base.mark_text(
    fontSize=14,
    baseline='middle',
    align='left',
    dx=10
).encode(
    x=alt.X('max(date):T'),
    y=alt.Y('number_of_orders:Q',title='Number of Orders').aggregate(argmax='date'),
    text=alt.Text('product_category:N')
)

# Combine the line chart and text mark into a single chart
chart = chart + text

chart = chart.configure_view(
    strokeWidth=0
).configure_axis(
    grid=False
)

chart.save('curiosity.html')