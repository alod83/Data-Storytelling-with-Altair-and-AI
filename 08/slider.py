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
slider = alt.binding_range(min=1960, max=2021,step=1)

select_year = alt.selection_point(name="Select", fields=['Year'],
                                   bind=slider)

# Create visualization
chart = alt.Chart(df).mark_bar(
    color=color
).encode(
        y=alt.Y('Country Name:O', sort='-x', title=''),
        x=alt.X('Population:Q'),
).add_params(
    select_year
).transform_filter(
    select_year
).properties(
    width=600,
    height=300,
    title='Population of Continents'
).configure_view(
    strokeWidth=0
).configure_axis(
    grid=False
)

chart.save('slider.html')