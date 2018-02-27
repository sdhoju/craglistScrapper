# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 20:51:16 2018

@author: CREX
"""
import csv




import pandas, sys
import pandas as pd

with open("..\data\part_2.tsv",encoding="utf8") as fd:

    rd = csv.reader(fd, delimiter="\t", quotechar='"')
    for row in rd:
        urls.append(row[0])
    print("Extracted urls for tsv file")

a = pd.read_csv("part_2.tsv",delimiter="\t",error_bad_lines=False)
b = pd.read_csv("part_3.tsv",delimiter="\t",error_bad_lines=False)

merged = a.merge(b, on = "url")

merged.to_csv('..\data\bonus.tsv', sep="\t", encoding='utf-8', index=False)
    
#bonus = pd.DataFrame(columns=['Posting time ','Number of images', 'Description under the image','Year',
#                              'Make and Model ','Condition ', 'Cylinders ','Drive ','Fuel ','Odometer ',
#                              'Paint color','Size','Title Status ','Transmission','VIN'])
#   