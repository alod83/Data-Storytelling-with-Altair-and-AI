import altair as alt
import pandas as pd

df = pd.read_csv('../source/tourist_arrivals_countries.csv', parse_dates=['Date'])

df = pd.melt(df, id_vars='Date', value_name='Tourist Arrivals', var_name='Country')

# extract year from date
df.loc[:, 'Year'] = df['Date'].dt.year

# filter out years before 1994 and after 2018
df = df[(df['Year'] >= 1994) & (df['Year'] <= 2018)]

# group by year and country
df = df.groupby(['Year', 'Country'])['Tourist Arrivals'].sum().reset_index()

chart = alt.Chart(df).mark_line().encode(
    x = 'Year:O',
    y = 'Tourist Arrivals:Q',
    color=alt.Color('Country:N')
)

chart.save('grouped-chart.html')