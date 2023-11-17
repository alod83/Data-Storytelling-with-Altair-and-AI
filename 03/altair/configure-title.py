import pandas as pd
import altair as alt

df = pd.DataFrame(
    {"Country": ["Japan", "USA", "Germany", "Spain", "France", "Italy"], 
     "Medals": [4, 6, 10, 3, 7, 8], 
     "Region":["Asia","Americas","Europe","Europe","Europe","Europe"]}) 


chart = alt.Chart(df).mark_bar(color='#636466').encode(
    x='Country',
    y='Medals'
).properties(width=300, 
             title='A bar chart'
)

chart = chart.configure_title(
    fontSize=20, #A
    color='#80C11E', #B
    offset=30, #C
    anchor='start' #D
)



chart.save('configure-title.html')
