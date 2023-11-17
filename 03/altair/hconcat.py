import altair as alt
import pandas as pd

df = pd.DataFrame(
    {"Country": ["Japan", "USA", "Germany", "Spain", "France", "Italy"], 
     "Medals": [4, 6, 10, 3, 7, 8], 
     "Region":["Asia","Americas","Europe","Europe","Europe","Europe"]}) 


base = alt.Chart(df
).encode(
    x='Country',
    y='Medals'
).properties(
    width=300
)

chart1 = base.mark_bar(
    color='#636466'
).properties(
    title='A bar chart'
) 

chart2 = base.mark_line(
    color='#80C11E'
).properties(
    title='A line chart'
)

chart = chart1 | chart2

chart.save('hconcat.html')