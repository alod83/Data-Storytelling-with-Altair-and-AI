import altair as alt
import pandas as pd

df = pd.read_csv('../source/tourist_arrivals_countries.csv', parse_dates=['Date'])

df = pd.melt(df, id_vars='Date', value_name='Tourist Arrivals', var_name='Country')

# extract year from date
df.loc[:, 'Year'] = df['Date'].dt.year

# group by year and country
df = df.groupby(['Year', 'Country'])['Tourist Arrivals'].sum().reset_index()

# filter out years before 1994 and after 2018
df = df[(df['Year'] >= 1994) & (df['Year'] <= 2018)]

# add a new column containing the difference for each country between the number of tourist arrivals in the year and 1994
for country in df['Country'].unique():
    current = df[df['Country'] == country]['Tourist Arrivals']
    base = df[(df['Country'] == country) & (df['Year'] == 1994)]['Tourist Arrivals'].values[0]
    df.loc[df['Country'] == country, 'PI'] = (current - base)/ base*100


base = alt.Chart(df).encode(
    x = alt.X('Year:O', title=''),
    y = alt.Y('PI:Q', title='Percentage Increase since 1994'),
    color=alt.Color('Country:N',
                    scale=alt.Scale(scheme='set2'), 
                    legend=None),
    strokeWidth=alt.condition(alt.datum.Country == 'PT', alt.value(7), alt.value(0.5))
).properties(
    title='Tourist Arrivals in Portugal (1994-2018)'
)

chart = base.mark_line()


annotation = base.mark_text(
    dx=10,
    align='left',
    fontSize=12
).encode(
    # format the text to show only 2 decimal places and add a percentage sign
    text='label:N'
).transform_filter(
    alt.datum.Year == 2018
).transform_calculate(
    label='datum.Country + "(" + format(datum.PI, ".2f") + "%)"'
)

# add a commentary
text_comm = f"""Thanks to the introduction 
of low-cost flights, 
Portugal has experienced 
an increase 
in tourist arrivals 
of over 200% in 25 years, 
even surpassing the increase 
in the other countries."""
df_commentary = pd.DataFrame([{'text' : text_comm}])

commentary = alt.Chart(df_commentary
).mark_text(
    lineBreak='\n',
    align='left',
    fontSize=20,
    y=0,
    x=0,
    color='#81c01e'
).encode(
    text='text:N'
).properties(
    width=200
)

# add an explainable chart
df_airports = pd.read_csv('../source/airports.csv')

df_airports = df_airports.melt(id_vars='Country Name', var_name='Year', value_name='Value')
df_airports.dropna(inplace=True)
df_airports = df_airports[df_airports['Country Name'] == 'Portugal']

airports = alt.Chart(df_airports).mark_line(
    color='#81c01e',
    strokeWidth=6
).encode(
    x=alt.X('Year', axis=alt.Axis(labels=False, ticks=False, grid=False), title='Year range: 1994-2018'),
    y=alt.Y('Value', axis=alt.Axis(labels=False, ticks=False, grid=False), title='Air Passengers range: 4.3M-17.3M')
).properties(
    title='Air passengers in Portugal',
    width=200,
    height=200
)


chart = ((commentary & airports) | (chart + annotation)
)

chart.save('chart.html')