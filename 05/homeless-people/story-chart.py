import pandas as pd
import altair as alt

df = pd.read_csv('source/homeless.csv')

# Data Cleaning
df['Territory'] = df['Territory'].str.replace('Trentino Alto Adige', 'Trentino-Alto Adige/Südtirol')

# Focus on total age, total sex and total citizenship
df = df[(df['Age'] == 'TOTAL') & (df['Sex'] == 'T') &  (df['Citizenship'] == 'TOTAL')]
df = df[['Value', 'ITTER107']]

# Normalize the values by popultation
df_pop = pd.read_csv('source/population.csv')
df_pop = df_pop[(df_pop['Age'] == 'TOTAL') & (df_pop['Sex'] == 'T')]


df_pop = df_pop[['Value', 'ITTER107','Territory']]

df_tot = df_pop.set_index('ITTER107').join(df.set_index('ITTER107'),lsuffix='_pop', rsuffix='_hom').reset_index()
df_tot['Ratio'] = df_tot['Value_hom']/df_tot['Value_pop']*1000

chart = alt.Chart(df_tot).mark_bar().encode(
    y = alt.Y('Territory', 
              sort='-x', 
              axis=alt.Axis(title='')),
    x = alt.X('Ratio', 
              axis=alt.Axis(tickCount=4,title='')),
    color=alt.condition(alt.datum.Ratio > 2, 
                        alt.value('#80C11E'), 
                        alt.value('lightgray'))
   
).properties(
    width=500,
    title='Number of homeless people in a population of 1,000'
)

# Add context
chart = chart.properties(width=500,title=alt.TitleParams(
    text=["Together, Let's Make a Difference:","Support Our Project to Help the Homeless!"],
    subtitle=['Homelessness is a heartbreaking reality that leaves individuals and families without a stable home,','leading to devastating consequences such as poor health and social isolation.'],
    subtitleFontSize=18,
))

# Create an Altair chart with an image mark
image1 = alt.Chart(pd.DataFrame({'image_url': ['media/homeless1.png']})
).mark_image(
    width=200,
    height=200,
).encode(
    url='image_url',
    x=alt.value(0),  # pixels from left
    y=alt.value(50)
)

image2 = alt.Chart(
    pd.DataFrame({'image_url': ['media/homeless2.png']})
).mark_image(
    width=200,
    height=200,
).encode(
    url='image_url',
    x=alt.value(0),  # pixels from left
    y=alt.value(300)
)

#chart = image1 + image2| chart

# Adding next steps
ns = pd.read_csv('source/next_steps.csv')

donuts = None
for index, row in ns.iterrows():
    # Create a pie chart for the current row
    curr_ns = pd.DataFrame(
        {'Category': ['A', 'B'],
         'Value': [row['Allocation'], 100-row['Allocation']]
        }
    )
    donut = alt.Chart(curr_ns).mark_arc(outerRadius=30,innerRadius=20).encode(
        theta=alt.Theta("Value:Q",stack=True),
        color=alt.Color("Category:N",scale=alt.Scale(range=['#80C11E', 'lightgray']),legend=None)
    )
    title = alt.Chart(curr_ns).mark_text(text=row['Category'], y=0, size=16)
    text = alt.Chart(curr_ns).mark_text(text=f"{row['Allocation']}%", color='#80C11E', size=16)
    donut = donut.properties(
        height=100, 
        width=100
    )
    if index == 0:
        donuts = title+donut+text
    else:
        donuts = alt.hconcat(donuts, title+donut+text)
donuts = donuts.properties(title='Our visionary plan to harness the funds')

chart = alt.vconcat(image1 + image2| chart,donuts)

chart = chart.configure_title(
    fontSize=20,
    offset=25
).configure_axis(
    grid=False
).configure_view(
    strokeWidth=0
)

chart.save('story-chart.html')