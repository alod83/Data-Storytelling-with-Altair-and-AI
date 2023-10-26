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
input_dropdown = alt.binding_select(options=df['Country Name'].unique())
select_country = alt.selection_point(name='Select',fields=['Country Name'], bind=input_dropdown, value=[{'Country Name': 'Africa Eastern and Southern'}])


# Create visualization
chart = alt.Chart(df).mark_line(
    color=color
).encode(
        y=alt.Y('Population:Q', title=''),
        x=alt.X('Year:O'),
).add_params(
    select_country
).transform_filter(
    select_country
).properties(
    width=600,
    height=300,
    title='Population of Continents'
).configure_view(
    strokeWidth=0
).configure_axis(
    grid=False
)

chart.save('dropdown.html')