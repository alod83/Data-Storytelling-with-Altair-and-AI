import pandas as pd
import altair as alt

df = pd.read_csv('source/pets.csv')

df.drop(index=[2],axis=0,inplace=True)
df['percentage'] = df['percentage']/10

data = pd.DataFrame([{'text' : 'cat', 'x': 0.5},
                     {'text' : 'dog', 'x': 9.4}
                    ])

color = ['#636466','#80C11E']
scale = alt.Scale(range=color)


chart = alt.Chart(df).mark_bar(
    size=50,
    y=80
).encode(
    x=alt.X('percentage:Q', 
            scale=alt.Scale(domain=[0, 10]),
            axis=alt.Axis(tickMinStep = 1,grid=False, title=None, orient='bottom')
           ),
    color=alt.Color('pet:O', legend=None,scale=scale),
    stroke=alt.Color('pet:O',scale=scale, legend=None),
    strokeWidth=alt.value(2),
    opacity=alt.value(0.6)

).properties(
    height=130,
    title=alt.TitleParams(
        text=['Increase the advertising campaign', 'on dog-related websites!'],
        fontSize=20
    )
)

df_ann = pd.DataFrame([{'text' : 'cat', 'x': 0.5},
                     {'text' : 'dog', 'x': 9.4}
                    ])

annotation = alt.Chart(df_ann).mark_text(
    fontSize=14, 
    y=30
).encode(
    text='text:N',
    x=alt.X('x:Q', 
            scale=alt.Scale(domain=[0, 10]),
            axis=alt.Axis(tickMinStep = 1,
                          grid=False, 
                          title=None, 
                          orient='bottom')),
    color=alt.Color('text:O', 
                    scale = alt.Scale(range=color), 
                    legend=None)
)

context_text = ['9 out of 10 pets particpating to the event are cats',
    'The participation rate for cats is nearly 8%',
                'across more than 150 advertised sites,', 
                "whereas for dogs, it's almost 5% across",
                'over 30 advertised sites.']


df_context = pd.DataFrame([{'text' : context_text }])

context = alt.Chart(df_context).mark_text(
    fontSize=20, 
    align='left',
    dy=30
).encode(
    text='text:N',
)

df_img = pd.DataFrame.from_records([
      {"x": 0, "img": "img/cat.png"},
      {"x": 9.8, "img": "img/dog.png"}
])

img = alt.Chart(df_img).mark_image(
    width=50,
    height=50,
    y=50
).encode(
    x=alt.X('x:Q', 
        scale=alt.Scale(domain=[0, 10]),
        axis=alt.Axis(tickMinStep = 1,
            grid=False, 
            title=None, 
            orient='bottom',
        )
    ),
    url='img',  
)

# Next Steps

# add the following logos to the chart:
# - the Facebook logo (https://www.facebook.com/images/fb_icon_325x325.png)
# - the Instagram logo (https://cdn3.iconfinder.com/data/icons/capsocial-round/500/instagram-512.png)
df_logos = pd.DataFrame({
    'x': [0, 1],
    'img': ['https://www.facebook.com/images/fb_icon_325x325.png',
            'https://cdn3.iconfinder.com/data/icons/capsocial-round/500/instagram-512.png'],
    # modify here with a specific page
    'url': ['https://www.facebook.com/',
            'https://www.instagram.com/']    
})

logos = alt.Chart(df_logos).mark_image(
    width=30,
    height=30,
    y=30,
    xOffset=40
).encode(
    x=alt.X('x:Q', axis=None),
    url='img',
    href='url'
).properties(
    width=50,
    title=alt.TitleParams(
        text=['Share on social media'],
        fontSize=14
    )
)

chart = ((context | (chart + annotation + img) & logos)
).configure_view(
    strokeWidth=0
).resolve_scale(
    color='independent',
    x='independent',
    y='independent'
).configure_axis(
    grid=False
)

chart.save('pets-social-sharing.html')