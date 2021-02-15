from sys import unraisablehook
import pandas as pd
from scraping import scrape_house

# import urls
urls = pd.read_csv('urls.csv')['url']
df = pd.DataFrame()

for url in urls:
  print(url)
  try:
    house = scrape_house(url)
    df = df.append(house)
  except:
    pass

df.to_csv('cleaned_data.csv')

# Figure out branches for cleaning.py
# Clean categorical data (make map from name -> int)
# Clean binary data
# Drop var with most missing
# Deal with NA's

# Think about modeling--do we need to set aside a test set?
    # Do we find an undervalued house using same houses that we build model on?
