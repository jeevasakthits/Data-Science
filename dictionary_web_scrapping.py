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



inp=input("Enter You Required Company")


e=[]
t=[]
"""
for k in range(26):
    inp=ord(inp)
    inp=inp+k
    inp=chr(inp)
    #Collecting data from trustpilot for particular company
    for i in range(1,1000):
        try:
            r=r=requests.get("https://ilearntamil.com/english-to-tamil-translation/?letter="+inp+"&cpage="+str(i))
            soup = BeautifulSoup(r.text, "lxml")
            review=review=soup.select("td")
            print(len(review))
            if len(review)==0:
                print(len(e))
                break
            j=2
            while(j<len(review)):
                e.append(review[j])
                t.append(review[j+1])
                j=j+2
        except:
            print(len(e))
            print("Ended page for read")
            break
print(e[0])
print(t[0])
"""




for i in range(1,1000):
    try:
        r=r=requests.get("https://ilearntamil.com/english-to-tamil-translation/?cpage="+str(i))
        soup = BeautifulSoup(r.text, "lxml")
        review=review=soup.select("td")
        print(len(review))
        if len(review)==0:
            print(len(e))
            break
        j=2
        while(j<len(review)):
            e.append(review[j])
            t.append(review[j+1])
            j=j+2
    except:
        print(len(e))
        print("Ended page for read")
        break








import os
os.chdir("F:/tamil")
#Storing scrabbed data into csv file
webscrp=pd.DataFrame()
webscrp["English"]=e
webscrp["Tamil"]=t

len(e)
webscrp.to_csv("eng_to_tamil.csv")


df=pd.read_csv("Tamil_to_english.csv")

df.head()
df.tail()


e=list(webscrp["English"])
t=list(webscrp["Tamil"])
e.extend(df["Tamil"])
t.extend(df["English"])


import re

for i in range(len(e)):
    e[i]=re.sub("<td>","",str(e[i]))
    e[i]=re.sub("</td>","",str(e[i]))
    e[i]=re.sub("<br/>",",",str(e[i]))
    t[i]=re.sub("<td>","",str(t[i]))
    t[i]=re.sub("</td>","",str(t[i]))
    t[i]=re.sub("<br/>",",",str(t[i]))


    








df=pd.DataFrame()
df["English"]=e
df["Tamil"]=t

df.to_excel("Combined_en_ta.xlsx",index=False)



df_Sent1=pd.read_excel("F:/tamil/tamil_parallel/920663gcdr_tamil/enta.xlsx")

df_Sent1.head()







soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())

