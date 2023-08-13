# Import the required libraries
# Load the 'data/product-ratings.csv' into a dataframe
# Create a histogram of the Pizza column using Altair
# Save the chart as a HTML file

import pandas as pd
import altair as alt

df = pd.read_csv('data/product-ratings.csv')

chart = alt.Chart(df).mark_bar(
    color='#81c01e'
).encode(
    x=alt.X('Rating:Q',
            bin=alt.Bin(maxbins=10, extent=[1, 10]),
            title='Rating',
            axis=alt.Axis(
                format='d',
            )
    ),
    y=alt.Y('count()', title='Number of Products')
)





line = alt.Chart(df).transform_density(
    'Rating',
    as_=['rating', 'density'],
).mark_line(
    color='red',
).encode(
    x='rating:Q',
    y=alt.Y('density:Q', axis=None)
)

# combine the bar chart and the density estimator
chart = chart + line

chart = chart.resolve_scale(y='independent'
).configure_view(
    stroke=None
).configure_axis(
    grid=False
)


chart.save('histogram.html')



