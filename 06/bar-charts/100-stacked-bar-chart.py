import pandas as pd
import altair as alt

data = {
    'percentage': [0.7,0.3],
    'label'     : ['70%','30%'],
    'color'     : ['#81c01e','lightgray']
}

df = pd.DataFrame(data)

chart = alt.Chart(df).mark_bar(
    size=40
).encode(
    x=alt.X('sum(percentage)', axis=None),
    color=alt.Color("color", scale=None)
).properties(
    width=300
)

text = alt.Chart(df.head(1)).mark_text(
    align='center',
    baseline='middle',
    fontSize=20,
    fontWeight='bold',
    color='lightgrey',
    dx=-30
).encode(
    text='label',
    x='percentage'
).properties(
    width=300
)

chart = (chart + text
).configure_view(
     strokeOpacity=0
)

chart.save('100-stacked-bar-chart.html')