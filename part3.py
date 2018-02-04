# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import pandas as pd # Pandas helps you with managing Data (csv, excel, txt, etc.)
import numpy as np # Numpy helps you with Numerical Calculation (matrix, vectors operation, etc.)
import sklearn # This is a very popular package full of data mining algorithms.
import csv
from bs4 import BeautifulSoup as bsp # It makes web scraping easy.
import requests # It helps to retrieve contents of a URL
import re # A package for using regular expressions

import time

print("start")
#part 3
def getPageContent3(url):
    r = requests.get(url) # Retrieves the content of the URL
    bs = bsp(r.text, "lxml") # Using "lxml" HTML parser to parse the content of the URL
    return bs
data3 = pd.DataFrame(columns=['Posting time ','Number of images', 'Description under the image','Year',
                              'Make and Model ','Condition ', 'Cylinders ','Drive ','Fuel ','Odometer ',
                              'Paint color','Size','Title Status ','Transmission','VIN','url'])
    
a=0
urls=[]    
with open("part_2.tsv",encoding="utf8") as fd:

    rd = csv.reader(fd, delimiter="\t", quotechar='"')
    for row in rd:
        urls.append(row[0])
    print("Extracted urls for tsv file")

def main(urls):
    urls.pop(0)
    for url in urls:
        try:
            print("Scrapping from "+ url)
            bs = getPageContent3(url)
            
            posting_time,num_of_images,desc_img,year, make_model,condition, cylinders ,drive ,fuel ,odometer,color,size,status,transmission,vin,url1=[None]*15
            url1=url
            try:
                posting_time = bs.find("time", { "class" : "date timeago" }).get_text().lstrip()
            except:
                posting_time=None
            try:
                num_of_images = len(bs.find("div", { "id" : "thumbs" }))
            except:
                num_of_images=None
            try:
                desc_img = bs.find("section",{"id":"postingbody"}).get_text().lstrip().lstrip('QR Code Link to This Post').lstrip()
            except:
                desc_img=None
            try:
                ds=bs.find_all('p',{'class':'attrgroup'})
                year = ds[0].get_text().split(' ')[0].lstrip()
                spans=ds[1].find_all('span')
                
                for span in spans:
        #            print(span.get_text().split(':')[0])
                    if str(span.get_text().split(':')[0]) == "condition":
                        condition = span.get_text().split(':')[1]
        
                    elif span.get_text().split(':')[0] == "cylinders":
                        cylinders = span.get_text().split(':')[1]
                    
                    elif span.get_text().split(':')[0] == "drive":
                        drive = span.get_text().split(':')[1]
                    elif span.get_text().split(':')[0] == "fuel":
                        fuel = span.get_text().split(':')[1]
                    elif span.get_text().split(':')[0] =="odometer":
                        odometer = span.get_text().split(':')[1]
                    elif span.get_text().split(':')[0] == "paint color":
                        color = span.get_text().split(':')[1]
                    elif span.get_text().split(':')[0] == "size":
                        size = span.get_text().split(':')[1]
                    elif span.get_text().split(':')[0] =="title status":
                        status = span.get_text().split(':')[1]
                    elif span.get_text().split(':')[0] == "transmission":
                        transmission = span.get_text().split(':')[1]
                    elif span.get_text().split(':')[0] == "VIN":
                        vin = span.get_text().split(':')[1]
            except:
                 a=0
            i = data3.shape[0]
            data3.loc[i] = [posting_time,num_of_images,desc_img,year, make_model,condition, cylinders ,drive ,fuel ,odometer,color,size,status,transmission,vin,url1]
        except:
            i = data3.shape[0]
            data3.loc[i] = [posting_time,num_of_images,desc_img,year, make_model,condition, cylinders ,drive ,fuel ,odometer,color,size,status,transmission,vin,url1]
    print("Scrapped all data")
    data3.to_csv('part_3.tsv',sep="\t", encoding='utf-8', index=False)
    print("Successfully write in part_3.tsv file")
    
main(urls)
print("End")