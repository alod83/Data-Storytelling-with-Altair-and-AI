import pandas as pd
import altair as alt

# Load data data/sales.csv as a Pandas dataframe
df = pd.read_csv('data/sales.csv')

# Load the TopoJSON file by URL
url = "https://raw.githubusercontent.com/deldersveld/topojson/master/continents/europe.json"

points = alt.Chart(df).mark_circle(
    color='#81c01e',
).encode(
    longitude='Longitude:Q',
    latitude='Latitude:Q',
    tooltip='Sales:Q'
).properties(
    width=400,
    height=400
)

map = alt.topo_feature(url, "continent_Europe_subunits")

base = alt.Chart(map).mark_geoshape(
    fill='lightgray',
    stroke='white'
).project('mercator').properties(
    width=400,
    height=400
)

chart = (base + points)


chart.save('dot-density-map.html')

