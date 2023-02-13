# Import the necessary libraries
# Read the following dataset into a pandas dataframe: 'source/tourist_arrivals_countries.csv' and parse the Date field as a date
# Remove missing rows from the data
# Extract the year from the Date field and create a new column called Year
# Group the data by Year and calculate the average number of tourist arrivals for each year
# Select only the rows where the year is 1994 or 2018
# Select only the following columns: Year, PT and DE
# Create a new dataframe df_pi with three columns Year, Country, and Percentage Increase
# Add a new row to df_pi with the following values: 1994, PT, 0.0
# Add a new row to df_pi with the following values: 1994, DE, 0.0
# For columns PT and DE in the original dataframe df, calculate the percentge increase of the second row respect to first row and store the result as two new columns in df_pi. For the column year, add 2018
# Use the Altair library to plot two lines in the same chart showing the PT and DE columns versus the Year column of df_pi. Use the color channel to discriminate for the Country column. Encode the x channel as ordinal. Set chart width to 400
# Create a new chart with the following text: 'Thanks to the introduction of low-cost flights, \nPortugal has experienced an increase in tourist arrivals \nof over 200% in 25 years, \neven surpassing the increase in Germany, \none of the favorite destinations for tourists ever.' Use the \n as a line break to format the text. Set the font size to 14. 
# Place the two graphs side by side. Set title to 'Yes, you can build a new swimming pool!'
# Save the chart as an HTML. Name the file output.html

import pandas as pd
import altair as alt

def main():
    # Read the following dataset into a pandas dataframe: 'source/tourist_arrivals_countries.csv' and parse the Date field as a date
    df = pd.read_csv('source/tourist_arrivals_countries.csv', parse_dates=['Date'])
    # Remove missing rows from the data
    df = df.dropna()
    # Extract the year from the Date field and create a new column called Year
    df['Year'] = df['Date'].dt.year
    # Group the data by Year and calculate the average number of tourist arrivals for each year
    df = df.groupby('Year').mean()
    # Select only the rows where the year is 1994 or 2018
    df = df.loc[[1994, 2018]]
    # Select only the following columns: Year, PT and DE
    df = df[['PT', 'DE']]
    # Create a new dataframe df_pi with three columns Year, Country and Percentage Increase
    df_pi = pd.DataFrame(columns=['Year', 'Country', 'Percentage Increase'])
    # Add a new row to df_pi with the following values: 1994, PT, 0.0
    df_pi = df_pi.append({'Year': 1994, 'Country': 'PT', 'Percentage Increase': 0.0}, ignore_index=True)
    # Add a new row to df_pi with the following values: 1994, DE, 0.0
    df_pi = df_pi.append({'Year': 1994, 'Country': 'DE', 'Percentage Increase': 0.0}, ignore_index=True)
    # For columns PT and DE in the original dataframe df, calculate the percentae increase of the second row respect to first row and store the result as two new columns in df_pi. For the column year, add 2018
    df_pi = df_pi.append({'Year': 2018, 'Country': 'PT', 'Percentage Increase': df['PT'].pct_change().dropna()[2018]}, ignore_index=True)
    df_pi = df_pi.append({'Year': 2018, 'Country': 'DE', 'Percentage Increase': df['DE'].pct_change().dropna()[2018]}, ignore_index=True)
    # Use the Altair library to plot two lines in the same chart showing the PT and DE columns versus the Year column of df_pi. Use the color channel to discriminate for the Country column. Encode the x channel as ordinal. Set chart width to 400
    chart = alt.Chart(df_pi).mark_line().encode(
        x=alt.X('Year', type='ordinal'),
        y='Percentage Increase',
        color='Country'
    ).properties(width=400)

    # Create a new chart with the following text: 'Thanks to the introduction of low-cost flights, \nPortugal has experienced an increase in tourist arrivals \nof over 200% in 25 years, \neven surpassing the increase in Germany, \none of the favorite destinations for tourists ever.' 
    text = alt.Chart(pd.DataFrame({'text': ['Thanks to the introduction of low-cost flights, \nPortugal has experienced an increase in tourist arrivals \nof over 200% in 25 years, \neven surpassing the increase in Germany, \none of the favorite destinations for tourists ever.']})).mark_text(
    ).encode(text='text')
    
    # Place the two graphs side by side. Set title to 'Yes, you can build a new swimming pool!'
    chart = alt.hconcat(chart, text).properties(title='Yes, you can build a new swimming pool!')


    # Save the chart as an HTML. Name the file output.html
    chart.save('output.html')

if __name__ == '__main__':
    main()
