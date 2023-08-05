import pandas as pd
import altair as alt

df = pd.read_csv('data/average_internet_speed.csv',parse_dates=['quarter'])


chart = alt.Chart(df
# explain the following line:
).transform_density( # Transform the data into density curves
    'average latency',
    as_=['average latency', 'density'],
    groupby=['quarter']
).mark_area(
    orient='horizontal',
    color='#81c01e',
).encode(
    y=alt.Y('average latency:Q', 
            title='Average latency'),
    x=alt.X('density:Q',
        # explain the following line:
        stack='center', # Center the density curves around the y-axis
        # explain the following line:
        impute=None, # Remove all the values that are outside the range of the data
        axis=alt.Axis(title=None, labels=False)
    ),
    # explain the following line:
    facet=alt.Facet( # Create a facet for each quarter
        'quarter:T',
        header=alt.Header(
            labelOrient='bottom',
            title=None,
        )
    )
).properties(
    width=60
).configure_view(
    strokeWidth=0
).configure_axis(
    grid=False
)

chart.save('violin-plot.html')