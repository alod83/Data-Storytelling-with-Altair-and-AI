# Import the necessary libraries
# Read the following dataset into a pandas dataframe: '../source/tourist_arrivals_countries.csv' and parse the Date field as a date
# Filter out rows before 1994 and after 2018
# Extract the year from the Date field and create a new column called Year
# Group the data by Year and calculate the sum of tourist arrivals for each year
# Add a new column to the DataFrame called PI containing the difference for each country between the number of tourist arrivals in the year and 1994
# Use the Altair library to plot the PI column for each country versus the Year
# Create a new chart with the following text: 'Thanks to the introduction\n of low-cost flights,\nPortugal has experienced\nan increase\nin tourist arrivals\nof over 200% in 25 years,\neven surpassing the increase\nin the other countries.' Use the \n as a line break to format the text. Set the font size to 14. 
# Place the two graphs side by side. Set title to 'Tourist Arrivals in Portugal (1994-2018)'
# Save the chart as an HTML. Name the file chart.html

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
    color=alt.Color('Country:N'),
    
).properties(
    title='Tourist Arrivals in Portugal (1994-2018)'
)

chart = base.mark_line()

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

commentary = alt.Chart(df_commentary).mark_text(
    lineBreak='\n',
    fontSize=14
).encode(
    text='text:N'
)

chart = chart | commentary

chart.save('chart.html')


