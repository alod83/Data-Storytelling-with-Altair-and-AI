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

df = pd.read_csv('../data/competitions.csv')
df = df[['Training Type', 'Record Time (Seconds)', 'Our Best Time']]
# Manually change the column name
df['Percentage Improvement'] = 100 - (df['Our Best Time'] - df['Record Time (Seconds)']) / df['Record Time (Seconds)'] * 100

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
    title=alt.TitleParams(
        text=['Unlock the Potential:', 'Invest in Rowing and Cycling for Maximum Returns!'],
        subtitle=['How to Choose the Best Sport to Fund: A Data-Driven Approach'],
    )
)

# Add a horizontal red line to the chart at y=50
# Add the line to the chart

chart = chart + alt.Chart(pd.DataFrame({'y': [50]})
                        ).mark_rule(color='red'
                        ).encode(
                            y=alt.Y('y', title='Percentage Improvement')
                        )


df['url'] = ''
df['y'] = 0
df.loc[df['Training Type'] == 'Cycling', 'url'] = 'cycling2.jpg'
df.loc[df['Training Type'] == 'Rowing', 'url'] = 'rowing2.png'
df.loc[df['Training Type'] == 'Rowing', 'y'] = 170
df.loc[df['Training Type'] == 'Cycling', 'y'] = 0

print(df)
img = alt.Chart(df).mark_image(
    width=150, 
    height=150,
    x=0).encode(
    url='url',
    y=alt.Y('y',axis=None, scale=alt.Scale(domain=[0, 220]))
).properties(
    width=100,
    height=200,
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

chart = (img | (chart + annotation)
).configure_view(
    strokeOpacity=0
).configure_title(
    fontSize=20,
    anchor='middle',
)


# Save the chart as 'competitions.html'


chart.save('competitions.html')
