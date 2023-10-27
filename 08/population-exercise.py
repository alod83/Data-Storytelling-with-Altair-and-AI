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

color='#80C11E'
# build the first chart with only the North America data
base = alt.Chart(df
).encode(
    x = alt.X('Year:Q',
              title=None, 
              axis=alt.Axis(format='.0f',tickMinStep=10)),
    y = alt.Y('Population:Q', 
              axis=alt.Axis(format='.2s'),
              scale=alt.Scale(domain=[1*10**7, 2.5*10**9])
    )

).properties(
    title='Population in North America over the last 50 years',
    width=400,
    height=250
)

na_chart = base.mark_line(
    color=color,
    opacity=1
).transform_filter(
    alt.datum['Country Name'] == 'North America'
)

# Create a list from the continents variables containing all strings except for North America

others = [c for c in df['Country Name'].unique() if c != 'North America']

input_dropdown = alt.binding_select(options=others)
select_country = alt.selection_point(name='Select',fields=['Country Name'], bind=input_dropdown, value=[{'Country Name': 'Africa Eastern and Southern'}])

others_chart = base.mark_line(
    color='grey',
    opacity=0.3
).add_params(
    select_country
).transform_filter(
    select_country
)

chart = (na_chart + others_chart).configure_axis(
    grid=False,
    titleFontSize=14,
    labelFontSize=12
).configure_title(
    fontSize=16,
    color=color
).configure_view(
    strokeWidth=0
)

chart.save('population.html')

