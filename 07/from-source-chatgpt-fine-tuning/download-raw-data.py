# import required libraries
# extract the title and link from the following rss/feed url: https://alod83.medium.com/feed
# for each extracted link, extract the subheading from the article
# create a dataframe with the following columns: 'prompt', 'completion'
# save the dataframe to a csv file called 'medium-articles.csv'

import feedparser
import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://alod83.medium.com/feed'
feed = feedparser.parse(url)

titles = []
links = []
subheadings = []

for entry in feed.entries:
    titles.append(entry.title)
    links.append(entry.link)
    print(entry.link)
    response = requests.get(entry.link)
    soup = BeautifulSoup(response.content, 'html.parser')
    subheading = soup.find('h2', attrs={'class': 'pw-subtitle-paragraph'}).text
    subheadings.append(subheading)

df = pd.DataFrame({'prompt': subheadings,'completion': titles})
df.to_csv('medium-articles.csv', index=False)
