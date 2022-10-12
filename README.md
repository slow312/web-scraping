# web-scraping

**Required Packages**<br/>
import requests <br/>
from bs4 import BeautifulSoup <br/>
import pandas <br/> 
<br/>
**Scrape NYT article titles and descriptions (file1.py)** <br/>
1. Article titles were found under "h2" tag <br/>
2. Replaced extra text around the article title with an empty string and added the titles in a seperate list
3. Article descriptions were found in the "p" tag <br/>
4. Similar to the article titles, the extra text was replaced with an empty string <br/>
5. Both lists were combined into a single dataframe <br/>

**Scrape Netflix's Income Statement from Yahoo Finance (file2.py)**<br/>
1. The financial statement's breakdown was found under the "div" tag <br/>
2. I used a regex expression to find the breakdown string saved between the other html tags <br/>
(I was having trouble getting the full regex pattern, so I used an additional .split() function to get rid of the rest of the text)<br/>
3. The final breakdown titles were saved in a seperate list<br/>

4. The income statement's numerical information were saved under the "div" tag <br/> 
(The income statement was seperated into grey and white columns. I had to pull the grey and white columns seperately to get the full chart)<br/>
5. A seperate function was created called "clean_ttm()" and was used to scan each html block for a specific regex pattern <br/>
6. "clean_ttm()" was used to get the numerical information from the income statement and save it into a seperate list <br/>

7. A new dictionary was created to save the resulting lists with their column name that I manually added <br/>
(While iterating through the grey and white columns, the income statement was being read from left to right. I had to splice the list to get the values for each column)<br/>
8. The dictionary was converted into a dataframe and saved as a csv file

