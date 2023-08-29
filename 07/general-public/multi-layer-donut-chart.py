# Import the required libraries
# Load '../data/competitions.csv' as pandas dataframe
# Select only the columns Training Type, Record Time (Seconds), Our Best Time
# Calculate the percentage difference between columns Our Best Time and Record Time (Seconds)  and store it into a new column called Percentage Difference
# Draw a bar chart with the following encodings:
# * The Percentage Difference on the y-axis with the following properties:
#   - The domain of the Y scale to [0,100]
# * Training Type on the x-axis with the following properties:
#   - The values sorted in descending order (-y)
# Set the following properties of the bar chart:
# * width to 300 pixels
# Save the chart as 'competitions.html'

import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import altair as alt

df = pd.read_csv('../data/competitions.csv')
df = df[['Training Type', 'Record Time (Seconds)', 'Our Best Time']]
# Manually change the column name
df['Percentage'] = 100 - (df['Our Best Time'] - df['Record Time (Seconds)']) / df['Record Time (Seconds)'] * 100
# Sort the values by the column 'Percentage'
df = df.sort_values(by='Percentage', ascending=False)

df['Complementary'] = 100 - df['Percentage']
df = df[['Training Type', 'Percentage', 'Complementary']].copy()
df = df.melt('Training Type', var_name='Percentage Type', value_name='Value')

training_types = df['Training Type'].unique()
charts = None

innerRadius=200
outerRadius=225
offset=30
y = -2*offset
width=300
height=300

for training_type in training_types:

    df_line = df[df['Training Type'] == training_type]

    color = 'lightgray'
    iColor = '#81c01e'
    if (training_type == 'Rowing') | (training_type == 'Cycling'):
        color = '#81c01e'
        iColor = 'lightgray'

    chart = alt.Chart(df_line).mark_arc(
        innerRadius=innerRadius,
        outerRadius=outerRadius,
        color=color
    ).encode( 
        theta=alt.Theta('Value:Q'),
        opacity=alt.condition(alt.datum['Percentage Type'] == 'Percentage', alt.value(1), alt.value(0)),
    ).properties(
        width=width,
        height=height
    )

    label = alt.Chart(df_line.head(1)).mark_text(
        align='right',
        baseline='middle',
        fontSize=20,
        fontWeight='bold',
        color=color,
        y = y,
        x = 150,
        dx = -10
    ).encode(
        text='Training Type',
    ).properties(
        width=width,
        height=height
    )

    percentage = alt.Chart(df_line.head(1)).mark_text(
        align='left',
        baseline='middle',
        fontSize=20,
        fontWeight='bold',
        color=iColor,
        y = y,
        x = 163,
        dx = -10
    ).encode(
        text=alt.Text('Percentage:N'),
    ).properties(
        width=width,
        height=height
    ).transform_calculate(
        Percentage = 'format(datum.Value, ".0f")' + ' + "%"'
    )

    innerRadius = innerRadius - offset
    outerRadius = outerRadius - offset
    y = y + 30
    if charts is None:
        charts = chart + label + percentage
    else:
        charts = charts + label + chart + percentage


# Add a new column to df called 'url' with the following value:
# * 'https://raw.githubusercontent.com/alod83/Data-Storytelling-with-Python-Altair-and-Generative-AI/eb16ac4564513ccfb8123ccde1926fbc88994ac6/04/case-study/images/cycling.png' for Training Type = 'Cycling'
# * 'https://raw.githubusercontent.com/alod83/Data-Storytelling-with-Python-Altair-and-Generative-AI/eb16ac4564513ccfb8123ccde1926fbc88994ac6/04/case-study/images/rowing.png' for Training Type = 'Rowing'
# * '' for all other Training Types

df['url'] = ''
df.loc[df['Training Type'] == 'Cycling', 'url'] = 'https://raw.githubusercontent.com/alod83/Data-Storytelling-with-Python-Altair-and-Generative-AI/eb16ac4564513ccfb8123ccde1926fbc88994ac6/04/case-study/images/cycling.png'
df.loc[df['Training Type'] == 'Rowing', 'url'] = 'https://raw.githubusercontent.com/alod83/Data-Storytelling-with-Python-Altair-and-Generative-AI/eb16ac4564513ccfb8123ccde1926fbc88994ac6/04/case-study/images/rowing.png'

df = pd.DataFrame({'Url' : [
    'https://raw.githubusercontent.com/alod83/Data-Storytelling-with-Python-Altair-and-Generative-AI/eb16ac4564513ccfb8123ccde1926fbc88994ac6/04/case-study/images/rowing.png',
    'https://raw.githubusercontent.com/alod83/Data-Storytelling-with-Python-Altair-and-Generative-AI/eb16ac4564513ccfb8123ccde1926fbc88994ac6/04/case-study/images/cycling.png'],
    'x' : [0, 1]})
# Add the following image to the chart:
# * The image is a 35x35 pixel image
# * The image is located at x='Training Type', y='Percentage Improvement'

images =  alt.Chart(df).mark_image(
    width=100, 
    height=100,
    y=170
).encode(
    url='Url',
    x=alt.X('x:O', axis=None)

).properties(
    width=width,
    height=height
)


charts = (images + charts).configure_view(
    strokeWidth=0
)


charts.save('multi-layer-donut-chart.html')
