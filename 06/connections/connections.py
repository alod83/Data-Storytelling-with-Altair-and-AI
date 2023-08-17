import pandas as pd
import altair as alt

# Load the dataset from the CSV file
df = pd.read_csv('e-commerce_sales_dataset.csv')

color='#81c01e'

# Plot distribution of product ratings and number of reviews
rating_reviews_chart = alt.Chart(df).mark_bar(
    color=color
).encode(
    alt.X('product_rating:Q', bin=alt.Bin(maxbins=5), title='Product Rating'),
    alt.Y('number_of_reviews:Q', title='Number of Reviews'),
    tooltip=['product_rating', 'number_of_reviews:Q']
).properties(
    title='Product Ratings vs. Number of Reviews'
)

df['percentage_of_returns'] = df['returns'] / df['number_of_orders' ]*100

# Visualize relationship between product ratings and revenue
rating_revenue_chart = alt.Chart(df).mark_circle(
    color=color,
    size=100
).encode(
    alt.X('product_rating:Q', title='Product Rating'),
    alt.Y('percentage_of_returns:Q', 
          title='Percentage of returns',
          scale=alt.Scale(domain=(0, 100))),
    tooltip=['product_rating', 'returns']
).properties(
    title='Product Ratings vs. Percentage of Returns'
)


# Concatenate the charts and display them
final_chart = (rating_reviews_chart | rating_revenue_chart
).configure_view(
    strokeWidth=0
).configure_axis(
    grid=False
)
               
final_chart.save('connections.html')
