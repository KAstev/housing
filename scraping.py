from pandas import DataFrame
from numpy import array, vstack
from requests import get
from bs4 import BeautifulSoup

def scrape_house(url):

  def extract_int(string):
    p_str = string.strip()
    return int(p_str.replace('$', '').replace(',',''))

  ########## Connect to URL ##########
  html = get(url)
  soup = BeautifulSoup(html.content, features='html.parser')

  ########## add price ##########
  price_str = soup.find(class_ = "uk-h1 uk-text-primary").text
  price = extract_int(price_str)
  df = array(['price', price])

  ########## get main table info ##########
  main_table = soup.find(class_ = "bt-listing__feature-grid")
  cells = main_table.find_all('li')
  for cell in cells:
      title = cell.find(class_ = 'uk-text-small uk-text-truncate').text
      attr_num = cell.find(class_ = 'attr-num').text

      if title == "SQFT" or title == "$/SQFT":
          attr_num = extract_int(attr_num)

      cell_info = [title, attr_num]
      df = vstack((df, cell_info))


  ########## Add location tables ##########
  location = soup.find('div', class_='m-0 bt-listing-table bt-listing__table-break')
  location = [[i for i in j.text.strip().split('\n') if i] for j in location('div', class_='grid')]
  df = vstack((df, location))

  ########## Add school tables ##########
  school = soup.find('div', class_='bt-listing-table bt-listing__table-break m-0')
  school = [[i.strip() for i in j.text.strip().split(':')] for j in school('div', class_='grid')]
  df = vstack((df, school))

  ########## Add feature tables ##########
  cells = soup('li', class_='cell')
  for cell in cells:
    table = array([row.text.strip().split('\n\n') for row in cell('tr')])
    df = vstack((df, table))

  return DataFrame(data=df[:,1].reshape(1,-1), columns=df[:,0])