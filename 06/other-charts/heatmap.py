import pandas as pd
import altair as alt

# Load data data/sales_reviews.csv as a Pandas dataframe
df = pd.read_csv('data/sales_reviews.csv')


width = 300
height = 300


base = alt.Chart(df
).transform_aggregate(
    mean_ranking='mean(Ranking)',
    groupby=['binned_reviews', 'binned_sales']
).transform_bin(
    'binned_reviews', 'Reviews', bin=alt.Bin(maxbins=10)
).transform_bin(
    'binned_sales', 'Sales', bin=alt.Bin(maxbins=10)
).encode(
    alt.X('binned_sales:O',
          title='Sales',
          axis=alt.Axis(labelAngle=0)
        ),
    alt.Y('binned_reviews:O',
          title='Reviews',
          sort=alt.SortOrder('descending')
        )
).properties(
    width=width,
    height=height
)


chart = base.mark_rect(
).encode(
    color=alt.Color('mean_ranking:Q',
            scale=alt.Scale(scheme='redyellowgreen'), 
            legend=alt.Legend(title='Ranking')
    ),

)

text = base.mark_text(baseline='middle').encode(
    alt.Text('mean_ranking:Q', format=".0f")
)

chart = chart + text

chart.save('heatmap.html')






chart.save('heatmap.html')
