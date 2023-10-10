# import required libraries
# load the dataset '../source/Aquaculture_Exports.csv' as a pandas dataframe
# apply the following filters to the dataframe:
#   - select only the rows where the 'GEOGRAPHY_DESC' column is 'World'
#   - select only the rows where the 'UNIT_DESC' column is 'KG'
# add a new column to the dataframe called 'DATE' which is a date object build as follows:
#   - the year is the 'YEAR_ID' column
#   - the month is the 'TIMEPERIOD_ID' column
#   - the day is 1
# plot the dateframe using altair as follows:
#   - the x axis is the 'DATE' column
#   - the y axis is the 'AMOUNT' column
#   - the color is the 'COMMODITY_DESC' column
# save the plot as 'chart.html'

import pandas as pd
import altair as alt

df = pd.read_csv('../source/Aquaculture_Exports.csv')
df = df[df['GEOGRAPHY_DESC'] == 'World']
df = df[df['UNIT_DESC'] == 'U.S.$']
#df = df[df['UNIT_DESC'] == 'KG']
df['DATE'] = pd.to_datetime(df['YEAR_ID'].astype(str) + '-' + df['TIMEPERIOD_ID'].astype(str) + '-1')
# print the max value of the 'DATE' column
color='#F27B6E'
#color='#0ABDFD'
domain = ['Salmon', 'Shrimp', 'Trout', 'Scallop', 'Other']

# from the dataframe filter out the following rows:
#   - the 'COMMODITY_DESC' value is not uppercase

df = df[~df['COMMODITY_DESC'].str.isupper()]

# add a new column to the dataframe called CATEGORY which is built as follows:
# - if the 'COMMODITY_DESC' value contains the word salmon or Salmon then the value is 'Salmon'
# - if the 'COMMODITY_DESC' value contains the word shrimp or Shrimp then the value is 'Shrimp'
# - if the 'COMMODITY_DESC' value contains the word trout or Trout then the value is 'Trout'
# - if the 'COMMODITY_DESC' value contains the word scallop or Scallop then the value is 'Scallop'
# - otherwise the value is 'Other'

df['CATEGORY'] = ['Salmon' if 'salmon' in x or 'Salmon' in x else 'Other' for x in df['COMMODITY_DESC']]
range = [color if 'Salmon' in x else 'lightgrey' for x in domain]

# group the dataframe by 'YEAR_ID' and 'COMMODITY_DESC' and sum the 'AMOUNT' column
# reset the index of the dataframe

df = df.groupby(['YEAR_ID', 'CATEGORY'])['AMOUNT'].sum().reset_index()

# remove year 2016 from the dataframe
df = df[df['YEAR_ID'] != 2016]

base = alt.Chart(df).encode(
    x=alt.X('YEAR_ID:O', title=''),
    y=alt.Y('AMOUNT', title='$',axis=alt.Axis(format='.2s')),
    color=alt.Color('CATEGORY', 
        legend=None,
        scale=alt.Scale(range=range, domain=domain)
    )
).properties(
    width=800,
    height=400
)


chart = base.mark_line(

)
# add a text mark to the chart as follows:
#   - the x position is 'DATE'
#   - the y position is AMOUNT
#   - the text is the value of the 'COMMODITY_DESC' column
# add a transform_filter to the text mark as follows:
# - select only the max value of the 'YEAR_ID' column

text = base.mark_text(
    align='left',
    baseline='middle',
    fontSize=14,
    dx=5
).encode(
    text='CATEGORY'
).transform_filter(
    alt.datum.YEAR_ID == df['YEAR_ID'].max()
)


chart = (chart  + text
).configure_axis(
    labelFontSize=14,
    titleFontSize=16,
    grid=False
).configure_view(
    strokeWidth=0
)
chart.save('chart.html')