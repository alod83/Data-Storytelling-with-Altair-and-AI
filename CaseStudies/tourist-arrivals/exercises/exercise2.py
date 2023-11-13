import altair as alt
import pandas as pd

df = pd.read_csv('../source/tourist_arrivals_countries.csv', parse_dates=['Date'])

df = pd.melt(df, id_vars='Date', value_name='Tourist Arrivals', var_name='Country')

# extract year from date
df.loc[:, 'Year'] = df['Date'].dt.year

# group by year and country
df = df.groupby(['Year', 'Country'])['Tourist Arrivals'].sum().reset_index()

# select only 1994 and 2018
df = df[(df['Year'] == 1994) | (df['Year'] == 2018)]

# add a new column containing the difference for each country between the number of tourist arrivals in the year and 1994
for country in df['Country'].unique():
    current = df[df['Country'] == country]['Tourist Arrivals']
    base = df[(df['Country'] == country) & (df['Year'] == 1994)]['Tourist Arrivals'].values[0]
    df.loc[df['Country'] == country, 'PI'] = (current - base)/ base*100
    

chart = alt.Chart(df).encode(
    x = alt.X('Year:O', title=''),
    y = alt.Y('Tourist Arrivals:Q', title='Tourist Arrivals'),
    color=alt.Color('Country:N',
                    scale=alt.Scale(scheme='set2')),
    strokeWidth=alt.condition(alt.datum.Country == 'PT', alt.value(7), alt.value(0.5)),
    order=alt.Order(
      # Sort the segments of the bars by this field
      'Tourist Arrivals',
      sort='ascending'
    )
).properties(
    title='Tourist Arrivals in Portugal (1994-2018)',
    width=600,
).mark_bar()

chart.save('exercise2.html')