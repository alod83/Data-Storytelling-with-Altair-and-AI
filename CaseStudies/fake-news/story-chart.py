import pandas as pd
import altair as alt

# Load the dataset data/fakenews.csv
df = pd.read_csv('data/fakenews.csv')

# Build a Python list with the following categories and name it material_life:
# Technology
# Environment
# Health
# Science
# Education
# Business
# Lifestyle
# Travel
# Politics
# Economy
# Sport

material_life = ['Technology', 'Environment', 'Health', 'Science', 'Education', 'Business', 'Lifestyle', 'Travel', 'Politics', 'Economy', 'Sport']

# Build a Python list with the following categories and name it moral_life:
# Social Issues
# Ethics
# Human Rights
# Philanthropy
# Diversity & Inclusion
# Relationships
# Culture & Arts
# Media & Entertainment
# Justice

moral_life = ['Social Issues', 'Ethics', 'Human Rights', 'Philanthropy', 'Diversity & Inclusion', 'Relationships', 'Culture & Arts', 'Media & Entertainment', 'Justice']

# Build a Python list with the following categories and name it spiritual_life:
# Religion
# Philosophy
# Spirituality & Faith
# Wellness & Mindfulness
# Personal Growth
# Mysticism
# Belief Systems

spiritual_life = ['Religion', 'Philosophy', 'Spirituality & Faith', 'Wellness & Mindfulness', 'Personal Growth', 'Mysticism', 'Belief Systems']

# Add a new column to the dataframe df called Macro Category that contains the following values:
# - if the Category is in material_life, then the value is Material Life
# - if the Category is in moral_life, then the value is Moral Life
# - if the Category is in spiritual_life, then the value is Spiritual Life

df['Macro Category'] = df['Category'].apply(lambda x: 'Material Life' if x in material_life else ('Moral Life' if x in moral_life else 'Spiritual Life'))

chart = alt.Chart(df).mark_bar(
).encode(
    y=alt.Y('Category:N', 
            sort='x',
            title=None,
            axis=alt.Axis(labelFontSize=14)
            ),
    x=alt.X('Percentage of Fake Articles:Q',
            title=None,
            axis=alt.Axis(labelFontSize=14, 
                          titleFontSize=14),
    ),
    color=alt.Color('Macro Category:N',
                    scale=alt.Scale(
                        range=['#991111', '#f38f8f','lightgray'],
                        domain=['Material Life', 'Moral Life', 'Spiritual Life']
                    ),
                    legend=None
            )
).properties(
    width=400,
    height=400
).transform_calculate(
    'Percentage of Fake Articles', alt.datum['Number of Fake Articles']/alt.datum['Number of Articles']*100
)

# Add an image to the chart
spiritual_image = alt.Chart(
    pd.DataFrame({'image_url': ['media/spiritual-life.png']})
).mark_image(
    width=80,
    height=80,
).encode(
    url='image_url',
    x=alt.value(270),  # pixels from left
    y=alt.value(50)
)

# Add a text to the chart
spiritual_text = alt.Chart(
    pd.DataFrame({'text': ['Spiritual Life']})
).mark_text(
    fontSize=30,
    color='black',
    align='center',
    baseline='middle',
    font='Monotype',
    fontStyle='italic'
).encode(
    x=alt.value(420),  # pixels from left
    y=alt.value(50),
    text='text'
)


moral_image = alt.Chart(
    pd.DataFrame({'image_url': ['media/moral-life.png']})
).mark_image(
    width=80,
    height=80,
).encode(
    url='image_url',
    x=alt.value(380),  # pixels from left
    y=alt.value(160)
)

moral_text = alt.Chart(
    pd.DataFrame({'text': ['Moral Life']})
).mark_text(
    fontSize=30,
    color='black',
    align='center',
    baseline='middle',
    font='Monotype',
    fontStyle='italic'
).encode(
    x=alt.value(530),  # pixels from left
    y=alt.value(160),
    text='text'
)

material_image = alt.Chart(
    pd.DataFrame({'image_url': ['media/material-life.png']})
).mark_image(
    width=80,
    height=80,
).encode(
    url='image_url',
    x=alt.value(500),  # pixels from left
    y=alt.value(300)
)

material_text = alt.Chart(
    pd.DataFrame({'text': ['Material Life']})
).mark_text(
    fontSize=30,
    color='black',
    align='center',
    baseline='middle',
    font='Monotype',
    fontStyle='italic'
).encode(
    x=alt.value(650),  # pixels from left
    y=alt.value(300),
    text='text'
)

chart = chart + spiritual_image  + spiritual_text + moral_image + moral_text + material_image + material_text

# Add context and wisdom
chart = chart.properties(width=500,title=alt.TitleParams(
    text=['Your Truth Guardian:', 'Take a Stand Against Fake News in Material and Moral Narratives'],
    subtitle=['The XX website is a popular source of news and information, but it is also a source of fake news.'],
    subtitleFontSize=18,
    fontSize=30,
    offset=40)
)

chart = chart.configure_axis(
    grid=False
).configure_view(
    strokeWidth=0
)
chart.save('story-chart.html')

