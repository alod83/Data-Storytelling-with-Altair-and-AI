import altair as alt
import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv('../source/tourist_arrivals_countries.csv', parse_dates=['Date'])

# Exploratory Data Analysis
eda = ProfileReport(df)
eda.to_file(output_file='eda.html')

df = pd.melt(df, id_vars='Date', value_name='Tourist Arrivals', var_name='Country')

chart = alt.Chart(df).mark_line().encode(
    x = 'Date:T',
    y = 'Tourist Arrivals:Q',
    color=alt.Color('Country:N')
)

chart.save('raw-chart.html')