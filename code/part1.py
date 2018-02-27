# -*- coding: utf-8 -*-

import pandas as pd 

from bs4 import BeautifulSoup as bsp # It makes web scraping easy.
import requests # It helps to retrieve contents of a URL
import re # A package for using regular expressions


#PArt 1 function
def getPageContent():
    url = 'https://northmiss.craigslist.org/search/cta?s=0'
    r = requests.get(url) # Retrieves the content of the URL
    bs = bsp(r.text, "lxml") # Using "lxml" HTML parser to parse the content of the URL
    return bs

#PArt 2 function
def getPageContents(items):
    url = 'https://northmiss.craigslist.org/search/cta?s='+str(items)
    r = requests.get(url) # Retrieves the content of the URL
    bs = bsp(r.text, "lxml") # Using "lxml" HTML parser to parse the content of the URL
    return bs
data = pd.DataFrame(columns=['url','Title', 'Price', 'City', 'State'])
for items in range(0,2316,120):
    bs = getPageContents(items)
    cars = bs.findAll("li", { "class" : "result-row" })
    for car in cars:
        url,title, price, city, state = [None]*5
        
        url = car.find('a').get('href')
        title = car.find('a', {"class":"result-title hdrlnk"}).contents[0]
        try:
            price=car.find('span',{"class":"result-price"}).contents[0]
        except:
            price=None

        try:
            text=car.find('span',{"class":"result-hood"}).contents[0]
            text=re.sub('[()]','',text)
            try:
                a_text=text.split(",")
                city=a_text[0]
                state=a_text[1]
            except:
                city=text.split(" ")[1]
                if city != "Get":
                    city=text
                else:
                    city=None
                
        except:
            city=None
      
        i = data.shape[0]
        data.loc[i] = [url,title, price, city, state ]    

print(data)
data.to_csv('..\data\part_2.tsv',sep="\t", encoding='utf-8', index=False)