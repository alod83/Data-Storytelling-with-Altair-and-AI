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

import pandas as pd
import altair as alt

df = pd.read_csv('source/competitions.csv')
df = df[['Training Type', 'Record Time (Seconds)', 'Our Best Time']]
# Manually change the column name
df['Percentage Improvement'] = 100 - (df['Our Best Time'] - df['Record Time (Seconds)']) / df['Record Time (Seconds)'] * 100

print(df)
chart = alt.Chart(df).mark_bar().encode(
    y=alt.Y('Percentage Improvement', scale=alt.Scale(domain=[0, 100])),
    x=alt.X('Training Type', 
            sort='-y',
            axis=alt.Axis(title=None, labelAngle=0)),
    # Add the color encoding. Set the color to:
    # - #80C11E if the Percentage Improvement is greater than 50, 
    # - lightgray otherwise
    color=alt.condition(
        alt.datum['Percentage Improvement'] > 50,
        alt.value('#80C11E'),
        alt.value('lightgray')
    )
).properties(
    width=400,
    height=300,
    # Add the following properties to the chart:
    # * title to 'Unlock the Potential: Invest in Rowing and Cycling for Maximum Returns!'
    title='Unlock the Potential: Invest in Rowing and Cycling for Maximum Returns!'
)

# Add a horizontal red line to the chart at y=50
# Add the line to the chart

chart = chart + alt.Chart(pd.DataFrame({'y': [50]})
                        ).mark_rule(color='red'
                        ).encode(
                            y=alt.Y('y', title='Percentage Improvement')
                        )

# Add a new column to df called 'url' with the following value:
# * 'https://github.com/alod83/AI-Powered-Data-Storytelling-in-Python-with-Altair/blob/b06e0f2ccba5833b14effa68c924ae3b54eb4040/CaseStudies/competitions/images/cycling.png' for Training Type = 'Cycling'
# * 'https://github.com/alod83/AI-Powered-Data-Storytelling-in-Python-with-Altair/blob/b06e0f2ccba5833b14effa68c924ae3b54eb4040/CaseStudies/competitions/images/rowing.png' for Training Type = 'Rowing'
# * '' for all other Training Types

df['url'] = ''
df.loc[df['Training Type'] == 'Cycling', 'url'] = 'https://github.com/alod83/AI-Powered-Data-Storytelling-in-Python-with-Altair/blob/b06e0f2ccba5833b14effa68c924ae3b54eb4040/CaseStudies/competitions/images/cycling.png'
df.loc[df['Training Type'] == 'Rowing', 'url'] = 'https://github.com/alod83/AI-Powered-Data-Storytelling-in-Python-with-Altair/blob/b06e0f2ccba5833b14effa68c924ae3b54eb4040/CaseStudies/competitions/images/rowing.png'

# Add the following image to the chart:
# * The image is a 35x35 pixel image
# * The image is located at x='Training Type', y='Percentage Improvement'

chart = chart + alt.Chart(df).mark_image(width=35, height=35).encode(
    x=alt.X('Training Type', sort='-y'),
    y=alt.Y('Percentage Improvement', title='Percentage Improvement'),
    url='url'
)

# Add the following text to the chart:
# "Use 50% as the benchmark for sports selection"
# The text is located at x=0, y=50
annotation_df = pd.DataFrame({'text': ['Use 50% as the benchmark for sports selection']})
annotation = alt.Chart(annotation_df
        ).mark_text(
            size=10, 
            align='left', 
            color='red',
            x=170,
            y=150,
            dy=-10
        ).encode(
            text='text'
        )

chart = (chart + annotation)


# Save the chart as 'competitions.html'


chart.save('competitions.html')
