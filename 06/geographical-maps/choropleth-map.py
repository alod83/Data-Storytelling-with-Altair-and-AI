import pandas as pd
import altair as alt

# Load data data/sales.csv as a Pandas dataframe
df = pd.read_csv('data/sales.csv')

# Load the TopoJSON file by URL
url = "https://raw.githubusercontent.com/deldersveld/topojson/master/continents/europe.json"


map = alt.topo_feature(url, "continent_Europe_subunits")

chart = alt.Chart(map).mark_geoshape(
    stroke='white',
).encode(
    tooltip=[alt.Tooltip('properties.geounit:N', title='Country'),
             'Sales:Q'],
    color=alt.Color('Sales:Q',scale=alt.Scale(scheme='greens'))
).project('mercator').properties(
    width=400,
    height=400
).transform_lookup(
    lookup='properties.geounit',
    from_=alt.LookupData(df, 'Country', ['Country', 'Sales'])
)


chart.save('choropleth-map.html')

