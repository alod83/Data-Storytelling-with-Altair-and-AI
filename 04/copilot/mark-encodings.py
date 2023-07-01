# Import the required libraries
# Load the file '../data/data.csv' into a pandas DataFrame
# Draw a line chart in Altair with the X column as the x-axis and the Y column as the y-axis
# Save the chart as a HTML file named chart.html

import pandas as pd
import altair as alt

df = pd.read_csv('../data/data.csv')

chart = alt.Chart(df).mark_line().encode(
    x='X',
    y='Y'
)

chart.save('chart.html')

# Load the file '../data/data2.csv' into a pandas DataFrame
# Draw a bar chart in Altair with the category column as the x-axis and the amount column as the y-axis
# Save the chart as a HTML file named chart2.html

df2 = pd.read_csv('../data/data2.csv')

chart2 = alt.Chart(df2).mark_bar().encode(
    x='category',
    y='amount'
)

chart2.save('chart2.html')

# Load the file '../data/data3.csv' into a pandas DataFrame
# Draw a bar chart in Altair with:
# - the category column as the x-axis 
# - the value column as the y-axis
# - the country column as the color of the bars. Set the col
# Save the chart as a HTML file named chart2.html

df3 = pd.read_csv('../data/data3.csv')

chart3 = alt.Chart(df3).mark_bar().encode(
    x='category',
    y='value',
    color='country'
)

chart3.save('chart3.html')

# Load the file '../data/data3.csv' into a pandas DataFrame
# Draw a bar chart in Altair with:
# * The category column as the x-axis 
# * The value column as the y-axis
# * The country column as the color. Set the color to:
#   - 'red' for 'IT'
#   - 'green' for 'FR'
# Save the chart as a HTML file named chart.html

chart4 = alt.Chart(df3).mark_bar().encode(
    x='category',
    y='value',
    color=alt.condition(
        alt.datum.country == 'IT',
        alt.value('red'),
        alt.value('green')
    )
)

chart4.save('chart4.html')