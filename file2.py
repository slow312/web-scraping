from locale import atof
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import re

# Make request to webpage
page = requests.get('https://finance.yahoo.com/quote/NFLX/financials/',headers={'User-Agent': 'Custom'})
# Create Beautiful Soup object
soup = BeautifulSoup(page.text,'html.parser')

#### Get Breakdown ####
breakdown = soup.find_all('div',class_='D(ib) Va(m) Ell Mt(-3px) W(215px)--mv2 W(200px) undefined')

def clean_breakdown(html):
    """
    Use re.search w/ pattern >(.*)</span></div> to find article title (did not fully get rid of extra text) 
    Use .group(1) to get first re.MatchObject containing title 
    Use split to get rid of rest of text; get last item in list
    return article title 

    Parameter html: string of html block  
    """
    result = re.search('>(.*)</span></div>',html)
    result = result.group(1)
    result = result.split('"Va(m)">',1)[1]
    return result

# Cleans 'Breakdown' data with clean_breakdown function
bd_clean = []
for x in breakdown:
    bd_clean.append(clean_breakdown(str(x)))

# Check final result + length aligns with chart on website
bd_clean
len(bd_clean)

#### Get Financial Information ####

# Chart was seperated into grey and white columns
# First pulled grey columns
grey_col = soup.find_all('div',class_='Ta(c) Py(6px) Bxz(bb) BdB Bdc($seperatorColor) Miw(120px) Miw(100px)--pnclg Bgc($lv1BgColor) fi-row:h_Bgc($hoverBgColor) D(tbc)')

def clean_ttm(html):
    """
    if statements to check for different patterns in html code
    if re.search found the regex pattern:
        save resulting re.MatchObject to html variable
        return first MatchObject
    function returns 'None' if pattern not found

    Parameter html: string of html block
    """
    if re.search('><span>(.*)</span></div>',str(x)):
        html = re.search('><span>(.*)</span></div>',str(x))
        return html.group(1)
    elif re.search('>(.*)</div>',str(x)):
        html = re.search('>(.*)</div>',str(x))
        return html.group(1) 
    else: 
        return 'None'

# Clean financial information from grey columns + use clean_ttm function
clean_grey = []
for x in grey_col:
    clean_grey.append(clean_ttm(str(x)))

# Check data + len lines up with breakdown data
clean_grey
len(clean_grey)
len(bd_clean) * 3

# Pulled data from white columns
white_col = soup.find_all('div', class_='Ta(c) Py(6px) Bxz(bb) BdB Bdc($seperatorColor) Miw(120px) Miw(100px)--pnclg D(tbc)')

# Clean financial info from white columns + use clean_ttm function
clean_white = []
for x in white_col:
    clean_white.append(clean_ttm(str(x)))

# Check data accurate + len lines up with breakdown data
clean_white
len(clean_white)
len(bd_clean) * 2

#### Put Together and Save Dataframe ####

# create dictionary of lists for each column 
# financial information from columns was read horizontally --> need every third/second variable in list
nflx_dict = {
    'BREAKDOWN':bd_clean,
    'TMM': clean_grey[0::3], 
    '12/30/2021': clean_white[0::2],
    '12/30/2020':clean_grey[1::3],
    '12/30/2019':clean_white[1::2],
    '12/30/2018': clean_grey[2::3]
}

# Turn dictionary into data frame
df = pd.DataFrame.from_dict(nflx_dict)
df
# Save dataframe to csv file
df.to_csv('web-scraping/data/nflex_income_statement.csv')


