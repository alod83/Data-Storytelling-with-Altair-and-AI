import numpy as np
import pandas as pd
import altair as alt

# Compute x^2 + y^2 across a 2D grid
x, y = np.meshgrid(range(0, 10), range(0, 10))

ndex = 0
value = 73 # percentage

## calculate colors for each cell of the waffle chart
colors = []
for i in range(100,0,-1):
    if i <= np.round(value):
        colors.append(1)
    else:
        colors.append(0)
        

# Convert this grid to columnar data expected by Altair
df = pd.DataFrame({'x': x.ravel(),
                        'y': y.ravel(),
                        'z': colors})

chart = alt.Chart(df).mark_rect(
    size=5, 
    stroke='black'
).encode(
    x=alt.X('x:O', axis=None),
    y=alt.Y('y:O', axis=None),
    color=alt.condition(alt.datum.z == 0, 
                        alt.value('lightgrey'),
                        alt.value('#81c01e')
                        )
).properties()

chart.save('waffle-chart.html')