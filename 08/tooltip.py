import pandas as pd
import altair as alt

df = pd.read_csv('data/population.csv')
df = df.melt(id_vars='Country Name', 
             var_name='Year', 
             value_name='Population')

df['Year'] = df['Year'].astype('int')

continents = ['Africa Eastern and Southern',
             'Africa Western and Central',
             'Middle East & North Africa',
              'Sub-Saharan Africa',
             'Europe & Central Asia',
             'Latin America & Caribbean',
             'North America',
             'East Asia & Pacific']

df = df[df['Country Name'].isin(continents)]

color = '#80C11E'

# Create visualization
chart = alt.Chart(df).mark_bar(
    color=color
).encode(
        y=alt.Y('Country Name:O', sort='-x', title=''),
        x=alt.X('Population:Q'),
        tooltip=['Country Name', 'Population']
).transform_filter(
    alt.datum.Year == 2018
).properties(
    width=600,
    height=300,
    title='Population of Continents'
).configure_view(
    strokeWidth=0
).configure_axis(
    grid=False
)

chart.save('tooltip.html')