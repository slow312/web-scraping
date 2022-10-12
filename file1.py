import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

# Make request to webpage
page = requests.get('https://www.nytimes.com/section/technology')
# Create beautiful soup object 
soup = BeautifulSoup(page.text,'html.parser')

#### Get NYT Headers ####
headers = soup.find_all('h2',class_='css-1kv6qi e15t083i0')

# Clean headers data
headers_clean = []
for x in headers:
    name = x.text
    name = name.replace('<h2 class="css-1kv6qi e15t083i0">','') 
    name = name.replace('</h2>','')
    print(name)
    headers_clean.append(name)

#### Get NYT Article Descriptions ####
descriptions = soup.find_all('p',class_='css-1pga48a e15t083i1')

# Clean description data
desc_clean = []
for x in descriptions:
    name = x.text
    name = name.replace('<p class="css-1pga48a e15t083i1">">','') 
    name = name.replace('</p>','')
    print(name)
    desc_clean.append(name)

# Turn header and description lists into dataframe
df = pd.DataFrame(list(zip(headers_clean,desc_clean)),columns=['Headers','Descriptions'])
df

# Create "data" folder + add dataframe into new folder
os.makedirs('web-scraping\data',exist_ok=True)
df.to_csv('web-scraping/data/nyt.csv')
