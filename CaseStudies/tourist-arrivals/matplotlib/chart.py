import matplotlib.pyplot as plt
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

# create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# plot the data
for country in df['Country'].unique():
    current = df[df['Country'] == country]['Tourist Arrivals']
    base = df[(df['Country'] == country) & (df['Year'] == 1994)]['Tourist Arrivals'].values[0]
    pi = (current - base)/ base*100
    ax.plot(df[df['Country'] == country]['Year'], pi, label=country)

# set the title and axis labels
ax.set_title('Tourist Arrivals in Portugal (1994-2018)')
ax.set_xlabel('')
ax.set_ylabel('Percentage Increase since 1994')

# add a legend
ax.legend()

# save the plot
plt.savefig('chart.png', dpi=300)

