import pandas as pd
import altair as alt

df = pd.read_csv('source/homeless.csv')

# Data Cleaning
df['Territory'] = df['Territory'].str.replace('Trentino Alto Adige', 'Trentino-Alto Adige/Südtirol')

# Focus on total age, total sex and total citizenship
df = df[(df['Age'] == 'TOTAL') & (df['Sex'] == 'T') &  (df['Citizenship'] == 'TOTAL')]

chart = alt.Chart(df).mark_bar(
    color='#80C11E'
).encode(
    y = alt.Y('Territory', 
              sort='-x', 
              axis=alt.Axis(title='')),
    x = alt.X('Value', 
              axis=alt.Axis(tickCount=4,title='Number of homeless people'))
).properties(
    width=500,
    title='Homelessness in Italy in 2021'
)

chart = chart.configure_title(
    fontSize=20,
    offset=25
).configure_axis(
    grid=False
).configure_view(
    strokeWidth=0
)

chart.save('bar-chart.html')