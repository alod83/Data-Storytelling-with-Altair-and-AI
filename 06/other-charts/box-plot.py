import pandas as pd
import altair as alt

df = pd.read_csv('data/average_internet_speed.csv',parse_dates=['quarter'])


chart = alt.Chart(df).mark_boxplot(
    color='#81c01e',
).encode(
    x=alt.X('quarter:T',
            title=None,
    ),
    y='average latency:Q'
).properties(
    width=600,
    height=300
).configure_view(
    strokeWidth=0
).configure_axis(
    grid=False
)

chart.save('box-plot.html')