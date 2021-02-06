import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests

"""Functions"""
def extract_int(string):
    p_str = string.strip()
    return int(p_str.replace('$', '').replace(',',''))

def scrape_house(url):
    # get soup
    html = requests.get(url)
    soup = BeautifulSoup(html.content, features = 'html.parser')

    # get main table info
    main_table = soup.find(class_ = "bt-listing__feature-grid")
    cells = main_table.find_all('li')
    main_np = []
    for cell in cells:
        title = cell.find(class_ = 'uk-text-small uk-text-truncate').text
        attr_num = cell.find(class_ = 'attr-num').text

        if title == "SQFT" or title == "$/SQFT":
            attr_num = extract_int(attr_num)

        cell_info = [title, attr_num]
        main_np.append(cell_info)
    main_np = np.array(main_np)

    # add price
    price_str = soup.find(class_ = "uk-h1 uk-text-primary").text
    price = extract_int(price_str)
    main_np = np.vstack((['price', price], main_np))

    #row = pd.DataFrame([price, otherstuff], columns = ['price', 'otherstuff'])

    #return row

""" Main code """
# setup
urls = pd.read_csv('urls.csv')['url'].tolist()
df = pd.DataFrame()

# loop through all houses
for url in urls:
    row = scrape_house(url)
    df = df.append(row)