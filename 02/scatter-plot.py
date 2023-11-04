import pandas as pd
import altair as alt

data = {
   'X' : [2,3,5,6,7,9,4,5,5,6],
   'Y' : [4,5,6,7,8,9,5,6,3,5]
}

df = pd.DataFrame(data)


chart = alt.Chart(df).mark_circle().encode(
    x = 'X',     
    y = 'Y' 
)

chart.save('scatter-plot.html')
