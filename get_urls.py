from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd


""" FUNCTIONS """
def scroll_to_bottom():
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

def click_load_button():
    try:
        load_button_wrapper = driver.find_element_by_class_name('js-load-more-wrapper')
        children = load_button_wrapper.find_elements_by_css_selector("*") 
        load_button = children[0]
    except:
        return False
    
    load_button.send_keys(Keys.RETURN)
    return True


""" CODE """
# set up path
PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)
url = 'https://www.forsaleutahrealestate.com/results-gallery/?county=12513&status=A'

# open session
driver.get(url)
driver.sleep(5)

# scroll to bottom
button_exists = True
SCROLL_PAUSE_TIME = 0.5

while button_exists:
    scroll_to_bottom()
    button_exists = click_load_button()

# get all card info
houses = driver.find_elements_by_tag_name('article')

# extract urls
urls = [h.get_attribute('data-url') for h in houses]

# quit page
driver.quit()

# save urls to csv
url_dict = {'url': urls} 
df = pd.DataFrame(url_dict)
df.to_csv('urls.csv', index=False)