# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 13:11:39 2020

@author: User
"""

from selenium import webdriver;import time;import pickle;import pandas as pd;import re;import random;import os
#Change The Directory
driver = webdriver.PhantomJS('C:/Users/User/Downloads/phantomjs-2.1.1-windows/bin/phantomjs') 
#Change Direcory
os.chdir('F:/telugu_dictionary/telugu_google_transV1')
#Read File 
dkl=pd.read_excel('English_words.xlsx');English_word=dkl["English"];l = [];tmap = {};l1 = [];tmap1 = {}

#Give 10000 limit from 60000
#upto len(English_word)
for ind, i in enumerate(English_word[60000:70000]):
    text=i
    tlist = []
    tlist1 = []
    #print(text)
    try:
        driver.get("https://translate.google.com/#view=home&op=translate&sl=en&tl=te&text={}".format(text))
        time.sleep(1)
        #print(i)
        try:
            content = driver.find_element_by_css_selector('.gt-baf-table')       # tlid-translation.translation    .gt-baf-table
            txt = content.text.split('\n')
            for t in txt:
                if re.sub('[^\u0C00-\u0C7F ]', '', t):
                    tlist.append(t)
            tmap[i] = tlist   
        except Exception as e:
            tmap[i] = []
            print(e)
        if ind % 10 == 0:
            print(ind)
            print(txt)
            #Rename the files like Google_trans_telugu_2_7_trans
            pickle.dump(tmap, open('Google_trans_telugu_2_6_trans.pkl', 'wb'))
        try:
            content = driver.find_element_by_css_selector('.tlid-translation.translation')       # tlid-translation.translation    .gt-baf-table
            txt = content.text.split('\n')
            for t in txt:
                if re.sub('[^\u0C00-\u0C7F ]', '', t):
                    tlist1.append(t)
            tmap1[i] = tlist1
        except Exception as e:
            tmap1[i] = []
            print(e)
        if ind % 10 == 0:
            print(txt)
            print(ind)
            #Rename the files like Google_trans_telugu_1_7_trans
            pickle.dump(tmap1, open('Google_trans_telugu_1_6_trans.pkl', 'wb'))
    except:
        driver = webdriver.PhantomJS('C:/Users/User/Downloads/phantomjs-2.1.1-windows/bin/phantomjs')
print(tmap)
print(tmap1)