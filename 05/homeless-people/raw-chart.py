import pandas as pd
import altair as alt

df = pd.read_csv('source/homeless.csv')

# Data Cleaning
df['Territory'] = df['Territory'].str.replace('Trentino Alto Adige', 'Trentino-Alto Adige/Südtirol')

# Focus on total age, total sex and total citizenship
df = df[(df['Age'] == 'TOTAL') & (df['Sex'] == 'T') &  (df['Citizenship'] == 'TOTAL')]

# Load the TopoJSON file by URL
url = "https://raw.githubusercontent.com/openpolis/geojson-italy/master/topojson/limits_IT_regions.topo.json"
map = alt.topo_feature(url, "regions")

chart = alt.Chart(map).mark_geoshape().encode(
    tooltip='properties.reg_name:N',
    color=alt.Color('Value:Q')
).project('mercator').properties(
    width=500,
    height=500
).transform_lookup(
    lookup='properties.reg_name',
    from_=alt.LookupData(df, 'Territory', ['Territory', 'Value'])
).properties(title='Homeless in Italy in 2021')

chart.save('raw-chart.html')