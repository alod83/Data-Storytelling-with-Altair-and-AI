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

x_size = 10
step = 5
N = 3

x = [i*(x_size+step) for i in range(N)]
y = [0 for i in range(N)]
x2 = [(i+1)*x_size+i*step for i in range(N)]
y2 = [10 for i in range(N)]
text = ['Online Campaign', 'Influencers Engagement', 'Social Media Promotion']

df_rect = pd.DataFrame(
    {   'x': x,
        'y': y,
        'x2': x2,
        'y2': y2,
        'text' : text
    }
)

rect = alt.Chart(df_rect).mark_rect(
    color='#80C11E',
    opacity=0.2
).encode(
    x=alt.X('x:Q', axis=None),
    y=alt.Y('y:Q', axis=None),
    x2='x2:Q',
    y2='y2:Q'
).properties(
    width=700,
    height=100,
    title=alt.TitleParams(
        text=['What can we do next?'],
        fontSize=20,
        offset=10
    )
)

text = alt.Chart(df_rect).mark_text(
    fontSize=14,
    align='left',
    dx=10,
).encode(
    text='text:N',
    x=alt.X('x:Q', axis=None),
    y=alt.Y('y_half:Q', axis=None),
).transform_calculate(
    y_half='datum.y2/2'
)

# add lines connecting the rectangles
#x = [10,25]
x = [x_size*i+step*(i-1) for i in range(1,N)]
y = [5 for i in range(N-1)]
y2 = [5 for i in range(N-1)]
#x2 = [15,30]
x2 = [(x_size+step)*i for i in range(1,N)]

df_line = pd.DataFrame(
    {   'x': x,
        'y': y,
        'x2': x2,
        'y2': y2
    }
)

line = alt.Chart(df_line).mark_line(
    point=True,
    strokeWidth=2
).encode(
    x=alt.X('x:Q', axis=None),
    y=alt.Y('y:Q', axis=None),
    x2='x2:Q',
    y2='y2:Q'
)



chart = ((context | (chart + annotation + img)) & (rect + line + text)
).configure_view(
    strokeWidth=0
).resolve_scale(
    color='independent',
    x='independent',
    y='independent'
).configure_axis(
    grid=False
)



chart.save('pets-visualized-roadmap.html')