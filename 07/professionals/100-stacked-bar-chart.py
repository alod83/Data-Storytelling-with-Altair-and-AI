import pandas as pd
import altair as alt

import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import altair as alt

df = pd.read_csv('../data/competitions.csv')
df = df[['Training Type', 'Record Time (Seconds)', 'Our Best Time']]
# Manually change the column name
df['Percentage'] = 1 - (df['Our Best Time'] - df['Record Time (Seconds)']) / df['Record Time (Seconds)']
# Sort the values by the column 'Percentage'
df = df.sort_values(by='Percentage', ascending=False)

df['Complementary'] = 1 - df['Percentage']
df = df[['Training Type', 'Percentage', 'Complementary']].copy()
df = df.melt('Training Type', var_name='Percentage Type', value_name='Value')

base = alt.Chart(df).encode(
).properties(
    width=300,
    height=300
)

chart = base.mark_bar(
    stroke='#81c01e',
    strokeWidth=2,
    size=30
).encode(
    y=alt.Y('Training Type:N', 
        sort='-x', 
        title='', 
        axis=alt.Axis(labelColor='#81c01e', 
            labelFontWeight='bold', 
            labelFontSize=14
        )
    ),
    x=alt.X('Value', axis=None, stack='normalize'),
    color=alt.Color('Percentage Type:N', 
        scale=alt.Scale(range=['#d9f3b0', 'white'], 
        domain=['Percentage', 'Complementary']),
        legend=None),
    order=alt.Order('Percentage Type:N', sort='descending'),
)

text = base.mark_text(
    color='#81c01e',
    align='left', 
    baseline='middle',
    dx=10
).encode(
    y=alt.Y('Training Type:N', 
        sort='-x', 
        title='', 
        axis=None
    ),
    x=alt.X('Value', axis=None),
    text=alt.Text('Value:Q', format='.2%'),
).transform_filter(
    alt.datum['Percentage Type'] == 'Percentage'
)





chart = (chart + text
).configure_view(
    strokeOpacity=0,
    #stroke='#81c01e'
).resolve_scale(
    y='independent'
)

chart.save('100-stacked-bar-chart.html')