import altair as alt
import pandas as pd

df = pd.DataFrame(
    {"Country": ["Japan", "USA", "Germany", "Spain", "France", "Italy"], 
     "Medals": [4, 6, 10, 3, 7, 8], 
     "Region":["Asia","Americas","Europe","Europe","Europe","Europe"]}) 

chart = alt.Chart(df).mark_bar(color='#636466').encode(
    x='Country',
    y='Medals',
    tooltip=['Country', 'Medals', 'Region']
).properties(
    width=300, 
    title='A bar chart'
).interactive()

chart.save('interactive.html')