# Import the required libraries
# Load the file 'data/data.csv' into a pandas DataFrame
# Draw a line chart named line in Altair with:
# * The X column as the x-axis
# * The Y column as the y-axis

import pandas as pd
import altair as alt

df = pd.read_csv('data/data.csv')

line = alt.Chart(df).mark_line().encode(
    x='X',
    y='Y'
)

# Load the file 'data/data3.csv' into a pandas DataFrame
# Draw a bar chart named bar in Altair with:
# * The category column as the x-axis 
# * The value column as the y-axis
# * The country column as the color. Set the color to:
#   - 'red' for 'Italy'
#   - 'green' for the other countries

df3 = pd.read_csv('data/data3.csv')

bar = alt.Chart(df3).mark_bar().encode(
    x='category',
    y='value',
    color=alt.condition(
        alt.datum.country == 'Italy',
        alt.value('red'),
        alt.value('green')
    ),
    # Add the tooltip encoding with the following columns in the tooltip:
    # * The category column
    # * The value column
    # * The country column
    tooltip=[
        'category',
        'value',
        'country'
    ]
# Make the chart interactive   
).interactive()



    

# Build a compound chart named chart with the line and bar charts aligned vertically
# Save the chart as a HTML file named chart.html

chart = alt.vconcat(
    line,
    bar
)

chart.save('chart.html')

