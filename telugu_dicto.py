# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 10:55:11 2019

@author: User
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 12:10:23 2019

@author: User
"""
# Web Scrapping
import requests
from bs4 import BeautifulSoup


#importing required packages
import requests
import urllib.request
import time 
from bs4 import BeautifulSoup
from html.parser import HTMLParser
import lxml
import pandas as pd
import re


etxt=[]
for j in range(26):
    inp="A"
    inp=ord(inp)
    inp=inp+j
    inp=chr(inp)
    r=requests.get("https://studysite.org/dictionary/english-to-telugu?Alphabet="+str(inp))
    soup = BeautifulSoup(r.text, "lxml")
    review=soup.select(".tdfont+ table a")
    for i in range(len(review)):
        s=review[i].text
        s=re.sub(", \xa0 ","",s)
        etxt.append(s)
        
print(len(etxt))
print(etxt[0:10])


ttxt=[]

for i in range(5404,len(etxt)):
    try:
        r=requests.get("https://studysite.org/dictionary/Telugu-meaning-of-"+str(etxt[i]))
        soup = BeautifulSoup(r.text, "lxml")
        review=soup.select("tr:nth-child(2) > td+ td , tr:nth-child(1) td+ td b")
        for j in range(len(review)):
            s=review[j].text
            s=re.sub("[\r\n\t]","",s)
            ttxt.append(s)
    except:
        #ttxt.append("None")
        print(len(ttxt))
        print("Ended page for read")

len1=len(ttxt)
"""
for i in range(abs(len(etxt)-len(ttxt))):
    ttxt.append("None")


import os
os.chdir("F:/telugu_dictionary")
#Storing scrabbed data into csv file
webscrp=pd.DataFrame()
webscrp["English"]=etxt
webscrp["Telugu"]=ttxt
webscrp.to_excel("English_to_Telugu.xlsx")

import os
os.chdir("F:/telugu_dictionary")
#Storing scrabbed data into csv file
webscrp=pd.DataFrame()
webscrp["English"]=etxt
webscrp["Telugu"]=ttxt
webscrp.to_excel("English_to_Telugu.xlsx")

"""
import os
os.chdir("F:/telugu_dictionary")
#Storing scrabbed data into csv file
webscrp1=pd.DataFrame()
webscrp1["Telugu"]=ttxt
webscrp1.to_excel("English_to_Telugu1.xlsx")



