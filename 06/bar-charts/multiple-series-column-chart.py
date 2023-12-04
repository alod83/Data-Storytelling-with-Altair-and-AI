import pandas as pd
import altair as alt

# Load data data/meals.csv as a Pandas dataframe
df = pd.read_csv('data/meals-by-year.csv')

df = df.melt(id_vars=['Meal Type'],var_name='Year',value_name='Number of Likes')

chart = alt.Chart(df).mark_bar(
).encode(
    x=alt.X('Year', 
            # Rotate the labels by 0 degrees
            axis=alt.Axis(title=None, labels=False)
    ),
    y=alt.Y('Number of Likes',axis=alt.Axis(grid=False)),
    column=alt.Column('Meal Type',
                      header=alt.Header(
                          labelOrient='bottom',
                          #labelBaseline='line-bottom',
                          title=None
                          )),
    color=alt.Color('Year',scale=alt.Scale(range=['lightgray','#81c01e']))
).properties(
    width=50,
    height=300
).configure_view(
    strokeWidth=0
)

chart.save('multiple-column-chart.html')

