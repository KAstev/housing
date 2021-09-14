import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scraping import scrape_house

urls = pd.read_csv('urls.csv')['url']
df = pd.DataFrame()
for url in urls:
  try:
    house = scrape_house(url)
    df = df.append(house)
  except:
    pass

df = pd.read_csv('data.csv')
df = df.query('price < 1000000')
# extra = df.iloc[:,86:]

y = df.iloc[:,0]

def eda(x, y):
  info = {'name': x.name, 'unique': len(x.unique()), 'nas': sum(x.isna())}
  print(info)
  plt.scatter(x, y)
  plt.show()

df['BEDS'].value_counts()  

plt.hist(df['BEDS'])
plt.show()

# Assuming Lasso or elastic ridge
# Look for columns with many NAs or many of the same value
# Check for outliers
# Check for linearity (maybe transforming y)
# Convert categorical variables