import requests
from bs4 import BeautifulSoup
import pandas as pd
from pandas.io.json import json_normalize

#url = 'http://www.nasdaq.com/market-activity/stocks/aapl/historical'
#headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'}
#r = requests.get(url).text
#print(r)



#response  = requests.get('https://www.wsj.com/market-data/quotes/index/UK/FTSE%20UK/UKX/historical-prices')
#soup = BeautifulSoup(response.text, 'html-parser')
#headers = soup.find('span': {'class':'<tr>'})
#print(headers)


                                                                                                             
url = 'https://www.wsj.com/market-data/quotes/index/UK/FTSE%20UK/UKX/historical-prices'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')



