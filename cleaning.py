import pandas as pd
from scraping import scrape_house

urls = pd.read_csv('urls.csv')['url']
df = pd.DataFrame()
for url in urls:
  house = scrape_house(url)
  df = df.append(house)